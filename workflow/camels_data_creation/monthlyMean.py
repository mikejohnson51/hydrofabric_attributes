# monthly mean definitions file for GLASS attributes
# pairs with monthlyMean_reg.py & monthlyMean_leap.py
# only 4 months change due to leap years (April, May, October, and November)
# Author: Rich Gibbs, NOAA, NWS, Office of Water Prediction, National Water Center

import boto3
import rasterio as rio
import numpy as np
import os, glob
import subprocess

# AWS config/credentials file
os.environ['AWS_PROFILE'] = "lynker_aws"


# Define January parameters    
def jan_reg(workdir, attribute, year):

    # Let's use Amazon S3
    s3 = boto3.resource('s3')
    print("[INFO:] Connecting to cloud")

    formdev = s3.Bucket('formulations-dev')

    print("--- Beginning January ---")
    
    month = 'JAN'
    
    # timestep constants
    ts1 = '001'
    ts2 = '009'
    ts3 = '017'
    ts4 = '025'
    
    # final upload prefix
    uploadprefix = 'spatial-grids/GLASS/' + attribute + '_monthlymean/'

    output_month = workdir + attribute + '_' + year + '_' + month + '.tif'
    
    # Define January Download
    def download_jan(timestep):
        prefix = 'spatial-grids/GLASS/' + attribute + '_mosaic/' + attribute + '_' + year + '_' + timestep
        objects = formdev.objects.filter(Prefix=prefix)
        for obj in objects:
            path, filename = os.path.split(obj.key)        
            formdev.download_file(obj.key, filename)
    
    print("--- Beginning Download ---")
    
    # Download January COGs by corresponding timestep
    download_jan(ts1)
    download_jan(ts2)
    download_jan(ts3)
    download_jan(ts4)

    
    # Average tifs and save output as Cloud-optimized Geotiff
    def mean_jan(tif1, tif2, tif3, tif4):
        print("--- Beginning Raster Algebra ---")
        
        # Open corresponding tifs in Rasterio and convert to 2D arrays
        fp = workdir + attribute + '_' + year + '_' + tif1 + '.tif'
        mosaic = rio.open(fp)
        file1 = mosaic.read(1, masked=True)
        file1_array = np.array(file1, dtype='float64')
        del fp, mosaic, file1
        
        fp = workdir + attribute + '_' + year + '_' + tif2 + '.tif'
        mosaic = rio.open(fp)
        file2 = mosaic.read(1, masked=True)
        file2_array = np.array(file2, dtype='float64')
        del fp, mosaic, file2
        
        fp = workdir + attribute + '_' + year + '_' + tif3 + '.tif'
        mosaic = rio.open(fp)
        file3 = mosaic.read(1, masked=True)
        file3_array = np.array(file3, dtype='float64')
        del fp, mosaic, file3
        
        fp = workdir + attribute + '_' + year + '_' + tif4 + '.tif'
        mosaic = rio.open(fp)
        file4 = mosaic.read(1, masked=True)
        file4_array = np.array(file4, dtype='float64')
        del fp, file4
        
        # Create 3D Array of 2D arrays
        array3d = [file1_array, file2_array, file3_array, file4_array]    
        del file1_array, file2_array, file3_array, file4_array
        
        # monthly mean calculation
        monthly_mean1 = np.mean(array3d, axis=0)
        monthly_mean = np.where(monthly_mean1<0, np.nan, monthly_mean1)
        del array3d, monthly_mean1
        
        print("--- Calculation Complete! ---")
        
        print("--- Generating COG ---")
        
        # Write array as new COG
        new_dataset =  rio.open(output_month,'w', driver='COG', height=mosaic.shape[0], width=mosaic.shape[1], count=1, dtype='float32', nodata='nan', crs=mosaic.crs, transform=mosaic.transform,)
        new_dataset.write(monthly_mean, 1)
        new_dataset.close()
        
        print("--- COG Generated! ---")
        
        del monthly_mean, new_dataset, mosaic
    
    mean_jan(ts1, ts2, ts3, ts4)
    
    def upload_jan():
    
        print("--- Beginning Upload ---")
    
        # Upload monthly mean COG to the corresponding folder on the AWS s3 bucket
        object_name = uploadprefix + os.path.basename(output_month)
        formdev.upload_file(output_month, object_name)
        
        print("--- Upload Complete ---")
    
    upload_jan()
    
    print("--- January Done ---")

# Define February parameters    
def feb_reg(workdir, attribute, year):

    # Let's use Amazon S3
    s3 = boto3.resource('s3')
    print("[INFO:] Connecting to cloud")

    formdev = s3.Bucket('formulations-dev')

    print("--- Beginning February ---")
    
    month = 'FEB'
    
    # timestep constants
    ts1 = '033'
    ts2 = '041'
    ts3 = '049'
    ts4 = '057'
    
    # final upload prefix
    uploadprefix = 'spatial-grids/GLASS/' + attribute + '_monthlymean/'

    output_month = workdir + attribute + '_' + year + '_' + month + '.tif'
    
    # Define February Download
    def download_feb(timestep):
        prefix = 'spatial-grids/GLASS/' + attribute + '_mosaic/' + attribute + '_' + year + '_' + timestep
        objects = formdev.objects.filter(Prefix=prefix)
        for obj in objects:
            path, filename = os.path.split(obj.key)        
            formdev.download_file(obj.key, filename)
    
    print("--- Beginning Download ---")
    
    # Download February COGs by corresponding timestep
    download_feb(ts1)
    download_feb(ts2)
    download_feb(ts3)
    download_feb(ts4)

    
    # Average tifs and save output as Cloud-optimized Geotiff
    def mean_feb(tif1, tif2, tif3, tif4):
        print("--- Beginning Raster Algebra ---")
        
        # Open corresponding tifs in Rasterio and convert to 2D arrays
        fp = workdir + attribute + '_' + year + '_' + tif1 + '.tif'
        mosaic = rio.open(fp)
        file1 = mosaic.read(1, masked=True)
        file1_array = np.array(file1, dtype='float64')
        del fp, mosaic, file1
        
        fp = workdir + attribute + '_' + year + '_' + tif2 + '.tif'
        mosaic = rio.open(fp)
        file2 = mosaic.read(1, masked=True)
        file2_array = np.array(file2, dtype='float64')
        del fp, mosaic, file2
        
        fp = workdir + attribute + '_' + year + '_' + tif3 + '.tif'
        mosaic = rio.open(fp)
        file3 = mosaic.read(1, masked=True)
        file3_array = np.array(file3, dtype='float64')
        del fp, mosaic, file3
        
        fp = workdir + attribute + '_' + year + '_' + tif4 + '.tif'
        mosaic = rio.open(fp)
        file4 = mosaic.read(1, masked=True)
        file4_array = np.array(file4, dtype='float64')
        del fp, file4
        
        # Create 3D Array of 2D arrays
        array3d = [file1_array, file2_array, file3_array, file4_array]    
        del file1_array, file2_array, file3_array, file4_array
        
        # monthly mean calculation
        monthly_mean1 = np.mean(array3d, axis=0)
        monthly_mean = np.where(monthly_mean1<0, np.nan, monthly_mean1)
        del array3d, monthly_mean1
        
        print("--- Calculation Complete! ---")
        
        print("--- Generating COG ---")
        
        # Write array as new COG
        new_dataset =  rio.open(output_month,'w', driver='COG', height=mosaic.shape[0], width=mosaic.shape[1], count=1, dtype='float32', nodata='nan', crs=mosaic.crs, transform=mosaic.transform,)
        new_dataset.write(monthly_mean, 1)
        new_dataset.close()
        
        print("--- COG Generated! ---")
        
        del monthly_mean, new_dataset, mosaic
    
    mean_feb(ts1, ts2, ts3, ts4)
    
    def upload_feb():
    
        print("--- Beginning Upload ---")
    
        # Upload monthly mean COG to the corresponding folder on the AWS s3 bucket
        object_name = uploadprefix + os.path.basename(output_month)
        formdev.upload_file(output_month, object_name)
    
        print("--- Upload Complete ---")
    
    upload_feb()
    
    print("--- February Done ---")
    
