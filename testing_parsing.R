# bounds function
# Used the following regular expression to replace empty lines with "---"
#   ^(?:[\t ]*(?:\r?\n|\r))+
# Did this in my code editor
library(dplyr)
library(readr)
library(progress)

# Grabs the start of each record and how many lines it contains
get_bounds <- function(file) {
  ll <- read.fwf(file, widths=c(2,500), as.is = TRUE)
  dividers <- which(ll[, 1] == "--")
  start <- c(0, dividers[1:(length(dividers)-1)])
  start <- start
  back <- dividers - 1
  start[1] <- 0 # reset the firs to be 0
  count <- back - start
  d <- data.frame(st = start, en = back, n = count)
}


# Parsed each record
parseEntry <- function(entry) {
  ## Split at beginning of each line that starts with a non-space character
  ll <- strsplit(entry, "\\n(?=\\S)", perl=TRUE)[[1]]
  ## Clean up empty characters at beginning of continuation lines
  ll <- gsub("\\n(\\s){3}", "", ll)
  ## Split each field into its two components
  x <- read.fwf(textConnection(ll), c(2, max(nchar(ll))), stringsAsFactors = FALSE)
  df <- data.frame(t(x[, 2]))
  names(df) <- as.character(x[, 1])
  df
}
#  Pulls out each record from a giant file of records
new_parse <- function(file, start, end) {
  message("file: ", file, "| start: ", start, "| end ", end, "\n")
  x <- paste(reader::n.readLines(file,skip = start, n = end), collapse = "\n")
  parseEntry(x)
}

meta_parse <- function(dataset, output) {
  bounds <- get_bounds(dataset)
  res <- mapply(new_parse, file = dataset, start = bounds$st, end = bounds$n,  SIMPLIFY = FALSE)
  res_df <- data.table::rbindlist(res, fill = TRUE)
  # Remove factors
  res_df <- data.frame(res_df, stringsAsFactors = FALSE)
  write_csv(res_df, path = output)
  invisible()
}

# Read the three files in the sample_wos_queries folder
files <- paste0("sample_wos_queries/", dir("sample_wos_queries/"))

meta_parse(files[1], "parsed/Repeatibility.csv")
meta_parse(files[2], "parsed/Replicability.csv")
meta_parse(files[3], "parsed/Reproducibility.csv") # This takes several minutes
