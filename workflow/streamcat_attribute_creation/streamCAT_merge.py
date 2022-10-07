# Sample file to merge streamCat Merge
# Author : Rich Gibbs NWC, OWP, NOAA


import streamCAT_functions as sc

workdir = # your directory location 
outdir = # output directory

vpu = # Example: "11"

sc.add_region(workdir, outdir, vpu)
sc.join_csv(outdir , vpu)
sc.prune_csv(outdir, vpu)