# Define March parameters    
def mar_reg(workdir, attribute, year):

    # Let's use Amazon S3
    s3 = boto3.resource('s3')
    print("[INFO:] Connecting to cloud")

    formdev = s3.Bucket('formulations-dev')

    print("--- Beginning March ---")
    
    month = 'MAR'
    
    # timestep constants
    ts1 = '033'
    ts2 = '041'
    ts3 = '049'
    ts4 = '057'
    
    # final upload prefix
    uploadprefix = 'spatial-grids/GLASS/' + attribute + '_monthlymean/'

    output_month = workdir + attribute + '_' + year + '_' + month + '.tif'
    
    # Define March Download
    def download_mar(timestep):
        prefix = 'spatial-grids/GLASS/' + attribute + '_mosaic/' + attribute + '_' + year + '_' + timestep
        objects = formdev.objects.filter(Prefix=prefix)
        for obj in objects:
            path, filename = os.path.split(obj.key)        
            formdev.download_file(obj.key, filename)
    
    print("--- Beginning Download ---")
    
    # Download March COGs by corresponding timestep
    download_mar(ts1)
    download_mar(ts2)
    download_mar(ts3)
    download_mar(ts4)

    
    # Average tifs and save output as Cloud-optimized Geotiff
    def mean_mar(tif1, tif2, tif3, tif4):
        print("--- Beginning Raster Algebra ---")
        
        # Open corresponding tifs in Rasterio and convert to 2D arrays
        fp = workdir + attribute + '_' + year + '_' + tif1 + '.tif'
        mosaic = rio.open(fp)
        file1 = mosaic.read(1, masked=True)
        file1_array = np.array(file1, dtype='float64')
        del fp, mosaic, file1
        
        fp = workdir + attribute + '_' + year + '_' + tif2 + '.tif'
        mosaic = rio.open(fp)
        file2 = mosaic.read(1, masked=True)
        file2_array = np.array(file2, dtype='float64')
        del fp, mosaic, file2
        
        fp = workdir + attribute + '_' + year + '_' + tif3 + '.tif'
        mosaic = rio.open(fp)
        file3 = mosaic.read(1, masked=True)
        file3_array = np.array(file3, dtype='float64')
        del fp, mosaic, file3
        
        fp = workdir + attribute + '_' + year + '_' + tif4 + '.tif'
        mosaic = rio.open(fp)
        file4 = mosaic.read(1, masked=True)
        file4_array = np.array(file4, dtype='float64')
        del fp, file4
        
        # Create 3D Array of 2D arrays
        array3d = [file1_array, file2_array, file3_array, file4_array]    
        del file1_array, file2_array, file3_array, file4_array
        
        # monthly mean calculation
        monthly_mean1 = np.mean(array3d, axis=0)
        monthly_mean = np.where(monthly_mean1<0, np.nan, monthly_mean1)
        del array3d, monthly_mean1
        
        print("--- Calculation Complete! ---")
        
        print("--- Generating COG ---")
        
        # Write array as new COG
        new_dataset =  rio.open(output_month,'w', driver='COG', height=mosaic.shape[0], width=mosaic.shape[1], count=1, dtype='float32', nodata='nan', crs=mosaic.crs, transform=mosaic.transform,)
        new_dataset.write(monthly_mean, 1)
        new_dataset.close()
        
        print("--- COG Generated! ---")
        
        del monthly_mean, new_dataset, mosaic
    
    mean_mar(ts1, ts2, ts3, ts4)
    
    def upload_mar():
    
        print("--- Beginning Upload ---")
        
        # Upload monthly mean COG to the corresponding folder on the AWS s3 bucket
        object_name = uploadprefix + os.path.basename(output_month)
        formdev.upload_file(output_month, object_name)
        
        print("--- Upload Complete ---")
    
    upload_mar()
    
    print("--- March Done ---")
    
# Define April parameters    
def apr_reg(workdir, attribute, year):

    # Let's use Amazon S3
    s3 = boto3.resource('s3')
    print("[INFO:] Connecting to cloud")

    formdev = s3.Bucket('formulations-dev')

    print("--- Beginning April ---")
    
    month = 'APR'
    
    # timestep constants
    ts1 = '097'
    ts2 = '105'
    ts3 = '113'
        
    # final upload prefix
    uploadprefix = 'spatial-grids/GLASS/' + attribute + '_monthlymean/'

    output_month = workdir + attribute + '_' + year + '_' + month + '.tif'
    
    # Define April Download
    def download_apr(timestep):
        prefix = 'spatial-grids/GLASS/' + attribute + '_mosaic/' + attribute + '_' + year + '_' + timestep
        objects = formdev.objects.filter(Prefix=prefix)
        for obj in objects:
            path, filename = os.path.split(obj.key)        
            formdev.download_file(obj.key, filename)
    
    print("--- Beginning Download ---")
    
    # Download April COGs by corresponding timestep
    download_apr(ts1)
    download_apr(ts2)
    download_apr(ts3)
        
    # Average tifs and save output as Cloud-optimized Geotiff
    def mean_apr(tif1, tif2, tif3):
        print("--- Beginning Raster Algebra ---")
        
        # Open corresponding tifs in Rasterio and convert to 2D arrays
        fp = workdir + attribute + '_' + year + '_' + tif1 + '.tif'
        mosaic = rio.open(fp)
        file1 = mosaic.read(1, masked=True)
        file1_array = np.array(file1, dtype='float64')
        del fp, mosaic, file1
        
        fp = workdir + attribute + '_' + year + '_' + tif2 + '.tif'
        mosaic = rio.open(fp)
        file2 = mosaic.read(1, masked=True)
        file2_array = np.array(file2, dtype='float64')
        del fp, mosaic, file2
        
        fp = workdir + attribute + '_' + year + '_' + tif3 + '.tif'
        mosaic = rio.open(fp)
        file3 = mosaic.read(1, masked=True)
        file3_array = np.array(file3, dtype='float64')
        del fp, file3
        
        # Create 3D Array of 2D arrays
        array3d = [file1_array, file2_array, file3_array]    
        del file1_array, file2_array, file3_array
        
        # monthly mean calculation
        monthly_mean1 = np.mean(array3d, axis=0)
        monthly_mean = np.where(monthly_mean1<0, np.nan, monthly_mean1)
        del array3d, monthly_mean1
        
        print("--- Calculation Complete! ---")
        
        print("--- Generating COG ---")
        
        # Write array as new COG
        new_dataset =  rio.open(output_month,'w', driver='COG', height=mosaic.shape[0], width=mosaic.shape[1], count=1, dtype='float32', nodata='nan', crs=mosaic.crs, transform=mosaic.transform,)
        new_dataset.write(monthly_mean, 1)
        new_dataset.close()
        
        print("--- COG Generated! ---")
        
        del monthly_mean, new_dataset, mosaic
    
    mean_apr(ts1, ts2, ts3)
    
    def upload_apr():
    
        print("--- Beginning Upload ---")
        
        # Upload monthly mean COG to the corresponding folder on the AWS s3 bucket
        object_name = uploadprefix + os.path.basename(output_month)
        formdev.upload_file(output_month, object_name)
        
        print("--- Upload Complete ---")
    
    upload_apr()
    
    print("--- April Done ---")
    
