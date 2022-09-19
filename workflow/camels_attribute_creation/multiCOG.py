# The script contains the definitions for generating multidimensional COGs, min/max/diff COGs of GLASS attribute means, and uploads/downloads from Lynker s3 bucket
# pairs with minmaxdiff.py
# Author: Rich Gibbs, NOAA, NWS, Office of Water Prediction, National Water Center

import boto3
import rasterio as rio
import numpy as np
import os, glob
import subprocess

wd = #set working directory path
attribute = #'LAI' or 'FVC'

# AWS config/credentials file
os.environ['AWS_PROFILE'] = "lynker_aws"

# Define ' + attribute + ' Tiffs Download Function
def download_tiffs(month, year):
    # Let's use Amazon S3
    s3 = boto3.resource('s3')
    print("[INFO:] Connecting to cloud")
    formdev = s3.Bucket('formulations-dev')
    
    print('--- Downloading ' + month + ' ' + year + ' ---')
    prefix = 'spatial-grids/GLASS/' + attribute + '_monthlymean/' + attribute + '_' + year + '_' + month
    my_bucket = s3.Bucket('formulations-dev')
    objects = my_bucket.objects.filter(Prefix=prefix)
    for obj in objects:
        path, filename = os.path.split(obj.key)        
        my_bucket.download_file(obj.key, filename)
    del prefix, objects
    
    print('--- Download Complete ---')
           
# Define Multidimensional COG Creation
def multidim_COG(month): 
    # Final COG path
    COG = wd + '' + attribute + '_' + month + '.tif'
    
    file_list = glob.glob(wd + '*'+ month + '.tif')
    print(file_list)
    
    # Create tuple for reference band names based on filenames
    files = [os.path.basename(x) for x in file_list]
    names = [os.path.splitext(x)[0] for x in files]
    bands = tuple(names)

    # Read metadata of first file
    with rio.open(file_list[0]) as src0:
        meta = src0.meta

    # Update meta to reflect the number of layers
    meta.update(count = len(file_list))

    # Read each layer and write it to stack
    with rio.open(COG,'w', **meta) as dst:
        for id, layer in enumerate(file_list, start=1):
            with rio.open(layer) as src1:
                dst.write_band(id, src1.read(1))
                dst.descriptions=bands
              
    print('--- COG generated! ---')
    
def upload_COG(month):
    print('--- Beginning Upload ---')
    
    # Let's use Amazon S3
    s3 = boto3.resource('s3')
    print("[INFO:] Connecting to cloud")
    formdev = s3.Bucket('formulations-dev')
    
    output_month = wd + '' + attribute + '_' + month + '.tif'

    upload_prefix = 'spatial-grids/GLASS/' + attribute + '_multidim/'
    my_bucket = s3.Bucket('formulations-dev')
    object_name = upload_prefix + os.path.basename(output_month)
    my_bucket.upload_file(output_month, object_name)
    
    print('--- Upload Complete ---')

