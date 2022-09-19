# notes: This script can/should be cleaned up before wide distribution
# Make sure to change year (line 15), attribute (line 16), and wd (line 19) variables before running script
# Author: Rich Gibbs, NOAA, NWS, Office of Water Prediction, National Water Center

import boto3
import osgeo.gdal as gdal
import numpy as np
import matplotlib.pyplot as plt
import os, glob
import subprocess

# AWS config/credentials file
os.environ['AWS_PROFILE'] = "lynker_aws"

def mosaic_tif(workdir, attribute, year, timestep):
    print("--- Beginning " + timestep + " ---")
     
    output_mosaic = workdir + attribute + '_' + year + '_' + timestep + '.tif'
     
    # Define download parameters
    def download_tiles():
        # prefix to be changed per timestamp
        prefix = 'spatial-grids/GLASS/' + attribute + '_raw/' + attribute + '_' + year + '_' + timestep
              
        # Let's use Amazon S3
        s3 = boto3.resource('s3')
        print("[INFO:] Connecting to cloud")
               
        formdev = s3.Bucket('formulations-dev')
        
        print("--- Filelist from AWS: ---")
        # S3 list all keys with the prefix 'spatial-grids/GLASS/' + attribute + '_raw/'
        for formdev in s3.buckets.all():
            for obj in formdev.objects.filter(Prefix=prefix):
                print('{0}:{1}'.format(formdev.name, obj.key))
        
        print("--- Beginning Download ---")

        formdev = s3.Bucket('formulations-dev')        
        objects = formdev.objects.filter(Prefix=prefix)
        for obj in objects:
            path, filename = os.path.split(obj.key)        
            formdev.download_file(obj.key, filename)
        
        print("--- Download Complete! ---")
        
    download_tiles()
    
    # Mosaic rasters and save output as Cloud-optimized Geotiff
    print("--- Beginning Mosaic ---")
    def mosaic_rasters():
        files_to_mosaic=glob.glob(workdir + '*.tif')
        files_to_mosaic

        gdal.Warp(output_mosaic, files_to_mosaic, format="COG", options="-overwrite -multi -wm 80% -t_srs EPSG:5070 -co TILED=YES -co BIGTIFF=YES -co COMPRESS=DEFLATE -co NUM_THREADS=ALL_CPUS")
        print("--- Mosaic Created! ---")        
    mosaic_rasters()
    
    # upload mosaic to s3 bucket
    def upload_mosaic():
        print("--- Beginning Upload ---")
        
        # Let's use Amazon S3
        s3 = boto3.resource('s3')
        print("[INFO:] Connecting to cloud")
        
        uploadprefix = 'spatial-grids/GLASS/' + attribute + '_mosaic/'
        formdev = s3.Bucket('formulations-dev')
        object_name = uploadprefix + os.path.basename(output_mosaic)
        formdev.upload_file(output_mosaic, object_name)
        print("--- Upload Complete ---")
    upload_mosaic()
    print("--- " + timestep + " Complete! ---")    
    