# Define April parameters (leap year)    
def apr_leap(workdir, attribute, year):

    # Let's use Amazon S3
    s3 = boto3.resource('s3')
    print("[INFO:] Connecting to cloud")

    formdev = s3.Bucket('formulations-dev')

    print("--- Beginning April ---")
    
    month = 'APR'
    
    # timestep constants
    ts1 = '097'
    ts2 = '105'
    ts3 = '113'
    ts4 = '121'
    
    # final upload prefix
    uploadprefix = 'spatial-grids/GLASS/' + attribute + '_monthlymean/'

    output_month = workdir + attribute + '_' + year + '_' + month + '.tif'
    
    # Define April Download
    def download_apr_leap(timestep):
        prefix = 'spatial-grids/GLASS/' + attribute + '_mosaic/' + attribute + '_' + year + '_' + timestep
        objects = formdev.objects.filter(Prefix=prefix)
        for obj in objects:
            path, filename = os.path.split(obj.key)        
            formdev.download_file(obj.key, filename)
    
    print("--- Beginning Download ---")
    
    # Download April COGs by corresponding timestep
    download_apr_leap(ts1)
    download_apr_leap(ts2)
    download_apr_leap(ts3)
    download_apr_leap(ts4)

    
    # Average tifs and save output as Cloud-optimized Geotiff
    def mean_apr_leap(tif1, tif2, tif3, tif4):
        print("--- Beginning Raster Algebra ---")
        
        # Open corresponding tifs in Rasterio and convert to 2D arrays
        fp = workdir + attribute + '_' + year + '_' + tif1 + '.tif'
        mosaic = rio.open(fp)
        file1 = mosaic.read(1, masked=True)
        file1_array = np.array(file1, dtype='float64')
        del fp, mosaic, file1
        
        fp = workdir + attribute + '_' + year + '_' + tif2 + '.tif'
        mosaic = rio.open(fp)
        file2 = mosaic.read(1, masked=True)
        file2_array = np.array(file2, dtype='float64')
        del fp, mosaic, file2
        
        fp = workdir + attribute + '_' + year + '_' + tif3 + '.tif'
        mosaic = rio.open(fp)
        file3 = mosaic.read(1, masked=True)
        file3_array = np.array(file3, dtype='float64')
        del fp, mosaic, file3
        
        fp = workdir + attribute + '_' + year + '_' + tif4 + '.tif'
        mosaic = rio.open(fp)
        file4 = mosaic.read(1, masked=True)
        file4_array = np.array(file4, dtype='float64')
        del fp, file4
        
        # Create 3D Array of 2D arrays
        array3d = [file1_array, file2_array, file3_array, file4_array]    
        del file1_array, file2_array, file3_array, file4_array
        
        # monthly mean calculation
        monthly_mean1 = np.mean(array3d, axis=0)
        monthly_mean = np.where(monthly_mean1<0, np.nan, monthly_mean1)
        del array3d, monthly_mean1
        
        print("--- Calculation Complete! ---")
        
        print("--- Generating COG ---")
        
        # Write array as new COG
        new_dataset =  rio.open(output_month,'w', driver='COG', height=mosaic.shape[0], width=mosaic.shape[1], count=1, dtype='float32', nodata='nan', crs=mosaic.crs, transform=mosaic.transform,)
        new_dataset.write(monthly_mean, 1)
        new_dataset.close()
        
        print("--- COG Generated! ---")
        
        del monthly_mean, new_dataset, mosaic
    
    mean_apr_leap(ts1, ts2, ts3, ts4)
    
    def upload_apr_leap():
    
        print("--- Beginning Upload ---")
        
        # Upload monthly mean COG to the corresponding folder on the AWS s3 bucket
        object_name = uploadprefix + os.path.basename(output_month)
        formdev.upload_file(output_month, object_name)
        
        print("--- Upload Complete ---")
    
    upload_apr_leap()
    
    print("--- April Done ---")
    
# Define May parameters    
def may_reg(workdir, attribute, year):

    # Let's use Amazon S3
    s3 = boto3.resource('s3')
    print("[INFO:] Connecting to cloud")

    formdev = s3.Bucket('formulations-dev')

    print("--- Beginning May ---")
    
    month = 'MAY'
    
    # timestep constants
    ts1 = '121'
    ts2 = '129'
    ts3 = '137'
    ts4 = '145'
    
    # final upload prefix
    uploadprefix = 'spatial-grids/GLASS/' + attribute + '_monthlymean/'

    output_month = workdir + attribute + '_' + year + '_' + month + '.tif'
    
    # Define May Download
    def download_may(timestep):
        prefix = 'spatial-grids/GLASS/' + attribute + '_mosaic/' + attribute + '_' + year + '_' + timestep
        objects = formdev.objects.filter(Prefix=prefix)
        for obj in objects:
            path, filename = os.path.split(obj.key)        
            formdev.download_file(obj.key, filename)
    
    print("--- Beginning Download ---")
    
    # Download May COGs by corresponding timestep
    download_may(ts1)
    download_may(ts2)
    download_may(ts3)
    download_may(ts4)

    
    # Average tifs and save output as Cloud-optimized Geotiff
    def mean_may(tif1, tif2, tif3, tif4):
        print("--- Beginning Raster Algebra ---")
        
        # Open corresponding tifs in Rasterio and convert to 2D arrays
        fp = workdir + attribute + '_' + year + '_' + tif1 + '.tif'
        mosaic = rio.open(fp)
        file1 = mosaic.read(1, masked=True)
        file1_array = np.array(file1, dtype='float64')
        del fp, mosaic, file1
        
        fp = workdir + attribute + '_' + year + '_' + tif2 + '.tif'
        mosaic = rio.open(fp)
        file2 = mosaic.read(1, masked=True)
        file2_array = np.array(file2, dtype='float64')
        del fp, mosaic, file2
        
        fp = workdir + attribute + '_' + year + '_' + tif3 + '.tif'
        mosaic = rio.open(fp)
        file3 = mosaic.read(1, masked=True)
        file3_array = np.array(file3, dtype='float64')
        del fp, mosaic, file3
        
        fp = workdir + attribute + '_' + year + '_' + tif4 + '.tif'
        mosaic = rio.open(fp)
        file4 = mosaic.read(1, masked=True)
        file4_array = np.array(file4, dtype='float64')
        del fp, file4
        
        # Create 3D Array of 2D arrays
        array3d = [file1_array, file2_array, file3_array, file4_array]    
        del file1_array, file2_array, file3_array, file4_array
        
        # monthly mean calculation
        monthly_mean1 = np.mean(array3d, axis=0)
        monthly_mean = np.where(monthly_mean1<0, np.nan, monthly_mean1)
        del array3d, monthly_mean1
        
        print("--- Calculation Complete! ---")
        
        print("--- Generating COG ---")
        
        # Write array as new COG
        new_dataset =  rio.open(output_month,'w', driver='COG', height=mosaic.shape[0], width=mosaic.shape[1], count=1, dtype='float32', nodata='nan', crs=mosaic.crs, transform=mosaic.transform,)
        new_dataset.write(monthly_mean, 1)
        new_dataset.close()
        
        print("--- COG Generated! ---")
        
        del monthly_mean, new_dataset, mosaic
    
    mean_may(ts1, ts2, ts3, ts4)
    
    def upload_may():
    
        print("--- Beginning Upload ---")
        
        # Upload monthly mean COG to the corresponding folder on the AWS s3 bucket
        object_name = uploadprefix + os.path.basename(output_month)
        formdev.upload_file(output_month, object_name)
        
        print("--- Upload Complete ---")
    
    upload_may()
    
    print("--- May Done ---")

