# This is a script to calculate and upload annual monthly means of GLASS attributes for non-leap years
# pairs with python script monthlyMean.py
# Author: Rich Gibbs, NOAA, NWS, Office of Water Prediction, National Water Center

import monthlyMean as mm
import cleanup

workdir = #Some working directory (example: 'C:/Users/Username/Documents/'
attribute = #GLASS attribute in s3 bucket (either 'LAI' or 'FVC')
year = #year (2000-2021)

mm.jan_reg(workdir, attribute, year)
mm.feb_reg(workdir, attribute, year)
mm.mar_reg(workdir, attribute, year)
mm.apr_reg(workdir, attribute, year)
mm.may_reg(workdir, attribute, year)
mm.jun_reg(workdir, attribute, year)
mm.jul_reg(workdir, attribute, year)
mm.aug_reg(workdir, attribute, year)
mm.sep_reg(workdir, attribute, year)
mm.oct_reg(workdir, attribute, year)
mm.nov_reg(workdir, attribute, year)
mm.dec_reg(workdir, attribute, year)

cleanup.del_files(workdir)
