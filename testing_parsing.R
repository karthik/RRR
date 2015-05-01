library(dplyr)
library(readr)
library(progress)
library(parallel)
# You must also have package called reader
# Otherwise install.packages("reader") not to be confused with readr

# Grabs the start of each record and how many lines it contains
get_bounds <- function(file) {
  ll <- read.fwf(file, widths=c(2, 500), as.is = TRUE)
  dividers <- which(ll[, 1] == "ER") # ER denotes end of record
  start <- c(0, dividers[1:(length(dividers) - 1)])
  start <- start
  back <- dividers - 1
  start[1] <- 0 # reset the first item to be 0 since we don't skip at top
  count <- back - start
  data.frame(st = start, n = count)
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
#  Pulls out each record from a giant file of records. The "bounds" df contains
# how many lines to skip and how many lines to read from that point forward
new_parse <- function(file, start, end) {
  message("file: ", file, "| start: ", start, "| end ", end, "\n")
  x <- paste(reader::n.readLines(file,skip = start, n = end), collapse = "\n")
  parseEntry(x)
}

# Basically pulls together the above two fns
# The mapply
meta_parse <- function(dataset, output) {
  bounds <- get_bounds(dataset)
  res <- mapply(new_parse,
                  file = dataset,
                  start = bounds$st,
                  end = bounds$n,
                  SIMPLIFY = FALSE)
  res_df <- data.table::rbindlist(res, fill = TRUE)
  # Remove factors
  res_df <- tbl_df(data.frame(res_df, stringsAsFactors = FALSE))
  # Pub type, author, title, source, abstract, DOI, pub year
  res_df_clean <- res_df %>% select(PT, AU, TI, SO, AB, DI, PY)
  write_csv(res_df_clean, path = output)
  invisible()
}

# Read the three files in the sample_wos_queries folder
files <- paste0("sample_wos_queries/", dir("sample_wos_queries/"))

meta_parse(files[1], "parsed/Repeatibility.csv")
meta_parse(files[2], "parsed/Replicability.csv")
meta_parse(files[3], "parsed/Reproducibility.csv") # This takes several minutes