# Define May parameters (leap year)    
def may_leap(workdir, attribute, year):

    # Let's use Amazon S3
    s3 = boto3.resource('s3')
    print("[INFO:] Connecting to cloud")

    formdev = s3.Bucket('formulations-dev')

    print("--- Beginning May ---")
    
    month = 'MAY'
    
    # timestep constants
    ts1 = '129'
    ts2 = '137'
    ts3 = '145'
    
    # final upload prefix
    uploadprefix = 'spatial-grids/GLASS/' + attribute + '_monthlymean/'

    output_month = workdir + attribute + '_' + year + '_' + month + '.tif'
    
    # Define May Download
    def download_may_leap(timestep):
        prefix = 'spatial-grids/GLASS/' + attribute + '_mosaic/' + attribute + '_' + year + '_' + timestep
        objects = formdev.objects.filter(Prefix=prefix)
        for obj in objects:
            path, filename = os.path.split(obj.key)        
            formdev.download_file(obj.key, filename)
    
    print("--- Beginning Download ---")
    
    # Download May COGs by corresponding timestep
    download_may_leap(ts1)
    download_may_leap(ts2)
    download_may_leap(ts3)
        
    # Average tifs and save output as Cloud-optimized Geotiff
    def mean_may_leap(tif1, tif2, tif3):
        print("--- Beginning Raster Algebra ---")
        
        # Open corresponding tifs in Rasterio and convert to 2D arrays
        fp = workdir + attribute + '_' + year + '_' + tif1 + '.tif'
        mosaic = rio.open(fp)
        file1 = mosaic.read(1, masked=True)
        file1_array = np.array(file1, dtype='float64')
        del fp, mosaic, file1
        
        fp = workdir + attribute + '_' + year + '_' + tif2 + '.tif'
        mosaic = rio.open(fp)
        file2 = mosaic.read(1, masked=True)
        file2_array = np.array(file2, dtype='float64')
        del fp, mosaic, file2
        
        fp = workdir + attribute + '_' + year + '_' + tif3 + '.tif'
        mosaic = rio.open(fp)
        file3 = mosaic.read(1, masked=True)
        file3_array = np.array(file3, dtype='float64')
        del fp, file3
                
        # Create 3D Array of 2D arrays
        array3d = [file1_array, file2_array, file3_array]    
        del file1_array, file2_array, file3_array
        
        # monthly mean calculation
        monthly_mean1 = np.mean(array3d, axis=0)
        monthly_mean = np.where(monthly_mean1<0, np.nan, monthly_mean1)
        del array3d, monthly_mean1
        
        print("--- Calculation Complete! ---")
        
        print("--- Generating COG ---")
        
        # Write array as new COG
        new_dataset =  rio.open(output_month,'w', driver='COG', height=mosaic.shape[0], width=mosaic.shape[1], count=1, dtype='float32', nodata='nan', crs=mosaic.crs, transform=mosaic.transform,)
        new_dataset.write(monthly_mean, 1)
        new_dataset.close()
        
        print("--- COG Generated! ---")
        
        del monthly_mean, new_dataset, mosaic
    
    mean_may_leap(ts1, ts2, ts3)
    
    def upload_may_leap():
    
        print("--- Beginning Upload ---")
        
        # Upload monthly mean COG to the corresponding folder on the AWS s3 bucket
        object_name = uploadprefix + os.path.basename(output_month)
        formdev.upload_file(output_month, object_name)
        
        print("--- Upload Complete ---")
    
    upload_may_leap()
    
    print("--- May Done ---")
    
# Define June parameters    
def jun_reg(workdir, attribute, year):

    # Let's use Amazon S3
    s3 = boto3.resource('s3')
    print("[INFO:] Connecting to cloud")

    formdev = s3.Bucket('formulations-dev')

    print("--- Beginning June ---")
    
    month = 'JUN'
    
    # timestep constants
    ts1 = '153'
    ts2 = '161'
    ts3 = '169'
    ts4 = '177'
    
    # final upload prefix
    uploadprefix = 'spatial-grids/GLASS/' + attribute + '_monthlymean/'

    output_month = workdir + attribute + '_' + year + '_' + month + '.tif'
    
    # Define June Download
    def download_jun(timestep):
        prefix = 'spatial-grids/GLASS/' + attribute + '_mosaic/' + attribute + '_' + year + '_' + timestep
        objects = formdev.objects.filter(Prefix=prefix)
        for obj in objects:
            path, filename = os.path.split(obj.key)        
            formdev.download_file(obj.key, filename)
    
    print("--- Beginning Download ---")
    
    # Download June COGs by corresponding timestep
    download_jun(ts1)
    download_jun(ts2)
    download_jun(ts3)
    download_jun(ts4)

    
    # Average tifs and save output as Cloud-optimized Geotiff
    def mean_jun(tif1, tif2, tif3, tif4):
        print("--- Beginning Raster Algebra ---")
        
        # Open corresponding tifs in Rasterio and convert to 2D arrays
        fp = workdir + attribute + '_' + year + '_' + tif1 + '.tif'
        mosaic = rio.open(fp)
        file1 = mosaic.read(1, masked=True)
        file1_array = np.array(file1, dtype='float64')
        del fp, mosaic, file1
        
        fp = workdir + attribute + '_' + year + '_' + tif2 + '.tif'
        mosaic = rio.open(fp)
        file2 = mosaic.read(1, masked=True)
        file2_array = np.array(file2, dtype='float64')
        del fp, mosaic, file2
        
        fp = workdir + attribute + '_' + year + '_' + tif3 + '.tif'
        mosaic = rio.open(fp)
        file3 = mosaic.read(1, masked=True)
        file3_array = np.array(file3, dtype='float64')
        del fp, mosaic, file3
        
        fp = workdir + attribute + '_' + year + '_' + tif4 + '.tif'
        mosaic = rio.open(fp)
        file4 = mosaic.read(1, masked=True)
        file4_array = np.array(file4, dtype='float64')
        del fp, file4
        
        # Create 3D Array of 2D arrays
        array3d = [file1_array, file2_array, file3_array, file4_array]    
        del file1_array, file2_array, file3_array, file4_array
        
        # monthly mean calculation
        monthly_mean1 = np.mean(array3d, axis=0)
        monthly_mean = np.where(monthly_mean1<0, np.nan, monthly_mean1)
        del array3d, monthly_mean1
        
        print("--- Calculation Complete! ---")
        
        print("--- Generating COG ---")
        
        # Write array as new COG
        new_dataset =  rio.open(output_month,'w', driver='COG', height=mosaic.shape[0], width=mosaic.shape[1], count=1, dtype='float32', nodata='nan', crs=mosaic.crs, transform=mosaic.transform,)
        new_dataset.write(monthly_mean, 1)
        new_dataset.close()
        
        print("--- COG Generated! ---")
        
        del monthly_mean, new_dataset, mosaic
    
    mean_jun(ts1, ts2, ts3, ts4)
    
    def upload_jun():
    
        print("--- Beginning Upload ---")
        
        # Upload monthly mean COG to the corresponding folder on the AWS s3 bucket
        object_name = uploadprefix + os.path.basename(output_month)
        formdev.upload_file(output_month, object_name)
        
        print("--- Upload Complete ---")
    
    upload_jun()
    
    print("--- June Done ---")
    
