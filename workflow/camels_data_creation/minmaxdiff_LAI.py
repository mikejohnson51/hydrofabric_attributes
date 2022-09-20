# Make sure to change download_month (line 6) variable before running script
# Author: Rich Gibbs, NOAA, NWS, Office of Water Prediction, National Water Center

import multiCOG as mc

download_month = #example: 'DEC'

mc.download_tiffs(download_month, '2001')
mc.download_tiffs(download_month, '2002')
mc.download_tiffs(download_month, '2003')
mc.download_tiffs(download_month, '2004')
mc.download_tiffs(download_month, '2005')
mc.download_tiffs(download_month, '2006')
mc.download_tiffs(download_month, '2007')
mc.download_tiffs(download_month, '2008')
mc.download_tiffs(download_month, '2009')
mc.download_tiffs(download_month, '2010')
mc.download_tiffs(download_month, '2011')
mc.download_tiffs(download_month, '2012')
mc.download_tiffs(download_month, '2013')
mc.download_tiffs(download_month, '2014')
mc.download_tiffs(download_month, '2015')
mc.download_tiffs(download_month, '2016')
mc.download_tiffs(download_month, '2017')
mc.download_tiffs(download_month, '2018')
mc.download_tiffs(download_month, '2019')
mc.download_tiffs(download_month, '2020')
mc.download_tiffs(download_month, '2021')

mc.multidim_COG(download_month)

mc.min_max_diff(download_month)

mc.upload_MinMaxDiff(download_month)