# Calculate Max, Min, and differece of the two and generate COGS    
def min_max_diff(month):
    # Input COG
    input_COG = wd + '' + attribute + '_' + month + '.tif'
    
    # Final COG paths
    MAX = wd + '' + attribute + '_MAX_' + month + '.tif'
    MIN = wd + '' + attribute + '_MIN_' + month + '.tif'
    DIFF = wd + '' + attribute + '_DIFF_' + month + '.tif'
    
    print('--- Loading Tiff ---')    
    raster = rio.open(input_COG)
    
    print('--- Creating Arrays ---')
    year1 = raster.read(1, masked = True)
    year1_array = np.array(year1, dtype='float32')
    del year1
    
    year2 = raster.read(2, masked = True)
    year2_array = np.array(year2, dtype='float32')
    del year2
    
    year3 = raster.read(3, masked = True)
    year3_array = np.array(year3, dtype='float32')
    del year3
    
    year4 = raster.read(4, masked = True)
    year4_array = np.array(year4, dtype='float32')
    del year4
    
    year5 = raster.read(5, masked = True)
    year5_array = np.array(year5, dtype='float32')
    del year5
    
    year6 = raster.read(6, masked = True)
    year6_array = np.array(year6, dtype='float32')
    del year6
    
    year7 = raster.read(7, masked = True)
    year7_array = np.array(year7, dtype='float32')
    del year7
    
    year8 = raster.read(8, masked = True)
    year8_array = np.array(year8, dtype='float32')
    del year8
    
    year9 = raster.read(9, masked = True)
    year9_array = np.array(year9, dtype='float32')
    del year9
    
    year10 = raster.read(10, masked = True)
    year10_array = np.array(year10, dtype='float32')
    del year10
    
    year11 = raster.read(11, masked = True)
    year11_array = np.array(year11, dtype='float32')
    del year11
    
    year12 = raster.read(12, masked = True)
    year12_array = np.array(year12, dtype='float32')
    del year12
    
    year13 = raster.read(13, masked = True)
    year13_array = np.array(year13, dtype='float32')
    del year13
    
    year14 = raster.read(14, masked = True)
    year14_array = np.array(year14, dtype='float32')
    del year14
    
    year15 = raster.read(15, masked = True)
    year15_array = np.array(year15, dtype='float32')
    del year15
    
    year16 = raster.read(16, masked = True)
    year16_array = np.array(year16, dtype='float32')
    del year16
    
    year17 = raster.read(17, masked = True)
    year17_array = np.array(year17, dtype='float32')
    del year17
    
    year18 = raster.read(18, masked = True)
    year18_array = np.array(year18, dtype='float32')
    del year18
    
    year19 = raster.read(19, masked = True)
    year19_array = np.array(year19, dtype='float32')
    del year19
    
    year20 = raster.read(20, masked = True)
    year20_array = np.array(year20, dtype='float32')
    del year20
    
    year21 = raster.read(21, masked = True)    
    year21_array = np.array(year21, dtype='float32')
    del year21
    
    raster.close()
    
    print('--- Creating 3d Array ---')
    
    # Create 3d array of bands
    array3d = [year1_array, year2_array, year3_array, year4_array, year5_array, year6_array, year7_array, year8_array, year9_array, year10_array, year11_array, year12_array, year13_array, year14_array, year15_array, year16_array, year17_array, year18_array, year19_array, year20_array, year21_array]
    del year1_array, year2_array, year3_array, year4_array, year5_array, year6_array, year7_array, year8_array, year9_array, year10_array, year11_array, year12_array, year13_array, year14_array, year15_array, year16_array, year17_array, year18_array, year19_array, year20_array, year21_array
    
    print('--- Beginning Calculations ---')
    
    # Calculate max and min arrays
    maximum = np.amax(array3d, axis=0)
    minimum = np.amin(array3d, axis=0)
    del array3d
    
    # Calculate difference array
    difference = np.absolute(maximum-minimum)
    
    print('--- Calculations Complete! ---')
    
    print('--- Writing COGs ---')
    
    # Write arrays as new COGs
    max_cog =  rio.open(MAX,'w', driver='COG', height=raster.shape[0], width=raster.shape[1], count=1, dtype='float32', nodata='nan', crs=raster.crs, transform=raster.transform,)
    max_cog.write(maximum, 1)
    max_cog.close()
    del max_cog, maximum
    
    min_cog =  rio.open(MIN,'w', driver='COG', height=raster.shape[0], width=raster.shape[1], count=1, dtype='float32', nodata='nan', crs=raster.crs, transform=raster.transform,)
    min_cog.write(minimum, 1)
    min_cog.close()
    del min_cog, minimum
    
    diff_cog =  rio.open(DIFF,'w', driver='COG', height=raster.shape[0], width=raster.shape[1], count=1, dtype='float32', nodata='nan', crs=raster.crs, transform=raster.transform,)
    diff_cog.write(difference, 1)
    diff_cog.close()
    del diff_cog, difference
              
    print('--- COGs generated! ---')
    
def upload_MinMaxDiff(month):
    print('--- Beginning Upload ---')
    
    # Let's use Amazon S3
    s3 = boto3.resource('s3')
    print("[INFO:] Connecting to cloud")
    formdev = s3.Bucket('formulations-dev')
    
    # Final COG paths
    MAX = wd + '' + attribute + '_MAX_' + month + '.tif'
    MIN = wd + '' + attribute + '_MIN_' + month + '.tif'
    DIFF = wd + '' + attribute + '_DIFF_' + month + '.tif'
    
    upload_prefix = 'spatial-grids/GLASS/' + attribute + '_MinMaxDiff/'
    my_bucket = s3.Bucket('formulations-dev')
    object_name = upload_prefix + os.path.basename(MAX)
    my_bucket.upload_file(MAX, object_name)
    print('--- Max Uploaded ---')
    
    upload_prefix = 'spatial-grids/GLASS/' + attribute + '_MinMaxDiff/'
    my_bucket = s3.Bucket('formulations-dev')
    object_name = upload_prefix + os.path.basename(MIN)
    my_bucket.upload_file(MIN, object_name)
    print('--- Min Uploaded ---')
    
    upload_prefix = 'spatial-grids/GLASS/' + attribute + '_MinMaxDiff/'
    my_bucket = s3.Bucket('formulations-dev')
    object_name = upload_prefix + os.path.basename(DIFF)
    my_bucket.upload_file(DIFF, object_name)
    print('--- Diff Uploaded ---')
    
    print('--- Upload Complete ---')