# Define July parameters    
def jul_reg(workdir, attribute, year):

    # Let's use Amazon S3
    s3 = boto3.resource('s3')
    print("[INFO:] Connecting to cloud")

    formdev = s3.Bucket('formulations-dev')

    print("--- Beginning July ---")
    
    month = 'JUL'
    
    # timestep constants
    ts1 = '185'
    ts2 = '193'
    ts3 = '201'
    ts4 = '209'
    
    # final upload prefix
    uploadprefix = 'spatial-grids/GLASS/' + attribute + '_monthlymean/'

    output_month = workdir + attribute + '_' + year + '_' + month + '.tif'
    
    # Define July Download
    def download_jul(timestep):
        prefix = 'spatial-grids/GLASS/' + attribute + '_mosaic/' + attribute + '_' + year + '_' + timestep
        objects = formdev.objects.filter(Prefix=prefix)
        for obj in objects:
            path, filename = os.path.split(obj.key)        
            formdev.download_file(obj.key, filename)
    
    print("--- Beginning Download ---")
    
    # Download July COGs by corresponding timestep
    download_jul(ts1)
    download_jul(ts2)
    download_jul(ts3)
    download_jul(ts4)
    
    # Average tifs and save output as Cloud-optimized Geotiff
    def mean_jul(tif1, tif2, tif3, tif4):
        print("--- Beginning Raster Algebra ---")
        
        # Open corresponding tifs in Rasterio and convert to 2D arrays
        fp = workdir + attribute + '_' + year + '_' + tif1 + '.tif'
        mosaic = rio.open(fp)
        file1 = mosaic.read(1, masked=True)
        file1_array = np.array(file1, dtype='float64')
        del fp, mosaic, file1
        
        fp = workdir + attribute + '_' + year + '_' + tif2 + '.tif'
        mosaic = rio.open(fp)
        file2 = mosaic.read(1, masked=True)
        file2_array = np.array(file2, dtype='float64')
        del fp, mosaic, file2
        
        fp = workdir + attribute + '_' + year + '_' + tif3 + '.tif'
        mosaic = rio.open(fp)
        file3 = mosaic.read(1, masked=True)
        file3_array = np.array(file3, dtype='float64')
        del fp, mosaic, file3
        
        fp = workdir + attribute + '_' + year + '_' + tif4 + '.tif'
        mosaic = rio.open(fp)
        file4 = mosaic.read(1, masked=True)
        file4_array = np.array(file4, dtype='float64')
        del fp, file4
        
        # Create 3D Array of 2D arrays
        array3d = [file1_array, file2_array, file3_array, file4_array]    
        del file1_array, file2_array, file3_array, file4_array
        
        # monthly mean calculation
        monthly_mean1 = np.mean(array3d, axis=0)
        monthly_mean = np.where(monthly_mean1<0, np.nan, monthly_mean1)
        del array3d, monthly_mean1
        
        print("--- Calculation Complete! ---")
        
        print("--- Generating COG ---")
        
        # Write array as new COG
        new_dataset =  rio.open(output_month,'w', driver='COG', height=mosaic.shape[0], width=mosaic.shape[1], count=1, dtype='float32', nodata='nan', crs=mosaic.crs, transform=mosaic.transform,)
        new_dataset.write(monthly_mean, 1)
        new_dataset.close()
        
        print("--- COG Generated! ---")
        
        del monthly_mean, new_dataset, mosaic
    
    mean_jul(ts1, ts2, ts3, ts4)
    
    def upload_jul():
    
        print("--- Beginning Upload ---")
        
        # Upload monthly mean COG to the corresponding folder on the AWS s3 bucket
        object_name = uploadprefix + os.path.basename(output_month)
        formdev.upload_file(output_month, object_name)
        
        print("--- Upload Complete ---")
    
    upload_jul()
    
    print("--- July Done ---")
    
# Define August parameters    
def aug_reg(workdir, attribute, year):

    # Let's use Amazon S3
    s3 = boto3.resource('s3')
    print("[INFO:] Connecting to cloud")

    formdev = s3.Bucket('formulations-dev')

    print("--- Beginning August ---")
    
    month = 'AUG'
    
    # timestep constants
    ts1 = '217'
    ts2 = '225'
    ts3 = '233'
    ts4 = '241'
    
    # final upload prefix
    uploadprefix = 'spatial-grids/GLASS/' + attribute + '_monthlymean/'

    output_month = workdir + attribute + '_' + year + '_' + month + '.tif'
    
    # Define August Download
    def download_aug(timestep):
        prefix = 'spatial-grids/GLASS/' + attribute + '_mosaic/' + attribute + '_' + year + '_' + timestep
        objects = formdev.objects.filter(Prefix=prefix)
        for obj in objects:
            path, filename = os.path.split(obj.key)        
            formdev.download_file(obj.key, filename)
    
    print("--- Beginning Download ---")
    
    # Download August COGs by corresponding timestep
    download_aug(ts1)
    download_aug(ts2)
    download_aug(ts3)
    download_aug(ts4)

    
    # Average tifs and save output as Cloud-optimized Geotiff
    def mean_aug(tif1, tif2, tif3, tif4):
        print("--- Beginning Raster Algebra ---")
        
        # Open corresponding tifs in Rasterio and convert to 2D arrays
        fp = workdir + attribute + '_' + year + '_' + tif1 + '.tif'
        mosaic = rio.open(fp)
        file1 = mosaic.read(1, masked=True)
        file1_array = np.array(file1, dtype='float64')
        del fp, mosaic, file1
        
        fp = workdir + attribute + '_' + year + '_' + tif2 + '.tif'
        mosaic = rio.open(fp)
        file2 = mosaic.read(1, masked=True)
        file2_array = np.array(file2, dtype='float64')
        del fp, mosaic, file2
        
        fp = workdir + attribute + '_' + year + '_' + tif3 + '.tif'
        mosaic = rio.open(fp)
        file3 = mosaic.read(1, masked=True)
        file3_array = np.array(file3, dtype='float64')
        del fp, mosaic, file3
        
        fp = workdir + attribute + '_' + year + '_' + tif4 + '.tif'
        mosaic = rio.open(fp)
        file4 = mosaic.read(1, masked=True)
        file4_array = np.array(file4, dtype='float64')
        del fp, file4
        
        # Create 3D Array of 2D arrays
        array3d = [file1_array, file2_array, file3_array, file4_array]    
        del file1_array, file2_array, file3_array, file4_array
        
        # monthly mean calculation
        monthly_mean1 = np.mean(array3d, axis=0)
        monthly_mean = np.where(monthly_mean1<0, np.nan, monthly_mean1)
        del array3d, monthly_mean1
        
        print("--- Calculation Complete! ---")
        
        print("--- Generating COG ---")
        
        # Write array as new COG
        new_dataset =  rio.open(output_month,'w', driver='COG', height=mosaic.shape[0], width=mosaic.shape[1], count=1, dtype='float32', nodata='nan', crs=mosaic.crs, transform=mosaic.transform,)
        new_dataset.write(monthly_mean, 1)
        new_dataset.close()
        
        print("--- COG Generated! ---")
        
        del monthly_mean, new_dataset, mosaic
    
    mean_aug(ts1, ts2, ts3, ts4)
    
    def upload_aug():
    
        print("--- Beginning Upload ---")
        
        # Upload monthly mean COG to the corresponding folder on the AWS s3 bucket
        object_name = uploadprefix + os.path.basename(output_month)
        formdev.upload_file(output_month, object_name)
        
        print("--- Upload Complete ---")
    
    upload_aug()
    
    print("--- August Done ---")
    
