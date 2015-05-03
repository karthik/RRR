all: vis_results.md

vis_results.md: vis_results.Rmd
	/usr/bin/Rscript -e "library(knitr); knit('vis_results.Rmd')"	