# Define September parameters    
def sep_reg(workdir, attribute, year):

    # Let's use Amazon S3
    s3 = boto3.resource('s3')
    print("[INFO:] Connecting to cloud")

    formdev = s3.Bucket('formulations-dev')

    print("--- Beginning September ---")
    
    month = 'SEP'
    
    # timestep constants
    ts1 = '249'
    ts2 = '257'
    ts3 = '265'
    ts4 = '273'
    
    # final upload prefix
    uploadprefix = 'spatial-grids/GLASS/' + attribute + '_monthlymean/'

    output_month = workdir + attribute + '_' + year + '_' + month + '.tif'
    
    # Define September Download
    def download_sep(timestep):
        prefix = 'spatial-grids/GLASS/' + attribute + '_mosaic/' + attribute + '_' + year + '_' + timestep
        objects = formdev.objects.filter(Prefix=prefix)
        for obj in objects:
            path, filename = os.path.split(obj.key)        
            formdev.download_file(obj.key, filename)
    
    print("--- Beginning Download ---")
    
    # Download September COGs by corresponding timestep
    download_sep(ts1)
    download_sep(ts2)
    download_sep(ts3)
    download_sep(ts4)

    
    # Average tifs and save output as Cloud-optimized Geotiff
    def mean_sep(tif1, tif2, tif3, tif4):
        print("--- Beginning Raster Algebra ---")
        
        # Open corresponding tifs in Rasterio and convert to 2D arrays
        fp = workdir + attribute + '_' + year + '_' + tif1 + '.tif'
        mosaic = rio.open(fp)
        file1 = mosaic.read(1, masked=True)
        file1_array = np.array(file1, dtype='float64')
        del fp, mosaic, file1
        
        fp = workdir + attribute + '_' + year + '_' + tif2 + '.tif'
        mosaic = rio.open(fp)
        file2 = mosaic.read(1, masked=True)
        file2_array = np.array(file2, dtype='float64')
        del fp, mosaic, file2
        
        fp = workdir + attribute + '_' + year + '_' + tif3 + '.tif'
        mosaic = rio.open(fp)
        file3 = mosaic.read(1, masked=True)
        file3_array = np.array(file3, dtype='float64')
        del fp, mosaic, file3
        
        fp = workdir + attribute + '_' + year + '_' + tif4 + '.tif'
        mosaic = rio.open(fp)
        file4 = mosaic.read(1, masked=True)
        file4_array = np.array(file4, dtype='float64')
        del fp, file4
        
        # Create 3D Array of 2D arrays
        array3d = [file1_array, file2_array, file3_array, file4_array]    
        del file1_array, file2_array, file3_array, file4_array
        
        # monthly mean calculation
        monthly_mean1 = np.mean(array3d, axis=0)
        monthly_mean = np.where(monthly_mean1<0, np.nan, monthly_mean1)
        del array3d, monthly_mean1
        
        print("--- Calculation Complete! ---")
        
        print("--- Generating COG ---")
        
        # Write array as new COG
        new_dataset =  rio.open(output_month,'w', driver='COG', height=mosaic.shape[0], width=mosaic.shape[1], count=1, dtype='float32', nodata='nan', crs=mosaic.crs, transform=mosaic.transform,)
        new_dataset.write(monthly_mean, 1)
        new_dataset.close()
        
        print("--- COG Generated! ---")
        
        del monthly_mean, new_dataset, mosaic
    
    mean_sep(ts1, ts2, ts3, ts4)
    
    def upload_sep():
    
        print("--- Beginning Upload ---")
        
        # Upload monthly mean COG to the corresponding folder on the AWS s3 bucket
        object_name = uploadprefix + os.path.basename(output_month)
        formdev.upload_file(output_month, object_name)
        
        print("--- Upload Complete ---")
    
    upload_sep()
    
    print("--- September Done ---")
    
# Define October parameters    
def oct_reg(workdir, attribute, year):

    # Let's use Amazon S3
    s3 = boto3.resource('s3')
    print("[INFO:] Connecting to cloud")

    formdev = s3.Bucket('formulations-dev')

    print("--- Beginning October ---")
    
    month = 'OCT'
    
    # timestep constants
    ts1 = '281'
    ts2 = '289'
    ts3 = '297'
       
    # final upload prefix
    uploadprefix = 'spatial-grids/GLASS/' + attribute + '_monthlymean/'

    output_month = workdir + attribute + '_' + year + '_' + month + '.tif'
    
    # Define October Download
    def download_oct(timestep):
        prefix = 'spatial-grids/GLASS/' + attribute + '_mosaic/' + attribute + '_' + year + '_' + timestep
        objects = formdev.objects.filter(Prefix=prefix)
        for obj in objects:
            path, filename = os.path.split(obj.key)        
            formdev.download_file(obj.key, filename)
    
    print("--- Beginning Download ---")
    
    # Download October COGs by corresponding timestep
    download_oct(ts1)
    download_oct(ts2)
    download_oct(ts3)
        
    # Average tifs and save output as Cloud-optimized Geotiff
    def mean_oct(tif1, tif2, tif3):
        print("--- Beginning Raster Algebra ---")
        
        # Open corresponding tifs in Rasterio and convert to 2D arrays
        fp = workdir + attribute + '_' + year + '_' + tif1 + '.tif'
        mosaic = rio.open(fp)
        file1 = mosaic.read(1, masked=True)
        file1_array = np.array(file1, dtype='float64')
        del fp, mosaic, file1
        
        fp = workdir + attribute + '_' + year + '_' + tif2 + '.tif'
        mosaic = rio.open(fp)
        file2 = mosaic.read(1, masked=True)
        file2_array = np.array(file2, dtype='float64')
        del fp, mosaic, file2
        
        fp = workdir + attribute + '_' + year + '_' + tif3 + '.tif'
        mosaic = rio.open(fp)
        file3 = mosaic.read(1, masked=True)
        file3_array = np.array(file3, dtype='float64')
        del fp, file3
               
        # Create 3D Array of 2D arrays
        array3d = [file1_array, file2_array, file3_array]    
        del file1_array, file2_array, file3_array
        
        # monthly mean calculation
        monthly_mean1 = np.mean(array3d, axis=0)
        monthly_mean = np.where(monthly_mean1<0, np.nan, monthly_mean1)
        del array3d, monthly_mean1
        
        print("--- Calculation Complete! ---")
        
        print("--- Generating COG ---")
        
        # Write array as new COG
        new_dataset =  rio.open(output_month,'w', driver='COG', height=mosaic.shape[0], width=mosaic.shape[1], count=1, dtype='float32', nodata='nan', crs=mosaic.crs, transform=mosaic.transform,)
        new_dataset.write(monthly_mean, 1)
        new_dataset.close()
        
        print("--- COG Generated! ---")
        
        del monthly_mean, new_dataset, mosaic
    
    mean_oct(ts1, ts2, ts3)
    
    def upload_oct():
    
        print("--- Beginning Upload ---")
        
        # Upload monthly mean COG to the corresponding folder on the AWS s3 bucket
        object_name = uploadprefix + os.path.basename(output_month)
        formdev.upload_file(output_month, object_name)
        
        print("--- Upload Complete ---")
    
    upload_oct()
    
    print("--- October Done ---")
    
# Define October parameters (leap year)    
def oct_leap(workdir, attribute, year):

    # Let's use Amazon S3
    s3 = boto3.resource('s3')
    print("[INFO:] Connecting to cloud")

    formdev = s3.Bucket('formulations-dev')

    print("--- Beginning October ---")
    
    month = 'OCT'
    
    # timestep constants
    ts1 = '281'
    ts2 = '289'
    ts3 = '297'
    ts4 = '305'
    
    # final upload prefix
    uploadprefix = 'spatial-grids/GLASS/' + attribute + '_monthlymean/'

    output_month = workdir + attribute + '_' + year + '_' + month + '.tif'
    
    # Define October Download
    def download_oct_leap(timestep):
        prefix = 'spatial-grids/GLASS/' + attribute + '_mosaic/' + attribute + '_' + year + '_' + timestep
        objects = formdev.objects.filter(Prefix=prefix)
        for obj in objects:
            path, filename = os.path.split(obj.key)        
            formdev.download_file(obj.key, filename)
    
    print("--- Beginning Download ---")
    
    # Download October COGs by corresponding timestep
    download_oct_leap(ts1)
    download_oct_leap(ts2)
    download_oct_leap(ts3)
    download_oct_leap(ts4)

    
    # Average tifs and save output as Cloud-optimized Geotiff
    def mean_oct_leap(tif1, tif2, tif3, tif4):
        print("--- Beginning Raster Algebra ---")
        
        # Open corresponding tifs in Rasterio and convert to 2D arrays
        fp = workdir + attribute + '_' + year + '_' + tif1 + '.tif'
        mosaic = rio.open(fp)
        file1 = mosaic.read(1, masked=True)
        file1_array = np.array(file1, dtype='float64')
        del fp, mosaic, file1
        
        fp = workdir + attribute + '_' + year + '_' + tif2 + '.tif'
        mosaic = rio.open(fp)
        file2 = mosaic.read(1, masked=True)
        file2_array = np.array(file2, dtype='float64')
        del fp, mosaic, file2
        
        fp = workdir + attribute + '_' + year + '_' + tif3 + '.tif'
        mosaic = rio.open(fp)
        file3 = mosaic.read(1, masked=True)
        file3_array = np.array(file3, dtype='float64')
        del fp, mosaic, file3
        
        fp = workdir + attribute + '_' + year + '_' + tif4 + '.tif'
        mosaic = rio.open(fp)
        file4 = mosaic.read(1, masked=True)
        file4_array = np.array(file4, dtype='float64')
        del fp, file4
        
        # Create 3D Array of 2D arrays
        array3d = [file1_array, file2_array, file3_array, file4_array]    
        del file1_array, file2_array, file3_array, file4_array
        
        # monthly mean calculation
        monthly_mean1 = np.mean(array3d, axis=0)
        monthly_mean = np.where(monthly_mean1<0, np.nan, monthly_mean1)
        del array3d, monthly_mean1
        
        print("--- Calculation Complete! ---")
        
        print("--- Generating COG ---")
        
        # Write array as new COG
        new_dataset =  rio.open(output_month,'w', driver='COG', height=mosaic.shape[0], width=mosaic.shape[1], count=1, dtype='float32', nodata='nan', crs=mosaic.crs, transform=mosaic.transform,)
        new_dataset.write(monthly_mean, 1)
        new_dataset.close()
        
        print("--- COG Generated! ---")
        
        del monthly_mean, new_dataset, mosaic
    
    mean_oct_leap(ts1, ts2, ts3, ts4)
    
    def upload_oct_leap():
    
        print("--- Beginning Upload ---")
        
        # Upload monthly mean COG to the corresponding folder on the AWS s3 bucket
        object_name = uploadprefix + os.path.basename(output_month)
        formdev.upload_file(output_month, object_name)
        
        print("--- Upload Complete ---")
    
    upload_oct_leap()
    
    print("--- October Done ---")
    
# Define November parameters    
def nov_reg(workdir, attribute, year):

    # Let's use Amazon S3
    s3 = boto3.resource('s3')
    print("[INFO:] Connecting to cloud")

    formdev = s3.Bucket('formulations-dev')

    print("--- Beginning November ---")
    
    month = 'NOV'
    
    # timestep constants
    ts1 = '305'
    ts2 = '313'
    ts3 = '321'
    ts4 = '329'
    
    # final upload prefix
    uploadprefix = 'spatial-grids/GLASS/' + attribute + '_monthlymean/'

    output_month = workdir + attribute + '_' + year + '_' + month + '.tif'
    
    # Define November Download
    def download_nov(timestep):
        prefix = 'spatial-grids/GLASS/' + attribute + '_mosaic/' + attribute + '_' + year + '_' + timestep
        objects = formdev.objects.filter(Prefix=prefix)
        for obj in objects:
            path, filename = os.path.split(obj.key)        
            formdev.download_file(obj.key, filename)
    
    print("--- Beginning Download ---")
    
    # Download November COGs by corresponding timestep
    download_nov(ts1)
    download_nov(ts2)
    download_nov(ts3)
    download_nov(ts4)

    
    # Average tifs and save output as Cloud-optimized Geotiff
    def mean_nov(tif1, tif2, tif3, tif4):
        print("--- Beginning Raster Algebra ---")
        
        # Open corresponding tifs in Rasterio and convert to 2D arrays
        fp = workdir + attribute + '_' + year + '_' + tif1 + '.tif'
        mosaic = rio.open(fp)
        file1 = mosaic.read(1, masked=True)
        file1_array = np.array(file1, dtype='float64')
        del fp, mosaic, file1
        
        fp = workdir + attribute + '_' + year + '_' + tif2 + '.tif'
        mosaic = rio.open(fp)
        file2 = mosaic.read(1, masked=True)
        file2_array = np.array(file2, dtype='float64')
        del fp, mosaic, file2
        
        fp = workdir + attribute + '_' + year + '_' + tif3 + '.tif'
        mosaic = rio.open(fp)
        file3 = mosaic.read(1, masked=True)
        file3_array = np.array(file3, dtype='float64')
        del fp, mosaic, file3
        
        fp = workdir + attribute + '_' + year + '_' + tif4 + '.tif'
        mosaic = rio.open(fp)
        file4 = mosaic.read(1, masked=True)
        file4_array = np.array(file4, dtype='float64')
        del fp, file4
        
        # Create 3D Array of 2D arrays
        array3d = [file1_array, file2_array, file3_array, file4_array]    
        del file1_array, file2_array, file3_array, file4_array
        
        # monthly mean calculation
        monthly_mean1 = np.mean(array3d, axis=0)
        monthly_mean = np.where(monthly_mean1<0, np.nan, monthly_mean1)
        del array3d, monthly_mean1
        
        print("--- Calculation Complete! ---")
        
        print("--- Generating COG ---")
        
        # Write array as new COG
        new_dataset =  rio.open(output_month,'w', driver='COG', height=mosaic.shape[0], width=mosaic.shape[1], count=1, dtype='float32', nodata='nan', crs=mosaic.crs, transform=mosaic.transform,)
        new_dataset.write(monthly_mean, 1)
        new_dataset.close()
        
        print("--- COG Generated! ---")
        
        del monthly_mean, new_dataset, mosaic
    
    mean_nov(ts1, ts2, ts3, ts4)
    
    def upload_nov():
    
        print("--- Beginning Upload ---")
        
        # Upload monthly mean COG to the corresponding folder on the AWS s3 bucket
        object_name = uploadprefix + os.path.basename(output_month)
        formdev.upload_file(output_month, object_name)
        
        print("--- Upload Complete ---")
    
    upload_nov()
    
    print("--- November Done ---")
    
# Define November parameters (leap year)    
def nov_leap(workdir, attribute, year):

    # Let's use Amazon S3
    s3 = boto3.resource('s3')
    print("[INFO:] Connecting to cloud")

    formdev = s3.Bucket('formulations-dev')

    print("--- Beginning November ---")
    
    month = 'NOV'
    
    # timestep constants
    ts1 = '313'
    ts2 = '321'
    ts3 = '329'
       
    # final upload prefix
    uploadprefix = 'spatial-grids/GLASS/' + attribute + '_monthlymean/'

    output_month = workdir + attribute + '_' + year + '_' + month + '.tif'
    
    # Define November Download
    def download_nov_leap(timestep):
        prefix = 'spatial-grids/GLASS/' + attribute + '_mosaic/' + attribute + '_' + year + '_' + timestep
        objects = formdev.objects.filter(Prefix=prefix)
        for obj in objects:
            path, filename = os.path.split(obj.key)        
            formdev.download_file(obj.key, filename)
    
    print("--- Beginning Download ---")
    
    # Download November COGs by corresponding timestep
    download_nov_leap(ts1)
    download_nov_leap(ts2)
    download_nov_leap(ts3)
        
    # Average tifs and save output as Cloud-optimized Geotiff
    def mean_nov_leap(tif1, tif2, tif3):
        print("--- Beginning Raster Algebra ---")
        
        # Open corresponding tifs in Rasterio and convert to 2D arrays
        fp = workdir + attribute + '_' + year + '_' + tif1 + '.tif'
        mosaic = rio.open(fp)
        file1 = mosaic.read(1, masked=True)
        file1_array = np.array(file1, dtype='float64')
        del fp, mosaic, file1
        
        fp = workdir + attribute + '_' + year + '_' + tif2 + '.tif'
        mosaic = rio.open(fp)
        file2 = mosaic.read(1, masked=True)
        file2_array = np.array(file2, dtype='float64')
        del fp, mosaic, file2
        
        fp = workdir + attribute + '_' + year + '_' + tif3 + '.tif'
        mosaic = rio.open(fp)
        file3 = mosaic.read(1, masked=True)
        file3_array = np.array(file3, dtype='float64')
        del fp, file3
               
        # Create 3D Array of 2D arrays
        array3d = [file1_array, file2_array, file3_array]    
        del file1_array, file2_array, file3_array
        
        # monthly mean calculation
        monthly_mean1 = np.mean(array3d, axis=0)
        monthly_mean = np.where(monthly_mean1<0, np.nan, monthly_mean1)
        del array3d, monthly_mean1
        
        print("--- Calculation Complete! ---")
        
        print("--- Generating COG ---")
        
        # Write array as new COG
        new_dataset =  rio.open(output_month,'w', driver='COG', height=mosaic.shape[0], width=mosaic.shape[1], count=1, dtype='float32', nodata='nan', crs=mosaic.crs, transform=mosaic.transform,)
        new_dataset.write(monthly_mean, 1)
        new_dataset.close()
        
        print("--- COG Generated! ---")
        
        del monthly_mean, new_dataset, mosaic
    
    mean_nov_leap(ts1, ts2, ts3)
    
    def upload_nov_leap():
    
        print("--- Beginning Upload ---")
        
        # Upload monthly mean COG to the corresponding folder on the AWS s3 bucket
        object_name = uploadprefix + os.path.basename(output_month)
        formdev.upload_file(output_month, object_name)
        
        print("--- Upload Complete ---")
    
    upload_nov_leap()
    
    print("--- November Done ---")
    
# Define December parameters    
def dec_reg(workdir, attribute, year):

    # Let's use Amazon S3
    s3 = boto3.resource('s3')
    print("[INFO:] Connecting to cloud")

    formdev = s3.Bucket('formulations-dev')

    print("--- Beginning December ---")
    
    month = 'DEC'
    
    # timestep constants
    ts1 = '337'
    ts2 = '345'
    ts3 = '353'
    ts4 = '361'
    
    # final upload prefix
    uploadprefix = 'spatial-grids/GLASS/' + attribute + '_monthlymean/'

    output_month = workdir + attribute + '_' + year + '_' + month + '.tif'
    
    # Define December Download
    def download_dec(timestep):
        prefix = 'spatial-grids/GLASS/' + attribute + '_mosaic/' + attribute + '_' + year + '_' + timestep
        objects = formdev.objects.filter(Prefix=prefix)
        for obj in objects:
            path, filename = os.path.split(obj.key)        
            formdev.download_file(obj.key, filename)
    
    print("--- Beginning Download ---")
    
    # Download December COGs by corresponding timestep
    download_dec(ts1)
    download_dec(ts2)
    download_dec(ts3)
    download_dec(ts4)

    
    # Average tifs and save output as Cloud-optimized Geotiff
    def mean_dec(tif1, tif2, tif3, tif4):
        print("--- Beginning Raster Algebra ---")
        
        # Open corresponding tifs in Rasterio and convert to 2D arrays
        fp = workdir + attribute + '_' + year + '_' + tif1 + '.tif'
        mosaic = rio.open(fp)
        file1 = mosaic.read(1, masked=True)
        file1_array = np.array(file1, dtype='float64')
        del fp, mosaic, file1
        
        fp = workdir + attribute + '_' + year + '_' + tif2 + '.tif'
        mosaic = rio.open(fp)
        file2 = mosaic.read(1, masked=True)
        file2_array = np.array(file2, dtype='float64')
        del fp, mosaic, file2
        
        fp = workdir + attribute + '_' + year + '_' + tif3 + '.tif'
        mosaic = rio.open(fp)
        file3 = mosaic.read(1, masked=True)
        file3_array = np.array(file3, dtype='float64')
        del fp, mosaic, file3
        
        fp = workdir + attribute + '_' + year + '_' + tif4 + '.tif'
        mosaic = rio.open(fp)
        file4 = mosaic.read(1, masked=True)
        file4_array = np.array(file4, dtype='float64')
        del fp, file4
        
        # Create 3D Array of 2D arrays
        array3d = [file1_array, file2_array, file3_array, file4_array]    
        del file1_array, file2_array, file3_array, file4_array
        
        # monthly mean calculation
        monthly_mean1 = np.mean(array3d, axis=0)
        monthly_mean = np.where(monthly_mean1<0, np.nan, monthly_mean1)
        del array3d, monthly_mean1
        
        print("--- Calculation Complete! ---")
        
        print("--- Generating COG ---")
        
        # Write array as new COG
        new_dataset =  rio.open(output_month,'w', driver='COG', height=mosaic.shape[0], width=mosaic.shape[1], count=1, dtype='float32', nodata='nan', crs=mosaic.crs, transform=mosaic.transform,)
        new_dataset.write(monthly_mean, 1)
        new_dataset.close()
        
        print("--- COG Generated! ---")
        
        del monthly_mean, new_dataset, mosaic
    
    mean_dec(ts1, ts2, ts3, ts4)
    
    def upload_dec():
    
        print("--- Beginning Upload ---")
        
        # Upload monthly mean COG to the corresponding folder on the AWS s3 bucket
        object_name = uploadprefix + os.path.basename(output_month)
        formdev.upload_file(output_month, object_name)
        
        print("--- Upload Complete ---")
    
    upload_dec()
    
    print("--- December Done ---")