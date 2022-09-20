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

# year and attributes that can be changed to download across years and attributes (LAI vs FVC)
year = #insert year(example: '2001')
attribute = #insert attribute/index (example: 'LAI' or 'FVC')

# working directory
wd = # insert working directory (example: 'C:/Users/username/Documents/workingdirectory/')

print("--- Beginning 001 ---")

# Let's use Amazon S3
s3 = boto3.resource('s3')
print("[INFO:] Connecting to cloud")

formdev = s3.Bucket('formulations-dev')

# prefix to be changed per timestamp
prefix = 'spatial-grids/GLASS/' + attribute + '_raw/' + attribute + '_' + year + '_001'

# final upload prefix
uploadprefix = 'spatial-grids/GLASS/' + attribute + '_mosaic/'

output_mosaic = wd + attribute + '_' + year + '_001.tif'

print("--- Filelist from AWS: ---")
# S3 list all keys with the prefix 'spatial-grids/GLASS/' + attribute + '_raw/'
for formdev in s3.buckets.all():
    for obj in formdev.objects.filter(Prefix=prefix):
        print('{0}:{1}'.format(formdev.name, obj.key))

# Download all objects in a bucket by given prefix (timestamp in this case)
print("--- Beginning Download ---")        
def download_timestamp():
    my_bucket = s3.Bucket('formulations-dev')
    objects = my_bucket.objects.filter(Prefix=prefix)
    for obj in objects:
        path, filename = os.path.split(obj.key)        
        my_bucket.download_file(obj.key, filename)     
download_timestamp()

print("--- Download Complete! ---")  

# Mosaic rasters and save output as Cloud-optimized Geotiff
print("--- Beginning Mosaic ---")
def mosaic_rasters():
    files_to_mosaic=glob.glob(wd+'*.tif')
    files_to_mosaic

    gdal.Warp(output_mosaic, files_to_mosaic, format="COG", options="-overwrite -multi -wm 80% -t_srs EPSG:5070 -co TILED=YES -co BIGTIFF=YES -co COMPRESS=DEFLATE -co NUM_THREADS=ALL_CPUS")
mosaic_rasters()
print("--- Rasters Mosaicked! ---")

#Upload mosaicked raster to the corresponding folder on the AWS s3 bucket
print("--- Beginning Upload ---")
def upload_mosaic():
    my_bucket = s3.Bucket('formulations-dev')
    object_name = uploadprefix + os.path.basename(output_mosaic)
    my_bucket.upload_file(output_mosaic, object_name)
upload_mosaic()
    
print("--- Upload Complete ---")

# Remove all .xml and .tif files
print("--- Cleaning Up Files ---")
cleandir = wd
files_in_directory = os.listdir(cleandir)
filtered_files = [file for file in files_in_directory if file.endswith(".tif")]
for file in filtered_files:
	path_to_file = os.path.join(cleandir, file)
	os.remove(path_to_file)
    
files_in_directory = os.listdir(cleandir)
filtered_files = [file for file in files_in_directory if file.endswith(".xml")]
for file in filtered_files:
	path_to_file = os.path.join(cleandir, file)
	os.remove(path_to_file)
    
print("--- 001 Done ---")
print("--- Beginning 009 ---")

# Let's use Amazon S3
s3 = boto3.resource('s3')
print("[INFO:] Connecting to cloud")

formdev = s3.Bucket('formulations-dev')

# prefix to be changed per timestamp
prefix = 'spatial-grids/GLASS/' + attribute + '_raw/' + attribute + '_' + year + '_009'

# final upload prefix
uploadprefix = 'spatial-grids/GLASS/' + attribute + '_mosaic/'

output_mosaic = wd + attribute + '_' + year + '_009.tif'

print("--- Filelist from AWS: ---")
# S3 list all keys with the prefix 'spatial-grids/GLASS/' + attribute + '_raw/'
for formdev in s3.buckets.all():
    for obj in formdev.objects.filter(Prefix=prefix):
        print('{0}:{1}'.format(formdev.name, obj.key))

# Download all objects in a bucket by given prefix (timestamp in this case)
print("--- Beginning Download ---")        
def download_timestamp():
    my_bucket = s3.Bucket('formulations-dev')
    objects = my_bucket.objects.filter(Prefix=prefix)
    for obj in objects:
        path, filename = os.path.split(obj.key)        
        my_bucket.download_file(obj.key, filename)     
download_timestamp()

print("--- Download Complete! ---")  

# Mosaic rasters and save output as Cloud-optimized Geotiff
print("--- Beginning Mosaic ---")
def mosaic_rasters():
    files_to_mosaic=glob.glob(wd+'*.tif')
    files_to_mosaic

    gdal.Warp(output_mosaic, files_to_mosaic, format="COG", options="-overwrite -multi -wm 80% -t_srs EPSG:5070 -co TILED=YES -co BIGTIFF=YES -co COMPRESS=DEFLATE -co NUM_THREADS=ALL_CPUS")
mosaic_rasters()
print("--- Rasters Mosaicked! ---")

#Upload mosaicked raster to the corresponding folder on the AWS s3 bucket
print("--- Beginning Upload ---")
def upload_mosaic():
    my_bucket = s3.Bucket('formulations-dev')
    object_name = uploadprefix + os.path.basename(output_mosaic)
    my_bucket.upload_file(output_mosaic, object_name)
upload_mosaic()
    
print("--- Upload Complete ---")

# Remove all .xml and .tif files
print("--- Cleaning Up Files ---")
cleandir = wd
files_in_directory = os.listdir(cleandir)
filtered_files = [file for file in files_in_directory if file.endswith(".tif")]
for file in filtered_files:
	path_to_file = os.path.join(cleandir, file)
	os.remove(path_to_file)
    
files_in_directory = os.listdir(cleandir)
filtered_files = [file for file in files_in_directory if file.endswith(".xml")]
for file in filtered_files:
	path_to_file = os.path.join(cleandir, file)
	os.remove(path_to_file)
    
print("--- 009 Done ---")

print("--- Beginning 017 ---")
# Let's use Amazon S3
s3 = boto3.resource('s3')
print("[INFO:] Connecting to cloud")

formdev = s3.Bucket('formulations-dev')

# prefix to be changed per timestamp
prefix = 'spatial-grids/GLASS/' + attribute + '_raw/' + attribute + '_' + year + '_017'

# final upload prefix
uploadprefix = 'spatial-grids/GLASS/' + attribute + '_mosaic/'

output_mosaic = wd + attribute + '_' + year + '_017.tif'

print("--- Filelist from AWS: ---")
# S3 list all keys with the prefix 'spatial-grids/GLASS/' + attribute + '_raw/'
for formdev in s3.buckets.all():
    for obj in formdev.objects.filter(Prefix=prefix):
        print('{0}:{1}'.format(formdev.name, obj.key))

# Download all objects in a bucket by given prefix (timestamp in this case)
print("--- Beginning Download ---")        
def download_timestamp():
    my_bucket = s3.Bucket('formulations-dev')
    objects = my_bucket.objects.filter(Prefix=prefix)
    for obj in objects:
        path, filename = os.path.split(obj.key)        
        my_bucket.download_file(obj.key, filename)     
download_timestamp()

print("--- Download Complete! ---")  

# Mosaic rasters and save output as Cloud-optimized Geotiff
print("--- Beginning Mosaic ---")
def mosaic_rasters():
    files_to_mosaic=glob.glob(wd+'*.tif')
    files_to_mosaic

    gdal.Warp(output_mosaic, files_to_mosaic, format="COG", options="-overwrite -multi -wm 80% -t_srs EPSG:5070 -co TILED=YES -co BIGTIFF=YES -co COMPRESS=DEFLATE -co NUM_THREADS=ALL_CPUS")
mosaic_rasters()
print("--- Rasters Mosaicked! ---")

#Upload mosaicked raster to the corresponding folder on the AWS s3 bucket
print("--- Beginning Upload ---")
def upload_mosaic():
    my_bucket = s3.Bucket('formulations-dev')
    object_name = uploadprefix + os.path.basename(output_mosaic)
    my_bucket.upload_file(output_mosaic, object_name)
upload_mosaic()
    
print("--- Upload Complete ---")

# Remove all .xml and .tif files
print("--- Cleaning Up Files ---")
cleandir = wd
files_in_directory = os.listdir(cleandir)
filtered_files = [file for file in files_in_directory if file.endswith(".tif")]
for file in filtered_files:
	path_to_file = os.path.join(cleandir, file)
	os.remove(path_to_file)
    
files_in_directory = os.listdir(cleandir)
filtered_files = [file for file in files_in_directory if file.endswith(".xml")]
for file in filtered_files:
	path_to_file = os.path.join(cleandir, file)
	os.remove(path_to_file)
    
print("--- 017 Done ---")

print("--- Beginning 025 ---")

# Let's use Amazon S3
s3 = boto3.resource('s3')
print("[INFO:] Connecting to cloud")

formdev = s3.Bucket('formulations-dev')

# prefix to be changed per timestamp
prefix = 'spatial-grids/GLASS/' + attribute + '_raw/' + attribute + '_' + year + '_025'

# final upload prefix
uploadprefix = 'spatial-grids/GLASS/' + attribute + '_mosaic/'

output_mosaic = wd + attribute + '_' + year + '_025.tif'

print("--- Filelist from AWS: ---")
# S3 list all keys with the prefix 'spatial-grids/GLASS/' + attribute + '_raw/'
for formdev in s3.buckets.all():
    for obj in formdev.objects.filter(Prefix=prefix):
        print('{0}:{1}'.format(formdev.name, obj.key))

# Download all objects in a bucket by given prefix (timestamp in this case)
print("--- Beginning Download ---")        
def download_timestamp():
    my_bucket = s3.Bucket('formulations-dev')
    objects = my_bucket.objects.filter(Prefix=prefix)
    for obj in objects:
        path, filename = os.path.split(obj.key)        
        my_bucket.download_file(obj.key, filename)     
download_timestamp()

print("--- Download Complete! ---")  

# Mosaic rasters and save output as Cloud-optimized Geotiff
print("--- Beginning Mosaic ---")
def mosaic_rasters():
    files_to_mosaic=glob.glob(wd+'*.tif')
    files_to_mosaic

    gdal.Warp(output_mosaic, files_to_mosaic, format="COG", options="-overwrite -multi -wm 80% -t_srs EPSG:5070 -co TILED=YES -co BIGTIFF=YES -co COMPRESS=DEFLATE -co NUM_THREADS=ALL_CPUS")
mosaic_rasters()
print("--- Rasters Mosaicked! ---")

#Upload mosaicked raster to the corresponding folder on the AWS s3 bucket
print("--- Beginning Upload ---")
def upload_mosaic():
    my_bucket = s3.Bucket('formulations-dev')
    object_name = uploadprefix + os.path.basename(output_mosaic)
    my_bucket.upload_file(output_mosaic, object_name)
upload_mosaic()
    
print("--- Upload Complete ---")

# Remove all .xml and .tif files
print("--- Cleaning Up Files ---")
cleandir = wd
files_in_directory = os.listdir(cleandir)
filtered_files = [file for file in files_in_directory if file.endswith(".tif")]
for file in filtered_files:
	path_to_file = os.path.join(cleandir, file)
	os.remove(path_to_file)
    
files_in_directory = os.listdir(cleandir)
filtered_files = [file for file in files_in_directory if file.endswith(".xml")]
for file in filtered_files:
	path_to_file = os.path.join(cleandir, file)
	os.remove(path_to_file)
    
print("--- 025 Done ---")

print("--- Beginning 033 ---")

# Let's use Amazon S3
s3 = boto3.resource('s3')
print("[INFO:] Connecting to cloud")

formdev = s3.Bucket('formulations-dev')

# prefix to be changed per timestamp
prefix = 'spatial-grids/GLASS/' + attribute + '_raw/' + attribute + '_' + year + '_033'

# final upload prefix
uploadprefix = 'spatial-grids/GLASS/' + attribute + '_mosaic/'

output_mosaic = wd + attribute + '_' + year + '_033.tif'

print("--- Filelist from AWS: ---")
# S3 list all keys with the prefix 'spatial-grids/GLASS/' + attribute + '_raw/'
for formdev in s3.buckets.all():
    for obj in formdev.objects.filter(Prefix=prefix):
        print('{0}:{1}'.format(formdev.name, obj.key))

# Download all objects in a bucket by given prefix (timestamp in this case)
print("--- Beginning Download ---")        
def download_timestamp():
    my_bucket = s3.Bucket('formulations-dev')
    objects = my_bucket.objects.filter(Prefix=prefix)
    for obj in objects:
        path, filename = os.path.split(obj.key)        
        my_bucket.download_file(obj.key, filename)     
download_timestamp()

print("--- Download Complete! ---")  

# Mosaic rasters and save output as Cloud-optimized Geotiff
print("--- Beginning Mosaic ---")
def mosaic_rasters():
    files_to_mosaic=glob.glob(wd+'*.tif')
    files_to_mosaic

    gdal.Warp(output_mosaic, files_to_mosaic, format="COG", options="-overwrite -multi -wm 80% -t_srs EPSG:5070 -co TILED=YES -co BIGTIFF=YES -co COMPRESS=DEFLATE -co NUM_THREADS=ALL_CPUS")
mosaic_rasters()
print("--- Rasters Mosaicked! ---")

#Upload mosaicked raster to the corresponding folder on the AWS s3 bucket
print("--- Beginning Upload ---")
def upload_mosaic():
    my_bucket = s3.Bucket('formulations-dev')
    object_name = uploadprefix + os.path.basename(output_mosaic)
    my_bucket.upload_file(output_mosaic, object_name)
upload_mosaic()
    
print("--- Upload Complete ---")

# Remove all .xml and .tif files
print("--- Cleaning Up Files ---")
cleandir = wd
files_in_directory = os.listdir(cleandir)
filtered_files = [file for file in files_in_directory if file.endswith(".tif")]
for file in filtered_files:
	path_to_file = os.path.join(cleandir, file)
	os.remove(path_to_file)
    
files_in_directory = os.listdir(cleandir)
filtered_files = [file for file in files_in_directory if file.endswith(".xml")]
for file in filtered_files:
	path_to_file = os.path.join(cleandir, file)
	os.remove(path_to_file)
    
print("--- 033 Done ---")

print("--- Beginning 041 ---")

# Let's use Amazon S3
s3 = boto3.resource('s3')
print("[INFO:] Connecting to cloud")

formdev = s3.Bucket('formulations-dev')

# prefix to be changed per timestamp
prefix = 'spatial-grids/GLASS/' + attribute + '_raw/' + attribute + '_' + year + '_041'

# final upload prefix
uploadprefix = 'spatial-grids/GLASS/' + attribute + '_mosaic/'

output_mosaic = wd + attribute + '_' + year + '_041.tif'

print("--- Filelist from AWS: ---")
# S3 list all keys with the prefix 'spatial-grids/GLASS/' + attribute + '_raw/'
for formdev in s3.buckets.all():
    for obj in formdev.objects.filter(Prefix=prefix):
        print('{0}:{1}'.format(formdev.name, obj.key))

# Download all objects in a bucket by given prefix (timestamp in this case)
print("--- Beginning Download ---")        
def download_timestamp():
    my_bucket = s3.Bucket('formulations-dev')
    objects = my_bucket.objects.filter(Prefix=prefix)
    for obj in objects:
        path, filename = os.path.split(obj.key)        
        my_bucket.download_file(obj.key, filename)     
download_timestamp()

print("--- Download Complete! ---")  

# Mosaic rasters and save output as Cloud-optimized Geotiff
print("--- Beginning Mosaic ---")
def mosaic_rasters():
    files_to_mosaic=glob.glob(wd+'*.tif')
    files_to_mosaic

    gdal.Warp(output_mosaic, files_to_mosaic, format="COG", options="-overwrite -multi -wm 80% -t_srs EPSG:5070 -co TILED=YES -co BIGTIFF=YES -co COMPRESS=DEFLATE -co NUM_THREADS=ALL_CPUS")
mosaic_rasters()
print("--- Rasters Mosaicked! ---")

#Upload mosaicked raster to the corresponding folder on the AWS s3 bucket
print("--- Beginning Upload ---")
def upload_mosaic():
    my_bucket = s3.Bucket('formulations-dev')
    object_name = uploadprefix + os.path.basename(output_mosaic)
    my_bucket.upload_file(output_mosaic, object_name)
upload_mosaic()
    
print("--- Upload Complete ---")

# Remove all .xml and .tif files
print("--- Cleaning Up Files ---")
cleandir = wd
files_in_directory = os.listdir(cleandir)
filtered_files = [file for file in files_in_directory if file.endswith(".tif")]
for file in filtered_files:
	path_to_file = os.path.join(cleandir, file)
	os.remove(path_to_file)
    
files_in_directory = os.listdir(cleandir)
filtered_files = [file for file in files_in_directory if file.endswith(".xml")]
for file in filtered_files:
	path_to_file = os.path.join(cleandir, file)
	os.remove(path_to_file)
    
print("--- 041 Done ---")

print("--- Beginning 049 ---")

# Let's use Amazon S3
s3 = boto3.resource('s3')
print("[INFO:] Connecting to cloud")

formdev = s3.Bucket('formulations-dev')

# prefix to be changed per timestamp
prefix = 'spatial-grids/GLASS/' + attribute + '_raw/' + attribute + '_' + year + '_049'

# final upload prefix
uploadprefix = 'spatial-grids/GLASS/' + attribute + '_mosaic/'

output_mosaic = wd + attribute + '_' + year + '_049.tif'

print("--- Filelist from AWS: ---")
# S3 list all keys with the prefix 'spatial-grids/GLASS/' + attribute + '_raw/'
for formdev in s3.buckets.all():
    for obj in formdev.objects.filter(Prefix=prefix):
        print('{0}:{1}'.format(formdev.name, obj.key))

# Download all objects in a bucket by given prefix (timestamp in this case)
print("--- Beginning Download ---")        
def download_timestamp():
    my_bucket = s3.Bucket('formulations-dev')
    objects = my_bucket.objects.filter(Prefix=prefix)
    for obj in objects:
        path, filename = os.path.split(obj.key)        
        my_bucket.download_file(obj.key, filename)     
download_timestamp()

print("--- Download Complete! ---")  

# Mosaic rasters and save output as Cloud-optimized Geotiff
print("--- Beginning Mosaic ---")
def mosaic_rasters():
    files_to_mosaic=glob.glob(wd+'*.tif')
    files_to_mosaic

    gdal.Warp(output_mosaic, files_to_mosaic, format="COG", options="-overwrite -multi -wm 80% -t_srs EPSG:5070 -co TILED=YES -co BIGTIFF=YES -co COMPRESS=DEFLATE -co NUM_THREADS=ALL_CPUS")
mosaic_rasters()
print("--- Rasters Mosaicked! ---")

#Upload mosaicked raster to the corresponding folder on the AWS s3 bucket
print("--- Beginning Upload ---")
def upload_mosaic():
    my_bucket = s3.Bucket('formulations-dev')
    object_name = uploadprefix + os.path.basename(output_mosaic)
    my_bucket.upload_file(output_mosaic, object_name)
upload_mosaic()
    
print("--- Upload Complete ---")

# Remove all .xml and .tif files
print("--- Cleaning Up Files ---")
cleandir = wd
files_in_directory = os.listdir(cleandir)
filtered_files = [file for file in files_in_directory if file.endswith(".tif")]
for file in filtered_files:
	path_to_file = os.path.join(cleandir, file)
	os.remove(path_to_file)
    
files_in_directory = os.listdir(cleandir)
filtered_files = [file for file in files_in_directory if file.endswith(".xml")]
for file in filtered_files:
	path_to_file = os.path.join(cleandir, file)
	os.remove(path_to_file)
    
print("--- 049 Done ---")

print("--- Beginning 057 ---")

# Let's use Amazon S3
s3 = boto3.resource('s3')
print("[INFO:] Connecting to cloud")

formdev = s3.Bucket('formulations-dev')

# prefix to be changed per timestamp
prefix = 'spatial-grids/GLASS/' + attribute + '_raw/' + attribute + '_' + year + '_057'

# final upload prefix
uploadprefix = 'spatial-grids/GLASS/' + attribute + '_mosaic/'

output_mosaic = wd + attribute + '_' + year + '_057.tif'

print("--- Filelist from AWS: ---")
# S3 list all keys with the prefix 'spatial-grids/GLASS/' + attribute + '_raw/'
for formdev in s3.buckets.all():
    for obj in formdev.objects.filter(Prefix=prefix):
        print('{0}:{1}'.format(formdev.name, obj.key))

# Download all objects in a bucket by given prefix (timestamp in this case)
print("--- Beginning Download ---")        
def download_timestamp():
    my_bucket = s3.Bucket('formulations-dev')
    objects = my_bucket.objects.filter(Prefix=prefix)
    for obj in objects:
        path, filename = os.path.split(obj.key)        
        my_bucket.download_file(obj.key, filename)     
download_timestamp()

print("--- Download Complete! ---")  

# Mosaic rasters and save output as Cloud-optimized Geotiff
print("--- Beginning Mosaic ---")
def mosaic_rasters():
    files_to_mosaic=glob.glob(wd+'*.tif')
    files_to_mosaic

    gdal.Warp(output_mosaic, files_to_mosaic, format="COG", options="-overwrite -multi -wm 80% -t_srs EPSG:5070 -co TILED=YES -co BIGTIFF=YES -co COMPRESS=DEFLATE -co NUM_THREADS=ALL_CPUS")
mosaic_rasters()
print("--- Rasters Mosaicked! ---")

#Upload mosaicked raster to the corresponding folder on the AWS s3 bucket
print("--- Beginning Upload ---")
def upload_mosaic():
    my_bucket = s3.Bucket('formulations-dev')
    object_name = uploadprefix + os.path.basename(output_mosaic)
    my_bucket.upload_file(output_mosaic, object_name)
upload_mosaic()
    
print("--- Upload Complete ---")

# Remove all .xml and .tif files
print("--- Cleaning Up Files ---")
cleandir = wd
files_in_directory = os.listdir(cleandir)
filtered_files = [file for file in files_in_directory if file.endswith(".tif")]
for file in filtered_files:
	path_to_file = os.path.join(cleandir, file)
	os.remove(path_to_file)
    
files_in_directory = os.listdir(cleandir)
filtered_files = [file for file in files_in_directory if file.endswith(".xml")]
for file in filtered_files:
	path_to_file = os.path.join(cleandir, file)
	os.remove(path_to_file)
    
print("--- 057 Done ---")

print("--- Beginning 065 ---")

# Let's use Amazon S3
s3 = boto3.resource('s3')
print("[INFO:] Connecting to cloud")

formdev = s3.Bucket('formulations-dev')

# prefix to be changed per timestamp
prefix = 'spatial-grids/GLASS/' + attribute + '_raw/' + attribute + '_' + year + '_065'

# final upload prefix
uploadprefix = 'spatial-grids/GLASS/' + attribute + '_mosaic/'

output_mosaic = wd + attribute + '_' + year + '_065.tif'

print("--- Filelist from AWS: ---")
# S3 list all keys with the prefix 'spatial-grids/GLASS/' + attribute + '_raw/'
for formdev in s3.buckets.all():
    for obj in formdev.objects.filter(Prefix=prefix):
        print('{0}:{1}'.format(formdev.name, obj.key))

# Download all objects in a bucket by given prefix (timestamp in this case)
print("--- Beginning Download ---")        
def download_timestamp():
    my_bucket = s3.Bucket('formulations-dev')
    objects = my_bucket.objects.filter(Prefix=prefix)
    for obj in objects:
        path, filename = os.path.split(obj.key)        
        my_bucket.download_file(obj.key, filename)     
download_timestamp()

print("--- Download Complete! ---")  

# Mosaic rasters and save output as Cloud-optimized Geotiff
print("--- Beginning Mosaic ---")
def mosaic_rasters():
    files_to_mosaic=glob.glob(wd+'*.tif')
    files_to_mosaic

    gdal.Warp(output_mosaic, files_to_mosaic, format="COG", options="-overwrite -multi -wm 80% -t_srs EPSG:5070 -co TILED=YES -co BIGTIFF=YES -co COMPRESS=DEFLATE -co NUM_THREADS=ALL_CPUS")
mosaic_rasters()
print("--- Rasters Mosaicked! ---")

#Upload mosaicked raster to the corresponding folder on the AWS s3 bucket
print("--- Beginning Upload ---")
def upload_mosaic():
    my_bucket = s3.Bucket('formulations-dev')
    object_name = uploadprefix + os.path.basename(output_mosaic)
    my_bucket.upload_file(output_mosaic, object_name)
upload_mosaic()
    
print("--- Upload Complete ---")

# Remove all .xml and .tif files
print("--- Cleaning Up Files ---")
cleandir = wd
files_in_directory = os.listdir(cleandir)
filtered_files = [file for file in files_in_directory if file.endswith(".tif")]
for file in filtered_files:
	path_to_file = os.path.join(cleandir, file)
	os.remove(path_to_file)
    
files_in_directory = os.listdir(cleandir)
filtered_files = [file for file in files_in_directory if file.endswith(".xml")]
for file in filtered_files:
	path_to_file = os.path.join(cleandir, file)
	os.remove(path_to_file)
    
print("--- 065 Done ---")

print("--- Beginning 073 ---")

# Let's use Amazon S3
s3 = boto3.resource('s3')
print("[INFO:] Connecting to cloud")

formdev = s3.Bucket('formulations-dev')

# prefix to be changed per timestamp
prefix = 'spatial-grids/GLASS/' + attribute + '_raw/' + attribute + '_' + year + '_073'

# final upload prefix
uploadprefix = 'spatial-grids/GLASS/' + attribute + '_mosaic/'

output_mosaic = wd + attribute + '_' + year + '_073.tif'

print("--- Filelist from AWS: ---")
# S3 list all keys with the prefix 'spatial-grids/GLASS/' + attribute + '_raw/'
for formdev in s3.buckets.all():
    for obj in formdev.objects.filter(Prefix=prefix):
        print('{0}:{1}'.format(formdev.name, obj.key))

# Download all objects in a bucket by given prefix (timestamp in this case)
print("--- Beginning Download ---")        
def download_timestamp():
    my_bucket = s3.Bucket('formulations-dev')
    objects = my_bucket.objects.filter(Prefix=prefix)
    for obj in objects:
        path, filename = os.path.split(obj.key)        
        my_bucket.download_file(obj.key, filename)     
download_timestamp()

print("--- Download Complete! ---")  

# Mosaic rasters and save output as Cloud-optimized Geotiff
print("--- Beginning Mosaic ---")
def mosaic_rasters():
    files_to_mosaic=glob.glob(wd+'*.tif')
    files_to_mosaic

    gdal.Warp(output_mosaic, files_to_mosaic, format="COG", options="-overwrite -multi -wm 80% -t_srs EPSG:5070 -co TILED=YES -co BIGTIFF=YES -co COMPRESS=DEFLATE -co NUM_THREADS=ALL_CPUS")
mosaic_rasters()
print("--- Rasters Mosaicked! ---")

#Upload mosaicked raster to the corresponding folder on the AWS s3 bucket
print("--- Beginning Upload ---")
def upload_mosaic():
    my_bucket = s3.Bucket('formulations-dev')
    object_name = uploadprefix + os.path.basename(output_mosaic)
    my_bucket.upload_file(output_mosaic, object_name)
upload_mosaic()
    
print("--- Upload Complete ---")

# Remove all .xml and .tif files
print("--- Cleaning Up Files ---")
cleandir = wd
files_in_directory = os.listdir(cleandir)
filtered_files = [file for file in files_in_directory if file.endswith(".tif")]
for file in filtered_files:
	path_to_file = os.path.join(cleandir, file)
	os.remove(path_to_file)
    
files_in_directory = os.listdir(cleandir)
filtered_files = [file for file in files_in_directory if file.endswith(".xml")]
for file in filtered_files:
	path_to_file = os.path.join(cleandir, file)
	os.remove(path_to_file)
    
print("--- 073 Done ---")

print("--- Beginning 081 ---")

# Let's use Amazon S3
s3 = boto3.resource('s3')
print("[INFO:] Connecting to cloud")

formdev = s3.Bucket('formulations-dev')

# prefix to be changed per timestamp
prefix = 'spatial-grids/GLASS/' + attribute + '_raw/' + attribute + '_' + year + '_081'

# final upload prefix
uploadprefix = 'spatial-grids/GLASS/' + attribute + '_mosaic/'

output_mosaic = wd + attribute + '_' + year + '_081.tif'

print("--- Filelist from AWS: ---")
# S3 list all keys with the prefix 'spatial-grids/GLASS/' + attribute + '_raw/'
for formdev in s3.buckets.all():
    for obj in formdev.objects.filter(Prefix=prefix):
        print('{0}:{1}'.format(formdev.name, obj.key))

# Download all objects in a bucket by given prefix (timestamp in this case)
print("--- Beginning Download ---")        
def download_timestamp():
    my_bucket = s3.Bucket('formulations-dev')
    objects = my_bucket.objects.filter(Prefix=prefix)
    for obj in objects:
        path, filename = os.path.split(obj.key)        
        my_bucket.download_file(obj.key, filename)     
download_timestamp()

print("--- Download Complete! ---")  

# Mosaic rasters and save output as Cloud-optimized Geotiff
print("--- Beginning Mosaic ---")
def mosaic_rasters():
    files_to_mosaic=glob.glob(wd+'*.tif')
    files_to_mosaic

    gdal.Warp(output_mosaic, files_to_mosaic, format="COG", options="-overwrite -multi -wm 80% -t_srs EPSG:5070 -co TILED=YES -co BIGTIFF=YES -co COMPRESS=DEFLATE -co NUM_THREADS=ALL_CPUS")
mosaic_rasters()
print("--- Rasters Mosaicked! ---")

#Upload mosaicked raster to the corresponding folder on the AWS s3 bucket
print("--- Beginning Upload ---")
def upload_mosaic():
    my_bucket = s3.Bucket('formulations-dev')
    object_name = uploadprefix + os.path.basename(output_mosaic)
    my_bucket.upload_file(output_mosaic, object_name)
upload_mosaic()
    
print("--- Upload Complete ---")

# Remove all .xml and .tif files
print("--- Cleaning Up Files ---")
cleandir = wd
files_in_directory = os.listdir(cleandir)
filtered_files = [file for file in files_in_directory if file.endswith(".tif")]
for file in filtered_files:
	path_to_file = os.path.join(cleandir, file)
	os.remove(path_to_file)
    
files_in_directory = os.listdir(cleandir)
filtered_files = [file for file in files_in_directory if file.endswith(".xml")]
for file in filtered_files:
	path_to_file = os.path.join(cleandir, file)
	os.remove(path_to_file)
    
print("--- 081 Done ---")

print("--- Beginning 089 ---")

# Let's use Amazon S3
s3 = boto3.resource('s3')
print("[INFO:] Connecting to cloud")

formdev = s3.Bucket('formulations-dev')

# prefix to be changed per timestamp
prefix = 'spatial-grids/GLASS/' + attribute + '_raw/' + attribute + '_' + year + '_089'

# final upload prefix
uploadprefix = 'spatial-grids/GLASS/' + attribute + '_mosaic/'

output_mosaic = wd + attribute + '_' + year + '_089.tif'

print("--- Filelist from AWS: ---")
# S3 list all keys with the prefix 'spatial-grids/GLASS/' + attribute + '_raw/'
for formdev in s3.buckets.all():
    for obj in formdev.objects.filter(Prefix=prefix):
        print('{0}:{1}'.format(formdev.name, obj.key))

# Download all objects in a bucket by given prefix (timestamp in this case)
print("--- Beginning Download ---")        
def download_timestamp():
    my_bucket = s3.Bucket('formulations-dev')
    objects = my_bucket.objects.filter(Prefix=prefix)
    for obj in objects:
        path, filename = os.path.split(obj.key)        
        my_bucket.download_file(obj.key, filename)     
download_timestamp()

print("--- Download Complete! ---")  

# Mosaic rasters and save output as Cloud-optimized Geotiff
print("--- Beginning Mosaic ---")
def mosaic_rasters():
    files_to_mosaic=glob.glob(wd+'*.tif')
    files_to_mosaic

    gdal.Warp(output_mosaic, files_to_mosaic, format="COG", options="-overwrite -multi -wm 80% -t_srs EPSG:5070 -co TILED=YES -co BIGTIFF=YES -co COMPRESS=DEFLATE -co NUM_THREADS=ALL_CPUS")
mosaic_rasters()
print("--- Rasters Mosaicked! ---")

#Upload mosaicked raster to the corresponding folder on the AWS s3 bucket
print("--- Beginning Upload ---")
def upload_mosaic():
    my_bucket = s3.Bucket('formulations-dev')
    object_name = uploadprefix + os.path.basename(output_mosaic)
    my_bucket.upload_file(output_mosaic, object_name)
upload_mosaic()
    
print("--- Upload Complete ---")

# Remove all .xml and .tif files
print("--- Cleaning Up Files ---")
cleandir = wd
files_in_directory = os.listdir(cleandir)
filtered_files = [file for file in files_in_directory if file.endswith(".tif")]
for file in filtered_files:
	path_to_file = os.path.join(cleandir, file)
	os.remove(path_to_file)
    
files_in_directory = os.listdir(cleandir)
filtered_files = [file for file in files_in_directory if file.endswith(".xml")]
for file in filtered_files:
	path_to_file = os.path.join(cleandir, file)
	os.remove(path_to_file)
    
print("--- 089 Done ---")

print("--- Beginning 097 ---")

# Let's use Amazon S3
s3 = boto3.resource('s3')
print("[INFO:] Connecting to cloud")

formdev = s3.Bucket('formulations-dev')

# prefix to be changed per timestamp
prefix = 'spatial-grids/GLASS/' + attribute + '_raw/' + attribute + '_' + year + '_097'

# final upload prefix
uploadprefix = 'spatial-grids/GLASS/' + attribute + '_mosaic/'

output_mosaic = wd + attribute + '_' + year + '_097.tif'

print("--- Filelist from AWS: ---")
# S3 list all keys with the prefix 'spatial-grids/GLASS/' + attribute + '_raw/'
for formdev in s3.buckets.all():
    for obj in formdev.objects.filter(Prefix=prefix):
        print('{0}:{1}'.format(formdev.name, obj.key))

# Download all objects in a bucket by given prefix (timestamp in this case)
print("--- Beginning Download ---")        
def download_timestamp():
    my_bucket = s3.Bucket('formulations-dev')
    objects = my_bucket.objects.filter(Prefix=prefix)
    for obj in objects:
        path, filename = os.path.split(obj.key)        
        my_bucket.download_file(obj.key, filename)     
download_timestamp()

print("--- Download Complete! ---")  

# Mosaic rasters and save output as Cloud-optimized Geotiff
print("--- Beginning Mosaic ---")
def mosaic_rasters():
    files_to_mosaic=glob.glob(wd+'*.tif')
    files_to_mosaic

    gdal.Warp(output_mosaic, files_to_mosaic, format="COG", options="-overwrite -multi -wm 80% -t_srs EPSG:5070 -co TILED=YES -co BIGTIFF=YES -co COMPRESS=DEFLATE -co NUM_THREADS=ALL_CPUS")
mosaic_rasters()
print("--- Rasters Mosaicked! ---")

#Upload mosaicked raster to the corresponding folder on the AWS s3 bucket
print("--- Beginning Upload ---")
def upload_mosaic():
    my_bucket = s3.Bucket('formulations-dev')
    object_name = uploadprefix + os.path.basename(output_mosaic)
    my_bucket.upload_file(output_mosaic, object_name)
upload_mosaic()
    
print("--- Upload Complete ---")

# Remove all .xml and .tif files
print("--- Cleaning Up Files ---")
cleandir = wd
files_in_directory = os.listdir(cleandir)
filtered_files = [file for file in files_in_directory if file.endswith(".tif")]
for file in filtered_files:
	path_to_file = os.path.join(cleandir, file)
	os.remove(path_to_file)
    
files_in_directory = os.listdir(cleandir)
filtered_files = [file for file in files_in_directory if file.endswith(".xml")]
for file in filtered_files:
	path_to_file = os.path.join(cleandir, file)
	os.remove(path_to_file)
    
print("--- 097 Done ---")

print("--- Beginning 105 ---")

# Let's use Amazon S3
s3 = boto3.resource('s3')
print("[INFO:] Connecting to cloud")

formdev = s3.Bucket('formulations-dev')

# prefix to be changed per timestamp
prefix = 'spatial-grids/GLASS/' + attribute + '_raw/' + attribute + '_' + year + '_105'

# final upload prefix
uploadprefix = 'spatial-grids/GLASS/' + attribute + '_mosaic/'

output_mosaic = wd + attribute + '_' + year + '_105.tif'

print("--- Filelist from AWS: ---")
# S3 list all keys with the prefix 'spatial-grids/GLASS/' + attribute + '_raw/'
for formdev in s3.buckets.all():
    for obj in formdev.objects.filter(Prefix=prefix):
        print('{0}:{1}'.format(formdev.name, obj.key))

# Download all objects in a bucket by given prefix (timestamp in this case)
print("--- Beginning Download ---")        
def download_timestamp():
    my_bucket = s3.Bucket('formulations-dev')
    objects = my_bucket.objects.filter(Prefix=prefix)
    for obj in objects:
        path, filename = os.path.split(obj.key)        
        my_bucket.download_file(obj.key, filename)     
download_timestamp()

print("--- Download Complete! ---")  

# Mosaic rasters and save output as Cloud-optimized Geotiff
print("--- Beginning Mosaic ---")
def mosaic_rasters():
    files_to_mosaic=glob.glob(wd+'*.tif')
    files_to_mosaic

    gdal.Warp(output_mosaic, files_to_mosaic, format="COG", options="-overwrite -multi -wm 80% -t_srs EPSG:5070 -co TILED=YES -co BIGTIFF=YES -co COMPRESS=DEFLATE -co NUM_THREADS=ALL_CPUS")
mosaic_rasters()
print("--- Rasters Mosaicked! ---")

#Upload mosaicked raster to the corresponding folder on the AWS s3 bucket
print("--- Beginning Upload ---")
def upload_mosaic():
    my_bucket = s3.Bucket('formulations-dev')
    object_name = uploadprefix + os.path.basename(output_mosaic)
    my_bucket.upload_file(output_mosaic, object_name)
upload_mosaic()
    
print("--- Upload Complete ---")

# Remove all .xml and .tif files
print("--- Cleaning Up Files ---")
cleandir = wd
files_in_directory = os.listdir(cleandir)
filtered_files = [file for file in files_in_directory if file.endswith(".tif")]
for file in filtered_files:
	path_to_file = os.path.join(cleandir, file)
	os.remove(path_to_file)
    
files_in_directory = os.listdir(cleandir)
filtered_files = [file for file in files_in_directory if file.endswith(".xml")]
for file in filtered_files:
	path_to_file = os.path.join(cleandir, file)
	os.remove(path_to_file)
    
print("--- 105 Done ---")

print("--- Beginning 113 ---")

# Let's use Amazon S3
s3 = boto3.resource('s3')
print("[INFO:] Connecting to cloud")

formdev = s3.Bucket('formulations-dev')

# prefix to be changed per timestamp
prefix = 'spatial-grids/GLASS/' + attribute + '_raw/' + attribute + '_' + year + '_113'

# final upload prefix
uploadprefix = 'spatial-grids/GLASS/' + attribute + '_mosaic/'

output_mosaic = wd + attribute + '_' + year + '_113.tif'

print("--- Filelist from AWS: ---")
# S3 list all keys with the prefix 'spatial-grids/GLASS/' + attribute + '_raw/'
for formdev in s3.buckets.all():
    for obj in formdev.objects.filter(Prefix=prefix):
        print('{0}:{1}'.format(formdev.name, obj.key))

# Download all objects in a bucket by given prefix (timestamp in this case)
print("--- Beginning Download ---")        
def download_timestamp():
    my_bucket = s3.Bucket('formulations-dev')
    objects = my_bucket.objects.filter(Prefix=prefix)
    for obj in objects:
        path, filename = os.path.split(obj.key)        
        my_bucket.download_file(obj.key, filename)     
download_timestamp()

print("--- Download Complete! ---")  

# Mosaic rasters and save output as Cloud-optimized Geotiff
print("--- Beginning Mosaic ---")
def mosaic_rasters():
    files_to_mosaic=glob.glob(wd+'*.tif')
    files_to_mosaic

    gdal.Warp(output_mosaic, files_to_mosaic, format="COG", options="-overwrite -multi -wm 80% -t_srs EPSG:5070 -co TILED=YES -co BIGTIFF=YES -co COMPRESS=DEFLATE -co NUM_THREADS=ALL_CPUS")
mosaic_rasters()
print("--- Rasters Mosaicked! ---")

#Upload mosaicked raster to the corresponding folder on the AWS s3 bucket
print("--- Beginning Upload ---")
def upload_mosaic():
    my_bucket = s3.Bucket('formulations-dev')
    object_name = uploadprefix + os.path.basename(output_mosaic)
    my_bucket.upload_file(output_mosaic, object_name)
upload_mosaic()
    
print("--- Upload Complete ---")

# Remove all .xml and .tif files
print("--- Cleaning Up Files ---")
cleandir = wd
files_in_directory = os.listdir(cleandir)
filtered_files = [file for file in files_in_directory if file.endswith(".tif")]
for file in filtered_files:
	path_to_file = os.path.join(cleandir, file)
	os.remove(path_to_file)
    
files_in_directory = os.listdir(cleandir)
filtered_files = [file for file in files_in_directory if file.endswith(".xml")]
for file in filtered_files:
	path_to_file = os.path.join(cleandir, file)
	os.remove(path_to_file)
    
print("--- 113 Done ---")

print("--- Beginning 121 ---")

# Let's use Amazon S3
s3 = boto3.resource('s3')
print("[INFO:] Connecting to cloud")

formdev = s3.Bucket('formulations-dev')

# prefix to be changed per timestamp
prefix = 'spatial-grids/GLASS/' + attribute + '_raw/' + attribute + '_' + year + '_121'

# final upload prefix
uploadprefix = 'spatial-grids/GLASS/' + attribute + '_mosaic/'

output_mosaic = wd + attribute + '_' + year + '_121.tif'

print("--- Filelist from AWS: ---")
# S3 list all keys with the prefix 'spatial-grids/GLASS/' + attribute + '_raw/'
for formdev in s3.buckets.all():
    for obj in formdev.objects.filter(Prefix=prefix):
        print('{0}:{1}'.format(formdev.name, obj.key))

# Download all objects in a bucket by given prefix (timestamp in this case)
print("--- Beginning Download ---")        
def download_timestamp():
    my_bucket = s3.Bucket('formulations-dev')
    objects = my_bucket.objects.filter(Prefix=prefix)
    for obj in objects:
        path, filename = os.path.split(obj.key)        
        my_bucket.download_file(obj.key, filename)     
download_timestamp()

print("--- Download Complete! ---")  

# Mosaic rasters and save output as Cloud-optimized Geotiff
print("--- Beginning Mosaic ---")
def mosaic_rasters():
    files_to_mosaic=glob.glob(wd+'*.tif')
    files_to_mosaic

    gdal.Warp(output_mosaic, files_to_mosaic, format="COG", options="-overwrite -multi -wm 80% -t_srs EPSG:5070 -co TILED=YES -co BIGTIFF=YES -co COMPRESS=DEFLATE -co NUM_THREADS=ALL_CPUS")
mosaic_rasters()
print("--- Rasters Mosaicked! ---")

#Upload mosaicked raster to the corresponding folder on the AWS s3 bucket
print("--- Beginning Upload ---")
def upload_mosaic():
    my_bucket = s3.Bucket('formulations-dev')
    object_name = uploadprefix + os.path.basename(output_mosaic)
    my_bucket.upload_file(output_mosaic, object_name)
upload_mosaic()
    
print("--- Upload Complete ---")

# Remove all .xml and .tif files
print("--- Cleaning Up Files ---")
cleandir = wd
files_in_directory = os.listdir(cleandir)
filtered_files = [file for file in files_in_directory if file.endswith(".tif")]
for file in filtered_files:
	path_to_file = os.path.join(cleandir, file)
	os.remove(path_to_file)
    
files_in_directory = os.listdir(cleandir)
filtered_files = [file for file in files_in_directory if file.endswith(".xml")]
for file in filtered_files:
	path_to_file = os.path.join(cleandir, file)
	os.remove(path_to_file)
    
print("--- 121 Done ---")

print("--- Beginning 129 ---")

# Let's use Amazon S3
s3 = boto3.resource('s3')
print("[INFO:] Connecting to cloud")

formdev = s3.Bucket('formulations-dev')

# prefix to be changed per timestamp
prefix = 'spatial-grids/GLASS/' + attribute + '_raw/' + attribute + '_' + year + '_129'

# final upload prefix
uploadprefix = 'spatial-grids/GLASS/' + attribute + '_mosaic/'

output_mosaic = wd + attribute + '_' + year + '_129.tif'

print("--- Filelist from AWS: ---")
# S3 list all keys with the prefix 'spatial-grids/GLASS/' + attribute + '_raw/'
for formdev in s3.buckets.all():
    for obj in formdev.objects.filter(Prefix=prefix):
        print('{0}:{1}'.format(formdev.name, obj.key))

# Download all objects in a bucket by given prefix (timestamp in this case)
print("--- Beginning Download ---")        
def download_timestamp():
    my_bucket = s3.Bucket('formulations-dev')
    objects = my_bucket.objects.filter(Prefix=prefix)
    for obj in objects:
        path, filename = os.path.split(obj.key)        
        my_bucket.download_file(obj.key, filename)     
download_timestamp()

print("--- Download Complete! ---")  

# Mosaic rasters and save output as Cloud-optimized Geotiff
print("--- Beginning Mosaic ---")
def mosaic_rasters():
    files_to_mosaic=glob.glob(wd+'*.tif')
    files_to_mosaic

    gdal.Warp(output_mosaic, files_to_mosaic, format="COG", options="-overwrite -multi -wm 80% -t_srs EPSG:5070 -co TILED=YES -co BIGTIFF=YES -co COMPRESS=DEFLATE -co NUM_THREADS=ALL_CPUS")
mosaic_rasters()
print("--- Rasters Mosaicked! ---")

#Upload mosaicked raster to the corresponding folder on the AWS s3 bucket
print("--- Beginning Upload ---")
def upload_mosaic():
    my_bucket = s3.Bucket('formulations-dev')
    object_name = uploadprefix + os.path.basename(output_mosaic)
    my_bucket.upload_file(output_mosaic, object_name)
upload_mosaic()
    
print("--- Upload Complete ---")

# Remove all .xml and .tif files
print("--- Cleaning Up Files ---")
cleandir = wd
files_in_directory = os.listdir(cleandir)
filtered_files = [file for file in files_in_directory if file.endswith(".tif")]
for file in filtered_files:
	path_to_file = os.path.join(cleandir, file)
	os.remove(path_to_file)
    
files_in_directory = os.listdir(cleandir)
filtered_files = [file for file in files_in_directory if file.endswith(".xml")]
for file in filtered_files:
	path_to_file = os.path.join(cleandir, file)
	os.remove(path_to_file)
    
print("--- 129 Done ---")

print("--- Beginning 137 ---")

# Let's use Amazon S3
s3 = boto3.resource('s3')
print("[INFO:] Connecting to cloud")

formdev = s3.Bucket('formulations-dev')

# prefix to be changed per timestamp
prefix = 'spatial-grids/GLASS/' + attribute + '_raw/' + attribute + '_' + year + '_137'

# final upload prefix
uploadprefix = 'spatial-grids/GLASS/' + attribute + '_mosaic/'

output_mosaic = wd + attribute + '_' + year + '_137.tif'

print("--- Filelist from AWS: ---")
# S3 list all keys with the prefix 'spatial-grids/GLASS/' + attribute + '_raw/'
for formdev in s3.buckets.all():
    for obj in formdev.objects.filter(Prefix=prefix):
        print('{0}:{1}'.format(formdev.name, obj.key))

# Download all objects in a bucket by given prefix (timestamp in this case)
print("--- Beginning Download ---")        
def download_timestamp():
    my_bucket = s3.Bucket('formulations-dev')
    objects = my_bucket.objects.filter(Prefix=prefix)
    for obj in objects:
        path, filename = os.path.split(obj.key)        
        my_bucket.download_file(obj.key, filename)     
download_timestamp()

print("--- Download Complete! ---")  

# Mosaic rasters and save output as Cloud-optimized Geotiff
print("--- Beginning Mosaic ---")
def mosaic_rasters():
    files_to_mosaic=glob.glob(wd+'*.tif')
    files_to_mosaic

    gdal.Warp(output_mosaic, files_to_mosaic, format="COG", options="-overwrite -multi -wm 80% -t_srs EPSG:5070 -co TILED=YES -co BIGTIFF=YES -co COMPRESS=DEFLATE -co NUM_THREADS=ALL_CPUS")
mosaic_rasters()
print("--- Rasters Mosaicked! ---")

#Upload mosaicked raster to the corresponding folder on the AWS s3 bucket
print("--- Beginning Upload ---")
def upload_mosaic():
    my_bucket = s3.Bucket('formulations-dev')
    object_name = uploadprefix + os.path.basename(output_mosaic)
    my_bucket.upload_file(output_mosaic, object_name)
upload_mosaic()
    
print("--- Upload Complete ---")

# Remove all .xml and .tif files
print("--- Cleaning Up Files ---")
cleandir = wd
files_in_directory = os.listdir(cleandir)
filtered_files = [file for file in files_in_directory if file.endswith(".tif")]
for file in filtered_files:
	path_to_file = os.path.join(cleandir, file)
	os.remove(path_to_file)
    
files_in_directory = os.listdir(cleandir)
filtered_files = [file for file in files_in_directory if file.endswith(".xml")]
for file in filtered_files:
	path_to_file = os.path.join(cleandir, file)
	os.remove(path_to_file)
    
print("--- 137 Done ---")

print("--- Beginning 145 ---")

# Let's use Amazon S3
s3 = boto3.resource('s3')
print("[INFO:] Connecting to cloud")

formdev = s3.Bucket('formulations-dev')

# prefix to be changed per timestamp
prefix = 'spatial-grids/GLASS/' + attribute + '_raw/' + attribute + '_' + year + '_145'

# final upload prefix
uploadprefix = 'spatial-grids/GLASS/' + attribute + '_mosaic/'

output_mosaic = wd + attribute + '_' + year + '_145.tif'

print("--- Filelist from AWS: ---")
# S3 list all keys with the prefix 'spatial-grids/GLASS/' + attribute + '_raw/'
for formdev in s3.buckets.all():
    for obj in formdev.objects.filter(Prefix=prefix):
        print('{0}:{1}'.format(formdev.name, obj.key))

# Download all objects in a bucket by given prefix (timestamp in this case)
print("--- Beginning Download ---")        
def download_timestamp():
    my_bucket = s3.Bucket('formulations-dev')
    objects = my_bucket.objects.filter(Prefix=prefix)
    for obj in objects:
        path, filename = os.path.split(obj.key)        
        my_bucket.download_file(obj.key, filename)     
download_timestamp()

print("--- Download Complete! ---")  

# Mosaic rasters and save output as Cloud-optimized Geotiff
print("--- Beginning Mosaic ---")
def mosaic_rasters():
    files_to_mosaic=glob.glob(wd+'*.tif')
    files_to_mosaic

    gdal.Warp(output_mosaic, files_to_mosaic, format="COG", options="-overwrite -multi -wm 80% -t_srs EPSG:5070 -co TILED=YES -co BIGTIFF=YES -co COMPRESS=DEFLATE -co NUM_THREADS=ALL_CPUS")
mosaic_rasters()
print("--- Rasters Mosaicked! ---")

#Upload mosaicked raster to the corresponding folder on the AWS s3 bucket
print("--- Beginning Upload ---")
def upload_mosaic():
    my_bucket = s3.Bucket('formulations-dev')
    object_name = uploadprefix + os.path.basename(output_mosaic)
    my_bucket.upload_file(output_mosaic, object_name)
upload_mosaic()
    
print("--- Upload Complete ---")

# Remove all .xml and .tif files
print("--- Cleaning Up Files ---")
cleandir = wd
files_in_directory = os.listdir(cleandir)
filtered_files = [file for file in files_in_directory if file.endswith(".tif")]
for file in filtered_files:
	path_to_file = os.path.join(cleandir, file)
	os.remove(path_to_file)
    
files_in_directory = os.listdir(cleandir)
filtered_files = [file for file in files_in_directory if file.endswith(".xml")]
for file in filtered_files:
	path_to_file = os.path.join(cleandir, file)
	os.remove(path_to_file)
    
print("--- 145 Done ---")

print("--- Beginning 153 ---")

# Let's use Amazon S3
s3 = boto3.resource('s3')
print("[INFO:] Connecting to cloud")

formdev = s3.Bucket('formulations-dev')

# prefix to be changed per timestamp
prefix = 'spatial-grids/GLASS/' + attribute + '_raw/' + attribute + '_' + year + '_153'

# final upload prefix
uploadprefix = 'spatial-grids/GLASS/' + attribute + '_mosaic/'

output_mosaic = wd + attribute + '_' + year + '_153.tif'

print("--- Filelist from AWS: ---")
# S3 list all keys with the prefix 'spatial-grids/GLASS/' + attribute + '_raw/'
for formdev in s3.buckets.all():
    for obj in formdev.objects.filter(Prefix=prefix):
        print('{0}:{1}'.format(formdev.name, obj.key))

# Download all objects in a bucket by given prefix (timestamp in this case)
print("--- Beginning Download ---")        
def download_timestamp():
    my_bucket = s3.Bucket('formulations-dev')
    objects = my_bucket.objects.filter(Prefix=prefix)
    for obj in objects:
        path, filename = os.path.split(obj.key)        
        my_bucket.download_file(obj.key, filename)     
download_timestamp()

print("--- Download Complete! ---")  

# Mosaic rasters and save output as Cloud-optimized Geotiff
print("--- Beginning Mosaic ---")
def mosaic_rasters():
    files_to_mosaic=glob.glob(wd+'*.tif')
    files_to_mosaic

    gdal.Warp(output_mosaic, files_to_mosaic, format="COG", options="-overwrite -multi -wm 80% -t_srs EPSG:5070 -co TILED=YES -co BIGTIFF=YES -co COMPRESS=DEFLATE -co NUM_THREADS=ALL_CPUS")
mosaic_rasters()
print("--- Rasters Mosaicked! ---")

#Upload mosaicked raster to the corresponding folder on the AWS s3 bucket
print("--- Beginning Upload ---")
def upload_mosaic():
    my_bucket = s3.Bucket('formulations-dev')
    object_name = uploadprefix + os.path.basename(output_mosaic)
    my_bucket.upload_file(output_mosaic, object_name)
upload_mosaic()
    
print("--- Upload Complete ---")

# Remove all .xml and .tif files
print("--- Cleaning Up Files ---")
cleandir = wd
files_in_directory = os.listdir(cleandir)
filtered_files = [file for file in files_in_directory if file.endswith(".tif")]
for file in filtered_files:
	path_to_file = os.path.join(cleandir, file)
	os.remove(path_to_file)
    
files_in_directory = os.listdir(cleandir)
filtered_files = [file for file in files_in_directory if file.endswith(".xml")]
for file in filtered_files:
	path_to_file = os.path.join(cleandir, file)
	os.remove(path_to_file)
    
print("--- 153 Done ---")

print("--- Beginning 161 ---")

# Let's use Amazon S3
s3 = boto3.resource('s3')
print("[INFO:] Connecting to cloud")

formdev = s3.Bucket('formulations-dev')

# prefix to be changed per timestamp
prefix = 'spatial-grids/GLASS/' + attribute + '_raw/' + attribute + '_' + year + '_161'

# final upload prefix
uploadprefix = 'spatial-grids/GLASS/' + attribute + '_mosaic/'

output_mosaic = wd + attribute + '_' + year + '_161.tif'

print("--- Filelist from AWS: ---")
# S3 list all keys with the prefix 'spatial-grids/GLASS/' + attribute + '_raw/'
for formdev in s3.buckets.all():
    for obj in formdev.objects.filter(Prefix=prefix):
        print('{0}:{1}'.format(formdev.name, obj.key))

# Download all objects in a bucket by given prefix (timestamp in this case)
print("--- Beginning Download ---")        
def download_timestamp():
    my_bucket = s3.Bucket('formulations-dev')
    objects = my_bucket.objects.filter(Prefix=prefix)
    for obj in objects:
        path, filename = os.path.split(obj.key)        
        my_bucket.download_file(obj.key, filename)     
download_timestamp()

print("--- Download Complete! ---")  

# Mosaic rasters and save output as Cloud-optimized Geotiff
print("--- Beginning Mosaic ---")
def mosaic_rasters():
    files_to_mosaic=glob.glob(wd+'*.tif')
    files_to_mosaic

    gdal.Warp(output_mosaic, files_to_mosaic, format="COG", options="-overwrite -multi -wm 80% -t_srs EPSG:5070 -co TILED=YES -co BIGTIFF=YES -co COMPRESS=DEFLATE -co NUM_THREADS=ALL_CPUS")
mosaic_rasters()
print("--- Rasters Mosaicked! ---")

#Upload mosaicked raster to the corresponding folder on the AWS s3 bucket
print("--- Beginning Upload ---")
def upload_mosaic():
    my_bucket = s3.Bucket('formulations-dev')
    object_name = uploadprefix + os.path.basename(output_mosaic)
    my_bucket.upload_file(output_mosaic, object_name)
upload_mosaic()
    
print("--- Upload Complete ---")

# Remove all .xml and .tif files
print("--- Cleaning Up Files ---")
cleandir = wd
files_in_directory = os.listdir(cleandir)
filtered_files = [file for file in files_in_directory if file.endswith(".tif")]
for file in filtered_files:
	path_to_file = os.path.join(cleandir, file)
	os.remove(path_to_file)
    
files_in_directory = os.listdir(cleandir)
filtered_files = [file for file in files_in_directory if file.endswith(".xml")]
for file in filtered_files:
	path_to_file = os.path.join(cleandir, file)
	os.remove(path_to_file)
    
print("--- 161 Done ---")

print("--- Beginning 169 ---")

# Let's use Amazon S3
s3 = boto3.resource('s3')
print("[INFO:] Connecting to cloud")

formdev = s3.Bucket('formulations-dev')

# prefix to be changed per timestamp
prefix = 'spatial-grids/GLASS/' + attribute + '_raw/' + attribute + '_' + year + '_169'

# final upload prefix
uploadprefix = 'spatial-grids/GLASS/' + attribute + '_mosaic/'

output_mosaic = wd + attribute + '_' + year + '_169.tif'

print("--- Filelist from AWS: ---")
# S3 list all keys with the prefix 'spatial-grids/GLASS/' + attribute + '_raw/'
for formdev in s3.buckets.all():
    for obj in formdev.objects.filter(Prefix=prefix):
        print('{0}:{1}'.format(formdev.name, obj.key))

# Download all objects in a bucket by given prefix (timestamp in this case)
print("--- Beginning Download ---")        
def download_timestamp():
    my_bucket = s3.Bucket('formulations-dev')
    objects = my_bucket.objects.filter(Prefix=prefix)
    for obj in objects:
        path, filename = os.path.split(obj.key)        
        my_bucket.download_file(obj.key, filename)     
download_timestamp()

print("--- Download Complete! ---")  

# Mosaic rasters and save output as Cloud-optimized Geotiff
print("--- Beginning Mosaic ---")
def mosaic_rasters():
    files_to_mosaic=glob.glob(wd+'*.tif')
    files_to_mosaic

    gdal.Warp(output_mosaic, files_to_mosaic, format="COG", options="-overwrite -multi -wm 80% -t_srs EPSG:5070 -co TILED=YES -co BIGTIFF=YES -co COMPRESS=DEFLATE -co NUM_THREADS=ALL_CPUS")
mosaic_rasters()
print("--- Rasters Mosaicked! ---")

#Upload mosaicked raster to the corresponding folder on the AWS s3 bucket
print("--- Beginning Upload ---")
def upload_mosaic():
    my_bucket = s3.Bucket('formulations-dev')
    object_name = uploadprefix + os.path.basename(output_mosaic)
    my_bucket.upload_file(output_mosaic, object_name)
upload_mosaic()
    
print("--- Upload Complete ---")

# Remove all .xml and .tif files
print("--- Cleaning Up Files ---")
cleandir = wd
files_in_directory = os.listdir(cleandir)
filtered_files = [file for file in files_in_directory if file.endswith(".tif")]
for file in filtered_files:
	path_to_file = os.path.join(cleandir, file)
	os.remove(path_to_file)
    
files_in_directory = os.listdir(cleandir)
filtered_files = [file for file in files_in_directory if file.endswith(".xml")]
for file in filtered_files:
	path_to_file = os.path.join(cleandir, file)
	os.remove(path_to_file)
    
print("--- 169 Done ---")

print("--- Beginning 177 ---")

# Let's use Amazon S3
s3 = boto3.resource('s3')
print("[INFO:] Connecting to cloud")

formdev = s3.Bucket('formulations-dev')

# prefix to be changed per timestamp
prefix = 'spatial-grids/GLASS/' + attribute + '_raw/' + attribute + '_' + year + '_177'

# final upload prefix
uploadprefix = 'spatial-grids/GLASS/' + attribute + '_mosaic/'

output_mosaic = wd + attribute + '_' + year + '_177.tif'

print("--- Filelist from AWS: ---")
# S3 list all keys with the prefix 'spatial-grids/GLASS/' + attribute + '_raw/'
for formdev in s3.buckets.all():
    for obj in formdev.objects.filter(Prefix=prefix):
        print('{0}:{1}'.format(formdev.name, obj.key))

# Download all objects in a bucket by given prefix (timestamp in this case)
print("--- Beginning Download ---")        
def download_timestamp():
    my_bucket = s3.Bucket('formulations-dev')
    objects = my_bucket.objects.filter(Prefix=prefix)
    for obj in objects:
        path, filename = os.path.split(obj.key)        
        my_bucket.download_file(obj.key, filename)     
download_timestamp()

print("--- Download Complete! ---")  

# Mosaic rasters and save output as Cloud-optimized Geotiff
print("--- Beginning Mosaic ---")
def mosaic_rasters():
    files_to_mosaic=glob.glob(wd+'*.tif')
    files_to_mosaic

    gdal.Warp(output_mosaic, files_to_mosaic, format="COG", options="-overwrite -multi -wm 80% -t_srs EPSG:5070 -co TILED=YES -co BIGTIFF=YES -co COMPRESS=DEFLATE -co NUM_THREADS=ALL_CPUS")
mosaic_rasters()
print("--- Rasters Mosaicked! ---")

#Upload mosaicked raster to the corresponding folder on the AWS s3 bucket
print("--- Beginning Upload ---")
def upload_mosaic():
    my_bucket = s3.Bucket('formulations-dev')
    object_name = uploadprefix + os.path.basename(output_mosaic)
    my_bucket.upload_file(output_mosaic, object_name)
upload_mosaic()
    
print("--- Upload Complete ---")

# Remove all .xml and .tif files
print("--- Cleaning Up Files ---")
cleandir = wd
files_in_directory = os.listdir(cleandir)
filtered_files = [file for file in files_in_directory if file.endswith(".tif")]
for file in filtered_files:
	path_to_file = os.path.join(cleandir, file)
	os.remove(path_to_file)
    
files_in_directory = os.listdir(cleandir)
filtered_files = [file for file in files_in_directory if file.endswith(".xml")]
for file in filtered_files:
	path_to_file = os.path.join(cleandir, file)
	os.remove(path_to_file)
    
print("--- 177 Done ---")

print("--- Beginning 185 ---")

# Let's use Amazon S3
s3 = boto3.resource('s3')
print("[INFO:] Connecting to cloud")

formdev = s3.Bucket('formulations-dev')

# prefix to be changed per timestamp
prefix = 'spatial-grids/GLASS/' + attribute + '_raw/' + attribute + '_' + year + '_185'

# final upload prefix
uploadprefix = 'spatial-grids/GLASS/' + attribute + '_mosaic/'

output_mosaic = wd + attribute + '_' + year + '_185.tif'

print("--- Filelist from AWS: ---")
# S3 list all keys with the prefix 'spatial-grids/GLASS/' + attribute + '_raw/'
for formdev in s3.buckets.all():
    for obj in formdev.objects.filter(Prefix=prefix):
        print('{0}:{1}'.format(formdev.name, obj.key))

# Download all objects in a bucket by given prefix (timestamp in this case)
print("--- Beginning Download ---")        
def download_timestamp():
    my_bucket = s3.Bucket('formulations-dev')
    objects = my_bucket.objects.filter(Prefix=prefix)
    for obj in objects:
        path, filename = os.path.split(obj.key)        
        my_bucket.download_file(obj.key, filename)     
download_timestamp()

print("--- Download Complete! ---")  

# Mosaic rasters and save output as Cloud-optimized Geotiff
print("--- Beginning Mosaic ---")
def mosaic_rasters():
    files_to_mosaic=glob.glob(wd+'*.tif')
    files_to_mosaic

    gdal.Warp(output_mosaic, files_to_mosaic, format="COG", options="-overwrite -multi -wm 80% -t_srs EPSG:5070 -co TILED=YES -co BIGTIFF=YES -co COMPRESS=DEFLATE -co NUM_THREADS=ALL_CPUS")
mosaic_rasters()
print("--- Rasters Mosaicked! ---")

#Upload mosaicked raster to the corresponding folder on the AWS s3 bucket
print("--- Beginning Upload ---")
def upload_mosaic():
    my_bucket = s3.Bucket('formulations-dev')
    object_name = uploadprefix + os.path.basename(output_mosaic)
    my_bucket.upload_file(output_mosaic, object_name)
upload_mosaic()
    
print("--- Upload Complete ---")

# Remove all .xml and .tif files
print("--- Cleaning Up Files ---")
cleandir = wd
files_in_directory = os.listdir(cleandir)
filtered_files = [file for file in files_in_directory if file.endswith(".tif")]
for file in filtered_files:
	path_to_file = os.path.join(cleandir, file)
	os.remove(path_to_file)
    
files_in_directory = os.listdir(cleandir)
filtered_files = [file for file in files_in_directory if file.endswith(".xml")]
for file in filtered_files:
	path_to_file = os.path.join(cleandir, file)
	os.remove(path_to_file)
    
print("--- 185 Done ---")

print("--- Beginning 193 ---")

# Let's use Amazon S3
s3 = boto3.resource('s3')
print("[INFO:] Connecting to cloud")

formdev = s3.Bucket('formulations-dev')

# prefix to be changed per timestamp
prefix = 'spatial-grids/GLASS/' + attribute + '_raw/' + attribute + '_' + year + '_193'

# final upload prefix
uploadprefix = 'spatial-grids/GLASS/' + attribute + '_mosaic/'

output_mosaic = wd + attribute + '_' + year + '_193.tif'

print("--- Filelist from AWS: ---")
# S3 list all keys with the prefix 'spatial-grids/GLASS/' + attribute + '_raw/'
for formdev in s3.buckets.all():
    for obj in formdev.objects.filter(Prefix=prefix):
        print('{0}:{1}'.format(formdev.name, obj.key))

# Download all objects in a bucket by given prefix (timestamp in this case)
print("--- Beginning Download ---")        
def download_timestamp():
    my_bucket = s3.Bucket('formulations-dev')
    objects = my_bucket.objects.filter(Prefix=prefix)
    for obj in objects:
        path, filename = os.path.split(obj.key)        
        my_bucket.download_file(obj.key, filename)     
download_timestamp()

print("--- Download Complete! ---")  

# Mosaic rasters and save output as Cloud-optimized Geotiff
print("--- Beginning Mosaic ---")
def mosaic_rasters():
    files_to_mosaic=glob.glob(wd+'*.tif')
    files_to_mosaic

    gdal.Warp(output_mosaic, files_to_mosaic, format="COG", options="-overwrite -multi -wm 80% -t_srs EPSG:5070 -co TILED=YES -co BIGTIFF=YES -co COMPRESS=DEFLATE -co NUM_THREADS=ALL_CPUS")
mosaic_rasters()
print("--- Rasters Mosaicked! ---")

#Upload mosaicked raster to the corresponding folder on the AWS s3 bucket
print("--- Beginning Upload ---")
def upload_mosaic():
    my_bucket = s3.Bucket('formulations-dev')
    object_name = uploadprefix + os.path.basename(output_mosaic)
    my_bucket.upload_file(output_mosaic, object_name)
upload_mosaic()
    
print("--- Upload Complete ---")

# Remove all .xml and .tif files
print("--- Cleaning Up Files ---")
cleandir = wd
files_in_directory = os.listdir(cleandir)
filtered_files = [file for file in files_in_directory if file.endswith(".tif")]
for file in filtered_files:
	path_to_file = os.path.join(cleandir, file)
	os.remove(path_to_file)
    
files_in_directory = os.listdir(cleandir)
filtered_files = [file for file in files_in_directory if file.endswith(".xml")]
for file in filtered_files:
	path_to_file = os.path.join(cleandir, file)
	os.remove(path_to_file)
    
print("--- 193 Done ---")

print("--- Beginning 201 ---")

# Let's use Amazon S3
s3 = boto3.resource('s3')
print("[INFO:] Connecting to cloud")

formdev = s3.Bucket('formulations-dev')

# prefix to be changed per timestamp
prefix = 'spatial-grids/GLASS/' + attribute + '_raw/' + attribute + '_' + year + '_201'

# final upload prefix
uploadprefix = 'spatial-grids/GLASS/' + attribute + '_mosaic/'

output_mosaic = wd + attribute + '_' + year + '_201.tif'

print("--- Filelist from AWS: ---")
# S3 list all keys with the prefix 'spatial-grids/GLASS/' + attribute + '_raw/'
for formdev in s3.buckets.all():
    for obj in formdev.objects.filter(Prefix=prefix):
        print('{0}:{1}'.format(formdev.name, obj.key))

# Download all objects in a bucket by given prefix (timestamp in this case)
print("--- Beginning Download ---")        
def download_timestamp():
    my_bucket = s3.Bucket('formulations-dev')
    objects = my_bucket.objects.filter(Prefix=prefix)
    for obj in objects:
        path, filename = os.path.split(obj.key)        
        my_bucket.download_file(obj.key, filename)     
download_timestamp()

print("--- Download Complete! ---")  

# Mosaic rasters and save output as Cloud-optimized Geotiff
print("--- Beginning Mosaic ---")
def mosaic_rasters():
    files_to_mosaic=glob.glob(wd+'*.tif')
    files_to_mosaic

    gdal.Warp(output_mosaic, files_to_mosaic, format="COG", options="-overwrite -multi -wm 80% -t_srs EPSG:5070 -co TILED=YES -co BIGTIFF=YES -co COMPRESS=DEFLATE -co NUM_THREADS=ALL_CPUS")
mosaic_rasters()
print("--- Rasters Mosaicked! ---")

#Upload mosaicked raster to the corresponding folder on the AWS s3 bucket
print("--- Beginning Upload ---")
def upload_mosaic():
    my_bucket = s3.Bucket('formulations-dev')
    object_name = uploadprefix + os.path.basename(output_mosaic)
    my_bucket.upload_file(output_mosaic, object_name)
upload_mosaic()
    
print("--- Upload Complete ---")

# Remove all .xml and .tif files
print("--- Cleaning Up Files ---")
cleandir = wd
files_in_directory = os.listdir(cleandir)
filtered_files = [file for file in files_in_directory if file.endswith(".tif")]
for file in filtered_files:
	path_to_file = os.path.join(cleandir, file)
	os.remove(path_to_file)
    
files_in_directory = os.listdir(cleandir)
filtered_files = [file for file in files_in_directory if file.endswith(".xml")]
for file in filtered_files:
	path_to_file = os.path.join(cleandir, file)
	os.remove(path_to_file)
    
print("--- 201 Done ---")

print("--- Beginning 209 ---")

# Let's use Amazon S3
s3 = boto3.resource('s3')
print("[INFO:] Connecting to cloud")

formdev = s3.Bucket('formulations-dev')

# prefix to be changed per timestamp
prefix = 'spatial-grids/GLASS/' + attribute + '_raw/' + attribute + '_' + year + '_209'

# final upload prefix
uploadprefix = 'spatial-grids/GLASS/' + attribute + '_mosaic/'

output_mosaic = wd + attribute + '_' + year + '_209.tif'

print("--- Filelist from AWS: ---")
# S3 list all keys with the prefix 'spatial-grids/GLASS/' + attribute + '_raw/'
for formdev in s3.buckets.all():
    for obj in formdev.objects.filter(Prefix=prefix):
        print('{0}:{1}'.format(formdev.name, obj.key))

# Download all objects in a bucket by given prefix (timestamp in this case)
print("--- Beginning Download ---")        
def download_timestamp():
    my_bucket = s3.Bucket('formulations-dev')
    objects = my_bucket.objects.filter(Prefix=prefix)
    for obj in objects:
        path, filename = os.path.split(obj.key)        
        my_bucket.download_file(obj.key, filename)     
download_timestamp()

print("--- Download Complete! ---")  

# Mosaic rasters and save output as Cloud-optimized Geotiff
print("--- Beginning Mosaic ---")
def mosaic_rasters():
    files_to_mosaic=glob.glob(wd+'*.tif')
    files_to_mosaic

    gdal.Warp(output_mosaic, files_to_mosaic, format="COG", options="-overwrite -multi -wm 80% -t_srs EPSG:5070 -co TILED=YES -co BIGTIFF=YES -co COMPRESS=DEFLATE -co NUM_THREADS=ALL_CPUS")
mosaic_rasters()
print("--- Rasters Mosaicked! ---")

#Upload mosaicked raster to the corresponding folder on the AWS s3 bucket
print("--- Beginning Upload ---")
def upload_mosaic():
    my_bucket = s3.Bucket('formulations-dev')
    object_name = uploadprefix + os.path.basename(output_mosaic)
    my_bucket.upload_file(output_mosaic, object_name)
upload_mosaic()
    
print("--- Upload Complete ---")

# Remove all .xml and .tif files
print("--- Cleaning Up Files ---")
cleandir = wd
files_in_directory = os.listdir(cleandir)
filtered_files = [file for file in files_in_directory if file.endswith(".tif")]
for file in filtered_files:
	path_to_file = os.path.join(cleandir, file)
	os.remove(path_to_file)
    
files_in_directory = os.listdir(cleandir)
filtered_files = [file for file in files_in_directory if file.endswith(".xml")]
for file in filtered_files:
	path_to_file = os.path.join(cleandir, file)
	os.remove(path_to_file)
    
print("--- 209 Done ---")

print("--- Beginning 217 ---")

# Let's use Amazon S3
s3 = boto3.resource('s3')
print("[INFO:] Connecting to cloud")

formdev = s3.Bucket('formulations-dev')

# prefix to be changed per timestamp
prefix = 'spatial-grids/GLASS/' + attribute + '_raw/' + attribute + '_' + year + '_217'

# final upload prefix
uploadprefix = 'spatial-grids/GLASS/' + attribute + '_mosaic/'

output_mosaic = wd + attribute + '_' + year + '_217.tif'

print("--- Filelist from AWS: ---")
# S3 list all keys with the prefix 'spatial-grids/GLASS/' + attribute + '_raw/'
for formdev in s3.buckets.all():
    for obj in formdev.objects.filter(Prefix=prefix):
        print('{0}:{1}'.format(formdev.name, obj.key))

# Download all objects in a bucket by given prefix (timestamp in this case)
print("--- Beginning Download ---")        
def download_timestamp():
    my_bucket = s3.Bucket('formulations-dev')
    objects = my_bucket.objects.filter(Prefix=prefix)
    for obj in objects:
        path, filename = os.path.split(obj.key)        
        my_bucket.download_file(obj.key, filename)     
download_timestamp()

print("--- Download Complete! ---")  

# Mosaic rasters and save output as Cloud-optimized Geotiff
print("--- Beginning Mosaic ---")
def mosaic_rasters():
    files_to_mosaic=glob.glob(wd+'*.tif')
    files_to_mosaic

    gdal.Warp(output_mosaic, files_to_mosaic, format="COG", options="-overwrite -multi -wm 80% -t_srs EPSG:5070 -co TILED=YES -co BIGTIFF=YES -co COMPRESS=DEFLATE -co NUM_THREADS=ALL_CPUS")
mosaic_rasters()
print("--- Rasters Mosaicked! ---")

#Upload mosaicked raster to the corresponding folder on the AWS s3 bucket
print("--- Beginning Upload ---")
def upload_mosaic():
    my_bucket = s3.Bucket('formulations-dev')
    object_name = uploadprefix + os.path.basename(output_mosaic)
    my_bucket.upload_file(output_mosaic, object_name)
upload_mosaic()
    
print("--- Upload Complete ---")

# Remove all .xml and .tif files
print("--- Cleaning Up Files ---")
cleandir = wd
files_in_directory = os.listdir(cleandir)
filtered_files = [file for file in files_in_directory if file.endswith(".tif")]
for file in filtered_files:
	path_to_file = os.path.join(cleandir, file)
	os.remove(path_to_file)
    
files_in_directory = os.listdir(cleandir)
filtered_files = [file for file in files_in_directory if file.endswith(".xml")]
for file in filtered_files:
	path_to_file = os.path.join(cleandir, file)
	os.remove(path_to_file)
    
print("--- 217 Done ---")

print("--- Beginning 225 ---")

# Let's use Amazon S3
s3 = boto3.resource('s3')
print("[INFO:] Connecting to cloud")

formdev = s3.Bucket('formulations-dev')

# prefix to be changed per timestamp
prefix = 'spatial-grids/GLASS/' + attribute + '_raw/' + attribute + '_' + year + '_225'

# final upload prefix
uploadprefix = 'spatial-grids/GLASS/' + attribute + '_mosaic/'

output_mosaic = wd + attribute + '_' + year + '_225.tif'

print("--- Filelist from AWS: ---")
# S3 list all keys with the prefix 'spatial-grids/GLASS/' + attribute + '_raw/'
for formdev in s3.buckets.all():
    for obj in formdev.objects.filter(Prefix=prefix):
        print('{0}:{1}'.format(formdev.name, obj.key))

# Download all objects in a bucket by given prefix (timestamp in this case)
print("--- Beginning Download ---")        
def download_timestamp():
    my_bucket = s3.Bucket('formulations-dev')
    objects = my_bucket.objects.filter(Prefix=prefix)
    for obj in objects:
        path, filename = os.path.split(obj.key)        
        my_bucket.download_file(obj.key, filename)     
download_timestamp()

print("--- Download Complete! ---")  

# Mosaic rasters and save output as Cloud-optimized Geotiff
print("--- Beginning Mosaic ---")
def mosaic_rasters():
    files_to_mosaic=glob.glob(wd+'*.tif')
    files_to_mosaic

    gdal.Warp(output_mosaic, files_to_mosaic, format="COG", options="-overwrite -multi -wm 80% -t_srs EPSG:5070 -co TILED=YES -co BIGTIFF=YES -co COMPRESS=DEFLATE -co NUM_THREADS=ALL_CPUS")
mosaic_rasters()
print("--- Rasters Mosaicked! ---")

#Upload mosaicked raster to the corresponding folder on the AWS s3 bucket
print("--- Beginning Upload ---")
def upload_mosaic():
    my_bucket = s3.Bucket('formulations-dev')
    object_name = uploadprefix + os.path.basename(output_mosaic)
    my_bucket.upload_file(output_mosaic, object_name)
upload_mosaic()
    
print("--- Upload Complete ---")

# Remove all .xml and .tif files
print("--- Cleaning Up Files ---")
cleandir = wd
files_in_directory = os.listdir(cleandir)
filtered_files = [file for file in files_in_directory if file.endswith(".tif")]
for file in filtered_files:
	path_to_file = os.path.join(cleandir, file)
	os.remove(path_to_file)
    
files_in_directory = os.listdir(cleandir)
filtered_files = [file for file in files_in_directory if file.endswith(".xml")]
for file in filtered_files:
	path_to_file = os.path.join(cleandir, file)
	os.remove(path_to_file)
    
print("--- 225 Done ---")

print("--- Beginning 233 ---")

# Let's use Amazon S3
s3 = boto3.resource('s3')
print("[INFO:] Connecting to cloud")

formdev = s3.Bucket('formulations-dev')

# prefix to be changed per timestamp
prefix = 'spatial-grids/GLASS/' + attribute + '_raw/' + attribute + '_' + year + '_233'

# final upload prefix
uploadprefix = 'spatial-grids/GLASS/' + attribute + '_mosaic/'

output_mosaic = wd + attribute + '_' + year + '_233.tif'

print("--- Filelist from AWS: ---")
# S3 list all keys with the prefix 'spatial-grids/GLASS/' + attribute + '_raw/'
for formdev in s3.buckets.all():
    for obj in formdev.objects.filter(Prefix=prefix):
        print('{0}:{1}'.format(formdev.name, obj.key))

# Download all objects in a bucket by given prefix (timestamp in this case)
print("--- Beginning Download ---")        
def download_timestamp():
    my_bucket = s3.Bucket('formulations-dev')
    objects = my_bucket.objects.filter(Prefix=prefix)
    for obj in objects:
        path, filename = os.path.split(obj.key)        
        my_bucket.download_file(obj.key, filename)     
download_timestamp()

print("--- Download Complete! ---")  

# Mosaic rasters and save output as Cloud-optimized Geotiff
print("--- Beginning Mosaic ---")
def mosaic_rasters():
    files_to_mosaic=glob.glob(wd+'*.tif')
    files_to_mosaic

    gdal.Warp(output_mosaic, files_to_mosaic, format="COG", options="-overwrite -multi -wm 80% -t_srs EPSG:5070 -co TILED=YES -co BIGTIFF=YES -co COMPRESS=DEFLATE -co NUM_THREADS=ALL_CPUS")
mosaic_rasters()
print("--- Rasters Mosaicked! ---")

#Upload mosaicked raster to the corresponding folder on the AWS s3 bucket
print("--- Beginning Upload ---")
def upload_mosaic():
    my_bucket = s3.Bucket('formulations-dev')
    object_name = uploadprefix + os.path.basename(output_mosaic)
    my_bucket.upload_file(output_mosaic, object_name)
upload_mosaic()
    
print("--- Upload Complete ---")

# Remove all .xml and .tif files
print("--- Cleaning Up Files ---")
cleandir = wd
files_in_directory = os.listdir(cleandir)
filtered_files = [file for file in files_in_directory if file.endswith(".tif")]
for file in filtered_files:
	path_to_file = os.path.join(cleandir, file)
	os.remove(path_to_file)
    
files_in_directory = os.listdir(cleandir)
filtered_files = [file for file in files_in_directory if file.endswith(".xml")]
for file in filtered_files:
	path_to_file = os.path.join(cleandir, file)
	os.remove(path_to_file)
    
print("--- 233 Done ---")

print("--- Beginning 241 ---")

# Let's use Amazon S3
s3 = boto3.resource('s3')
print("[INFO:] Connecting to cloud")

formdev = s3.Bucket('formulations-dev')

# prefix to be changed per timestamp
prefix = 'spatial-grids/GLASS/' + attribute + '_raw/' + attribute + '_' + year + '_241'

# final upload prefix
uploadprefix = 'spatial-grids/GLASS/' + attribute + '_mosaic/'

output_mosaic = wd + attribute + '_' + year + '_241.tif'

print("--- Filelist from AWS: ---")
# S3 list all keys with the prefix 'spatial-grids/GLASS/' + attribute + '_raw/'
for formdev in s3.buckets.all():
    for obj in formdev.objects.filter(Prefix=prefix):
        print('{0}:{1}'.format(formdev.name, obj.key))

# Download all objects in a bucket by given prefix (timestamp in this case)
print("--- Beginning Download ---")        
def download_timestamp():
    my_bucket = s3.Bucket('formulations-dev')
    objects = my_bucket.objects.filter(Prefix=prefix)
    for obj in objects:
        path, filename = os.path.split(obj.key)        
        my_bucket.download_file(obj.key, filename)     
download_timestamp()

print("--- Download Complete! ---")  

# Mosaic rasters and save output as Cloud-optimized Geotiff
print("--- Beginning Mosaic ---")
def mosaic_rasters():
    files_to_mosaic=glob.glob(wd+'*.tif')
    files_to_mosaic

    gdal.Warp(output_mosaic, files_to_mosaic, format="COG", options="-overwrite -multi -wm 80% -t_srs EPSG:5070 -co TILED=YES -co BIGTIFF=YES -co COMPRESS=DEFLATE -co NUM_THREADS=ALL_CPUS")
mosaic_rasters()
print("--- Rasters Mosaicked! ---")

#Upload mosaicked raster to the corresponding folder on the AWS s3 bucket
print("--- Beginning Upload ---")
def upload_mosaic():
    my_bucket = s3.Bucket('formulations-dev')
    object_name = uploadprefix + os.path.basename(output_mosaic)
    my_bucket.upload_file(output_mosaic, object_name)
upload_mosaic()
    
print("--- Upload Complete ---")

# Remove all .xml and .tif files
print("--- Cleaning Up Files ---")
cleandir = wd
files_in_directory = os.listdir(cleandir)
filtered_files = [file for file in files_in_directory if file.endswith(".tif")]
for file in filtered_files:
	path_to_file = os.path.join(cleandir, file)
	os.remove(path_to_file)
    
files_in_directory = os.listdir(cleandir)
filtered_files = [file for file in files_in_directory if file.endswith(".xml")]
for file in filtered_files:
	path_to_file = os.path.join(cleandir, file)
	os.remove(path_to_file)
    
print("--- 241 Done ---")

print("--- Beginning 249 ---")

# Let's use Amazon S3
s3 = boto3.resource('s3')
print("[INFO:] Connecting to cloud")

formdev = s3.Bucket('formulations-dev')

# prefix to be changed per timestamp
prefix = 'spatial-grids/GLASS/' + attribute + '_raw/' + attribute + '_' + year + '_249'

# final upload prefix
uploadprefix = 'spatial-grids/GLASS/' + attribute + '_mosaic/'

output_mosaic = wd + attribute + '_' + year + '_249.tif'

print("--- Filelist from AWS: ---")
# S3 list all keys with the prefix 'spatial-grids/GLASS/' + attribute + '_raw/'
for formdev in s3.buckets.all():
    for obj in formdev.objects.filter(Prefix=prefix):
        print('{0}:{1}'.format(formdev.name, obj.key))

# Download all objects in a bucket by given prefix (timestamp in this case)
print("--- Beginning Download ---")        
def download_timestamp():
    my_bucket = s3.Bucket('formulations-dev')
    objects = my_bucket.objects.filter(Prefix=prefix)
    for obj in objects:
        path, filename = os.path.split(obj.key)        
        my_bucket.download_file(obj.key, filename)     
download_timestamp()

print("--- Download Complete! ---")  

# Mosaic rasters and save output as Cloud-optimized Geotiff
print("--- Beginning Mosaic ---")
def mosaic_rasters():
    files_to_mosaic=glob.glob(wd+'*.tif')
    files_to_mosaic

    gdal.Warp(output_mosaic, files_to_mosaic, format="COG", options="-overwrite -multi -wm 80% -t_srs EPSG:5070 -co TILED=YES -co BIGTIFF=YES -co COMPRESS=DEFLATE -co NUM_THREADS=ALL_CPUS")
mosaic_rasters()
print("--- Rasters Mosaicked! ---")

#Upload mosaicked raster to the corresponding folder on the AWS s3 bucket
print("--- Beginning Upload ---")
def upload_mosaic():
    my_bucket = s3.Bucket('formulations-dev')
    object_name = uploadprefix + os.path.basename(output_mosaic)
    my_bucket.upload_file(output_mosaic, object_name)
upload_mosaic()
    
print("--- Upload Complete ---")

# Remove all .xml and .tif files
print("--- Cleaning Up Files ---")
cleandir = wd
files_in_directory = os.listdir(cleandir)
filtered_files = [file for file in files_in_directory if file.endswith(".tif")]
for file in filtered_files:
	path_to_file = os.path.join(cleandir, file)
	os.remove(path_to_file)
    
files_in_directory = os.listdir(cleandir)
filtered_files = [file for file in files_in_directory if file.endswith(".xml")]
for file in filtered_files:
	path_to_file = os.path.join(cleandir, file)
	os.remove(path_to_file)
    
print("--- 249 Done ---")

print("--- Beginning 257 ---")

# Let's use Amazon S3
s3 = boto3.resource('s3')
print("[INFO:] Connecting to cloud")

formdev = s3.Bucket('formulations-dev')

# prefix to be changed per timestamp
prefix = 'spatial-grids/GLASS/' + attribute + '_raw/' + attribute + '_' + year + '_257'

# final upload prefix
uploadprefix = 'spatial-grids/GLASS/' + attribute + '_mosaic/'

output_mosaic = wd + attribute + '_' + year + '_257.tif'

print("--- Filelist from AWS: ---")
# S3 list all keys with the prefix 'spatial-grids/GLASS/' + attribute + '_raw/'
for formdev in s3.buckets.all():
    for obj in formdev.objects.filter(Prefix=prefix):
        print('{0}:{1}'.format(formdev.name, obj.key))

# Download all objects in a bucket by given prefix (timestamp in this case)
print("--- Beginning Download ---")        
def download_timestamp():
    my_bucket = s3.Bucket('formulations-dev')
    objects = my_bucket.objects.filter(Prefix=prefix)
    for obj in objects:
        path, filename = os.path.split(obj.key)        
        my_bucket.download_file(obj.key, filename)     
download_timestamp()

print("--- Download Complete! ---")  

# Mosaic rasters and save output as Cloud-optimized Geotiff
print("--- Beginning Mosaic ---")
def mosaic_rasters():
    files_to_mosaic=glob.glob(wd+'*.tif')
    files_to_mosaic

    gdal.Warp(output_mosaic, files_to_mosaic, format="COG", options="-overwrite -multi -wm 80% -t_srs EPSG:5070 -co TILED=YES -co BIGTIFF=YES -co COMPRESS=DEFLATE -co NUM_THREADS=ALL_CPUS")
mosaic_rasters()
print("--- Rasters Mosaicked! ---")

#Upload mosaicked raster to the corresponding folder on the AWS s3 bucket
print("--- Beginning Upload ---")
def upload_mosaic():
    my_bucket = s3.Bucket('formulations-dev')
    object_name = uploadprefix + os.path.basename(output_mosaic)
    my_bucket.upload_file(output_mosaic, object_name)
upload_mosaic()
    
print("--- Upload Complete ---")

# Remove all .xml and .tif files
print("--- Cleaning Up Files ---")
cleandir = wd
files_in_directory = os.listdir(cleandir)
filtered_files = [file for file in files_in_directory if file.endswith(".tif")]
for file in filtered_files:
	path_to_file = os.path.join(cleandir, file)
	os.remove(path_to_file)
    
files_in_directory = os.listdir(cleandir)
filtered_files = [file for file in files_in_directory if file.endswith(".xml")]
for file in filtered_files:
	path_to_file = os.path.join(cleandir, file)
	os.remove(path_to_file)
    
print("--- 257 Done ---")

print("--- Beginning 265 ---")

# Let's use Amazon S3
s3 = boto3.resource('s3')
print("[INFO:] Connecting to cloud")

formdev = s3.Bucket('formulations-dev')

# prefix to be changed per timestamp
prefix = 'spatial-grids/GLASS/' + attribute + '_raw/' + attribute + '_' + year + '_265'

# final upload prefix
uploadprefix = 'spatial-grids/GLASS/' + attribute + '_mosaic/'

output_mosaic = wd + attribute + '_' + year + '_265.tif'

print("--- Filelist from AWS: ---")
# S3 list all keys with the prefix 'spatial-grids/GLASS/' + attribute + '_raw/'
for formdev in s3.buckets.all():
    for obj in formdev.objects.filter(Prefix=prefix):
        print('{0}:{1}'.format(formdev.name, obj.key))

# Download all objects in a bucket by given prefix (timestamp in this case)
print("--- Beginning Download ---")        
def download_timestamp():
    my_bucket = s3.Bucket('formulations-dev')
    objects = my_bucket.objects.filter(Prefix=prefix)
    for obj in objects:
        path, filename = os.path.split(obj.key)        
        my_bucket.download_file(obj.key, filename)     
download_timestamp()

print("--- Download Complete! ---")  

# Mosaic rasters and save output as Cloud-optimized Geotiff
print("--- Beginning Mosaic ---")
def mosaic_rasters():
    files_to_mosaic=glob.glob(wd+'*.tif')
    files_to_mosaic

    gdal.Warp(output_mosaic, files_to_mosaic, format="COG", options="-overwrite -multi -wm 80% -t_srs EPSG:5070 -co TILED=YES -co BIGTIFF=YES -co COMPRESS=DEFLATE -co NUM_THREADS=ALL_CPUS")
mosaic_rasters()
print("--- Rasters Mosaicked! ---")

#Upload mosaicked raster to the corresponding folder on the AWS s3 bucket
print("--- Beginning Upload ---")
def upload_mosaic():
    my_bucket = s3.Bucket('formulations-dev')
    object_name = uploadprefix + os.path.basename(output_mosaic)
    my_bucket.upload_file(output_mosaic, object_name)
upload_mosaic()
    
print("--- Upload Complete ---")

# Remove all .xml and .tif files
print("--- Cleaning Up Files ---")
cleandir = wd
files_in_directory = os.listdir(cleandir)
filtered_files = [file for file in files_in_directory if file.endswith(".tif")]
for file in filtered_files:
	path_to_file = os.path.join(cleandir, file)
	os.remove(path_to_file)
    
files_in_directory = os.listdir(cleandir)
filtered_files = [file for file in files_in_directory if file.endswith(".xml")]
for file in filtered_files:
	path_to_file = os.path.join(cleandir, file)
	os.remove(path_to_file)
    
print("--- 265 Done ---")

print("--- Beginning 273 ---")

# Let's use Amazon S3
s3 = boto3.resource('s3')
print("[INFO:] Connecting to cloud")

formdev = s3.Bucket('formulations-dev')

# prefix to be changed per timestamp
prefix = 'spatial-grids/GLASS/' + attribute + '_raw/' + attribute + '_' + year + '_273'

# final upload prefix
uploadprefix = 'spatial-grids/GLASS/' + attribute + '_mosaic/'

output_mosaic = wd + attribute + '_' + year + '_273.tif'

print("--- Filelist from AWS: ---")
# S3 list all keys with the prefix 'spatial-grids/GLASS/' + attribute + '_raw/'
for formdev in s3.buckets.all():
    for obj in formdev.objects.filter(Prefix=prefix):
        print('{0}:{1}'.format(formdev.name, obj.key))

# Download all objects in a bucket by given prefix (timestamp in this case)
print("--- Beginning Download ---")        
def download_timestamp():
    my_bucket = s3.Bucket('formulations-dev')
    objects = my_bucket.objects.filter(Prefix=prefix)
    for obj in objects:
        path, filename = os.path.split(obj.key)        
        my_bucket.download_file(obj.key, filename)     
download_timestamp()

print("--- Download Complete! ---")  

# Mosaic rasters and save output as Cloud-optimized Geotiff
print("--- Beginning Mosaic ---")
def mosaic_rasters():
    files_to_mosaic=glob.glob(wd+'*.tif')
    files_to_mosaic

    gdal.Warp(output_mosaic, files_to_mosaic, format="COG", options="-overwrite -multi -wm 80% -t_srs EPSG:5070 -co TILED=YES -co BIGTIFF=YES -co COMPRESS=DEFLATE -co NUM_THREADS=ALL_CPUS")
mosaic_rasters()
print("--- Rasters Mosaicked! ---")

#Upload mosaicked raster to the corresponding folder on the AWS s3 bucket
print("--- Beginning Upload ---")
def upload_mosaic():
    my_bucket = s3.Bucket('formulations-dev')
    object_name = uploadprefix + os.path.basename(output_mosaic)
    my_bucket.upload_file(output_mosaic, object_name)
upload_mosaic()
    
print("--- Upload Complete ---")

# Remove all .xml and .tif files
print("--- Cleaning Up Files ---")
cleandir = wd
files_in_directory = os.listdir(cleandir)
filtered_files = [file for file in files_in_directory if file.endswith(".tif")]
for file in filtered_files:
	path_to_file = os.path.join(cleandir, file)
	os.remove(path_to_file)
    
files_in_directory = os.listdir(cleandir)
filtered_files = [file for file in files_in_directory if file.endswith(".xml")]
for file in filtered_files:
	path_to_file = os.path.join(cleandir, file)
	os.remove(path_to_file)
    
print("--- 273 Done ---")

print("--- Beginning 281 ---")

# Let's use Amazon S3
s3 = boto3.resource('s3')
print("[INFO:] Connecting to cloud")

formdev = s3.Bucket('formulations-dev')

# prefix to be changed per timestamp
prefix = 'spatial-grids/GLASS/' + attribute + '_raw/' + attribute + '_' + year + '_281'

# final upload prefix
uploadprefix = 'spatial-grids/GLASS/' + attribute + '_mosaic/'

output_mosaic = wd + attribute + '_' + year + '_281.tif'

print("--- Filelist from AWS: ---")
# S3 list all keys with the prefix 'spatial-grids/GLASS/' + attribute + '_raw/'
for formdev in s3.buckets.all():
    for obj in formdev.objects.filter(Prefix=prefix):
        print('{0}:{1}'.format(formdev.name, obj.key))

# Download all objects in a bucket by given prefix (timestamp in this case)
print("--- Beginning Download ---")        
def download_timestamp():
    my_bucket = s3.Bucket('formulations-dev')
    objects = my_bucket.objects.filter(Prefix=prefix)
    for obj in objects:
        path, filename = os.path.split(obj.key)        
        my_bucket.download_file(obj.key, filename)     
download_timestamp()

print("--- Download Complete! ---")  

# Mosaic rasters and save output as Cloud-optimized Geotiff
print("--- Beginning Mosaic ---")
def mosaic_rasters():
    files_to_mosaic=glob.glob(wd+'*.tif')
    files_to_mosaic

    gdal.Warp(output_mosaic, files_to_mosaic, format="COG", options="-overwrite -multi -wm 80% -t_srs EPSG:5070 -co TILED=YES -co BIGTIFF=YES -co COMPRESS=DEFLATE -co NUM_THREADS=ALL_CPUS")
mosaic_rasters()
print("--- Rasters Mosaicked! ---")

#Upload mosaicked raster to the corresponding folder on the AWS s3 bucket
print("--- Beginning Upload ---")
def upload_mosaic():
    my_bucket = s3.Bucket('formulations-dev')
    object_name = uploadprefix + os.path.basename(output_mosaic)
    my_bucket.upload_file(output_mosaic, object_name)
upload_mosaic()
    
print("--- Upload Complete ---")

# Remove all .xml and .tif files
print("--- Cleaning Up Files ---")
cleandir = wd
files_in_directory = os.listdir(cleandir)
filtered_files = [file for file in files_in_directory if file.endswith(".tif")]
for file in filtered_files:
	path_to_file = os.path.join(cleandir, file)
	os.remove(path_to_file)
    
files_in_directory = os.listdir(cleandir)
filtered_files = [file for file in files_in_directory if file.endswith(".xml")]
for file in filtered_files:
	path_to_file = os.path.join(cleandir, file)
	os.remove(path_to_file)
    
print("--- 281 Done ---")

print("--- Beginning 289 ---")

# Let's use Amazon S3
s3 = boto3.resource('s3')
print("[INFO:] Connecting to cloud")

formdev = s3.Bucket('formulations-dev')

# prefix to be changed per timestamp
prefix = 'spatial-grids/GLASS/' + attribute + '_raw/' + attribute + '_' + year + '_289'

# final upload prefix
uploadprefix = 'spatial-grids/GLASS/' + attribute + '_mosaic/'

output_mosaic = wd + attribute + '_' + year + '_289.tif'

print("--- Filelist from AWS: ---")
# S3 list all keys with the prefix 'spatial-grids/GLASS/' + attribute + '_raw/'
for formdev in s3.buckets.all():
    for obj in formdev.objects.filter(Prefix=prefix):
        print('{0}:{1}'.format(formdev.name, obj.key))

# Download all objects in a bucket by given prefix (timestamp in this case)
print("--- Beginning Download ---")        
def download_timestamp():
    my_bucket = s3.Bucket('formulations-dev')
    objects = my_bucket.objects.filter(Prefix=prefix)
    for obj in objects:
        path, filename = os.path.split(obj.key)        
        my_bucket.download_file(obj.key, filename)     
download_timestamp()

print("--- Download Complete! ---")  

# Mosaic rasters and save output as Cloud-optimized Geotiff
print("--- Beginning Mosaic ---")
def mosaic_rasters():
    files_to_mosaic=glob.glob(wd+'*.tif')
    files_to_mosaic

    gdal.Warp(output_mosaic, files_to_mosaic, format="COG", options="-overwrite -multi -wm 80% -t_srs EPSG:5070 -co TILED=YES -co BIGTIFF=YES -co COMPRESS=DEFLATE -co NUM_THREADS=ALL_CPUS")
mosaic_rasters()
print("--- Rasters Mosaicked! ---")

#Upload mosaicked raster to the corresponding folder on the AWS s3 bucket
print("--- Beginning Upload ---")
def upload_mosaic():
    my_bucket = s3.Bucket('formulations-dev')
    object_name = uploadprefix + os.path.basename(output_mosaic)
    my_bucket.upload_file(output_mosaic, object_name)
upload_mosaic()
    
print("--- Upload Complete ---")

# Remove all .xml and .tif files
print("--- Cleaning Up Files ---")
cleandir = wd
files_in_directory = os.listdir(cleandir)
filtered_files = [file for file in files_in_directory if file.endswith(".tif")]
for file in filtered_files:
	path_to_file = os.path.join(cleandir, file)
	os.remove(path_to_file)
    
files_in_directory = os.listdir(cleandir)
filtered_files = [file for file in files_in_directory if file.endswith(".xml")]
for file in filtered_files:
	path_to_file = os.path.join(cleandir, file)
	os.remove(path_to_file)
    
print("--- 289 Done ---")

print("--- Beginning 297 ---")

# Let's use Amazon S3
s3 = boto3.resource('s3')
print("[INFO:] Connecting to cloud")

formdev = s3.Bucket('formulations-dev')

# prefix to be changed per timestamp
prefix = 'spatial-grids/GLASS/' + attribute + '_raw/' + attribute + '_' + year + '_297'

# final upload prefix
uploadprefix = 'spatial-grids/GLASS/' + attribute + '_mosaic/'

output_mosaic = wd + attribute + '_' + year + '_297.tif'

print("--- Filelist from AWS: ---")
# S3 list all keys with the prefix 'spatial-grids/GLASS/' + attribute + '_raw/'
for formdev in s3.buckets.all():
    for obj in formdev.objects.filter(Prefix=prefix):
        print('{0}:{1}'.format(formdev.name, obj.key))

# Download all objects in a bucket by given prefix (timestamp in this case)
print("--- Beginning Download ---")        
def download_timestamp():
    my_bucket = s3.Bucket('formulations-dev')
    objects = my_bucket.objects.filter(Prefix=prefix)
    for obj in objects:
        path, filename = os.path.split(obj.key)        
        my_bucket.download_file(obj.key, filename)     
download_timestamp()

print("--- Download Complete! ---")  

# Mosaic rasters and save output as Cloud-optimized Geotiff
print("--- Beginning Mosaic ---")
def mosaic_rasters():
    files_to_mosaic=glob.glob(wd+'*.tif')
    files_to_mosaic

    gdal.Warp(output_mosaic, files_to_mosaic, format="COG", options="-overwrite -multi -wm 80% -t_srs EPSG:5070 -co TILED=YES -co BIGTIFF=YES -co COMPRESS=DEFLATE -co NUM_THREADS=ALL_CPUS")
mosaic_rasters()
print("--- Rasters Mosaicked! ---")

#Upload mosaicked raster to the corresponding folder on the AWS s3 bucket
print("--- Beginning Upload ---")
def upload_mosaic():
    my_bucket = s3.Bucket('formulations-dev')
    object_name = uploadprefix + os.path.basename(output_mosaic)
    my_bucket.upload_file(output_mosaic, object_name)
upload_mosaic()
    
print("--- Upload Complete ---")

# Remove all .xml and .tif files
print("--- Cleaning Up Files ---")
cleandir = wd
files_in_directory = os.listdir(cleandir)
filtered_files = [file for file in files_in_directory if file.endswith(".tif")]
for file in filtered_files:
	path_to_file = os.path.join(cleandir, file)
	os.remove(path_to_file)
    
files_in_directory = os.listdir(cleandir)
filtered_files = [file for file in files_in_directory if file.endswith(".xml")]
for file in filtered_files:
	path_to_file = os.path.join(cleandir, file)
	os.remove(path_to_file)
    
print("--- 297 Done ---")

print("--- Beginning 305 ---")

# Let's use Amazon S3
s3 = boto3.resource('s3')
print("[INFO:] Connecting to cloud")

formdev = s3.Bucket('formulations-dev')

# prefix to be changed per timestamp
prefix = 'spatial-grids/GLASS/' + attribute + '_raw/' + attribute + '_' + year + '_305'

# final upload prefix
uploadprefix = 'spatial-grids/GLASS/' + attribute + '_mosaic/'

output_mosaic = wd + attribute + '_' + year + '_305.tif'

print("--- Filelist from AWS: ---")
# S3 list all keys with the prefix 'spatial-grids/GLASS/' + attribute + '_raw/'
for formdev in s3.buckets.all():
    for obj in formdev.objects.filter(Prefix=prefix):
        print('{0}:{1}'.format(formdev.name, obj.key))

# Download all objects in a bucket by given prefix (timestamp in this case)
print("--- Beginning Download ---")        
def download_timestamp():
    my_bucket = s3.Bucket('formulations-dev')
    objects = my_bucket.objects.filter(Prefix=prefix)
    for obj in objects:
        path, filename = os.path.split(obj.key)        
        my_bucket.download_file(obj.key, filename)     
download_timestamp()

print("--- Download Complete! ---")  

# Mosaic rasters and save output as Cloud-optimized Geotiff
print("--- Beginning Mosaic ---")
def mosaic_rasters():
    files_to_mosaic=glob.glob(wd+'*.tif')
    files_to_mosaic

    gdal.Warp(output_mosaic, files_to_mosaic, format="COG", options="-overwrite -multi -wm 80% -t_srs EPSG:5070 -co TILED=YES -co BIGTIFF=YES -co COMPRESS=DEFLATE -co NUM_THREADS=ALL_CPUS")
mosaic_rasters()
print("--- Rasters Mosaicked! ---")

#Upload mosaicked raster to the corresponding folder on the AWS s3 bucket
print("--- Beginning Upload ---")
def upload_mosaic():
    my_bucket = s3.Bucket('formulations-dev')
    object_name = uploadprefix + os.path.basename(output_mosaic)
    my_bucket.upload_file(output_mosaic, object_name)
upload_mosaic()
    
print("--- Upload Complete ---")

# Remove all .xml and .tif files
print("--- Cleaning Up Files ---")
cleandir = wd
files_in_directory = os.listdir(cleandir)
filtered_files = [file for file in files_in_directory if file.endswith(".tif")]
for file in filtered_files:
	path_to_file = os.path.join(cleandir, file)
	os.remove(path_to_file)
    
files_in_directory = os.listdir(cleandir)
filtered_files = [file for file in files_in_directory if file.endswith(".xml")]
for file in filtered_files:
	path_to_file = os.path.join(cleandir, file)
	os.remove(path_to_file)
    
print("--- 305 Done ---")

print("--- Beginning 313 ---")

# Let's use Amazon S3
s3 = boto3.resource('s3')
print("[INFO:] Connecting to cloud")

formdev = s3.Bucket('formulations-dev')

# prefix to be changed per timestamp
prefix = 'spatial-grids/GLASS/' + attribute + '_raw/' + attribute + '_' + year + '_313'

# final upload prefix
uploadprefix = 'spatial-grids/GLASS/' + attribute + '_mosaic/'

output_mosaic = wd + attribute + '_' + year + '_313.tif'

print("--- Filelist from AWS: ---")
# S3 list all keys with the prefix 'spatial-grids/GLASS/' + attribute + '_raw/'
for formdev in s3.buckets.all():
    for obj in formdev.objects.filter(Prefix=prefix):
        print('{0}:{1}'.format(formdev.name, obj.key))

# Download all objects in a bucket by given prefix (timestamp in this case)
print("--- Beginning Download ---")        
def download_timestamp():
    my_bucket = s3.Bucket('formulations-dev')
    objects = my_bucket.objects.filter(Prefix=prefix)
    for obj in objects:
        path, filename = os.path.split(obj.key)        
        my_bucket.download_file(obj.key, filename)     
download_timestamp()

print("--- Download Complete! ---")  

# Mosaic rasters and save output as Cloud-optimized Geotiff
print("--- Beginning Mosaic ---")
def mosaic_rasters():
    files_to_mosaic=glob.glob(wd+'*.tif')
    files_to_mosaic

    gdal.Warp(output_mosaic, files_to_mosaic, format="COG", options="-overwrite -multi -wm 80% -t_srs EPSG:5070 -co TILED=YES -co BIGTIFF=YES -co COMPRESS=DEFLATE -co NUM_THREADS=ALL_CPUS")
mosaic_rasters()
print("--- Rasters Mosaicked! ---")

#Upload mosaicked raster to the corresponding folder on the AWS s3 bucket
print("--- Beginning Upload ---")
def upload_mosaic():
    my_bucket = s3.Bucket('formulations-dev')
    object_name = uploadprefix + os.path.basename(output_mosaic)
    my_bucket.upload_file(output_mosaic, object_name)
upload_mosaic()
    
print("--- Upload Complete ---")

# Remove all .xml and .tif files
print("--- Cleaning Up Files ---")
cleandir = wd
files_in_directory = os.listdir(cleandir)
filtered_files = [file for file in files_in_directory if file.endswith(".tif")]
for file in filtered_files:
	path_to_file = os.path.join(cleandir, file)
	os.remove(path_to_file)
    
files_in_directory = os.listdir(cleandir)
filtered_files = [file for file in files_in_directory if file.endswith(".xml")]
for file in filtered_files:
	path_to_file = os.path.join(cleandir, file)
	os.remove(path_to_file)
    
print("--- 313 Done ---")

print("--- Beginning 321 ---")

# Let's use Amazon S3
s3 = boto3.resource('s3')
print("[INFO:] Connecting to cloud")

formdev = s3.Bucket('formulations-dev')

# prefix to be changed per timestamp
prefix = 'spatial-grids/GLASS/' + attribute + '_raw/' + attribute + '_' + year + '_321'

# final upload prefix
uploadprefix = 'spatial-grids/GLASS/' + attribute + '_mosaic/'

output_mosaic = wd + attribute + '_' + year + '_321.tif'

print("--- Filelist from AWS: ---")
# S3 list all keys with the prefix 'spatial-grids/GLASS/' + attribute + '_raw/'
for formdev in s3.buckets.all():
    for obj in formdev.objects.filter(Prefix=prefix):
        print('{0}:{1}'.format(formdev.name, obj.key))

# Download all objects in a bucket by given prefix (timestamp in this case)
print("--- Beginning Download ---")        
def download_timestamp():
    my_bucket = s3.Bucket('formulations-dev')
    objects = my_bucket.objects.filter(Prefix=prefix)
    for obj in objects:
        path, filename = os.path.split(obj.key)        
        my_bucket.download_file(obj.key, filename)     
download_timestamp()

print("--- Download Complete! ---")  

# Mosaic rasters and save output as Cloud-optimized Geotiff
print("--- Beginning Mosaic ---")
def mosaic_rasters():
    files_to_mosaic=glob.glob(wd+'*.tif')
    files_to_mosaic

    gdal.Warp(output_mosaic, files_to_mosaic, format="COG", options="-overwrite -multi -wm 80% -t_srs EPSG:5070 -co TILED=YES -co BIGTIFF=YES -co COMPRESS=DEFLATE -co NUM_THREADS=ALL_CPUS")
mosaic_rasters()
print("--- Rasters Mosaicked! ---")

#Upload mosaicked raster to the corresponding folder on the AWS s3 bucket
print("--- Beginning Upload ---")
def upload_mosaic():
    my_bucket = s3.Bucket('formulations-dev')
    object_name = uploadprefix + os.path.basename(output_mosaic)
    my_bucket.upload_file(output_mosaic, object_name)
upload_mosaic()
    
print("--- Upload Complete ---")

# Remove all .xml and .tif files
print("--- Cleaning Up Files ---")
cleandir = wd
files_in_directory = os.listdir(cleandir)
filtered_files = [file for file in files_in_directory if file.endswith(".tif")]
for file in filtered_files:
	path_to_file = os.path.join(cleandir, file)
	os.remove(path_to_file)
    
files_in_directory = os.listdir(cleandir)
filtered_files = [file for file in files_in_directory if file.endswith(".xml")]
for file in filtered_files:
	path_to_file = os.path.join(cleandir, file)
	os.remove(path_to_file)
    
print("--- 321 Done ---")

print("--- Beginning 329 ---")

# Let's use Amazon S3
s3 = boto3.resource('s3')
print("[INFO:] Connecting to cloud")

formdev = s3.Bucket('formulations-dev')

# prefix to be changed per timestamp
prefix = 'spatial-grids/GLASS/' + attribute + '_raw/' + attribute + '_' + year + '_329'

# final upload prefix
uploadprefix = 'spatial-grids/GLASS/' + attribute + '_mosaic/'

output_mosaic = wd + attribute + '_' + year + '_329.tif'

print("--- Filelist from AWS: ---")
# S3 list all keys with the prefix 'spatial-grids/GLASS/' + attribute + '_raw/'
for formdev in s3.buckets.all():
    for obj in formdev.objects.filter(Prefix=prefix):
        print('{0}:{1}'.format(formdev.name, obj.key))

# Download all objects in a bucket by given prefix (timestamp in this case)
print("--- Beginning Download ---")        
def download_timestamp():
    my_bucket = s3.Bucket('formulations-dev')
    objects = my_bucket.objects.filter(Prefix=prefix)
    for obj in objects:
        path, filename = os.path.split(obj.key)        
        my_bucket.download_file(obj.key, filename)     
download_timestamp()

print("--- Download Complete! ---")  

# Mosaic rasters and save output as Cloud-optimized Geotiff
print("--- Beginning Mosaic ---")
def mosaic_rasters():
    files_to_mosaic=glob.glob(wd+'*.tif')
    files_to_mosaic

    gdal.Warp(output_mosaic, files_to_mosaic, format="COG", options="-overwrite -multi -wm 80% -t_srs EPSG:5070 -co TILED=YES -co BIGTIFF=YES -co COMPRESS=DEFLATE -co NUM_THREADS=ALL_CPUS")
mosaic_rasters()
print("--- Rasters Mosaicked! ---")

#Upload mosaicked raster to the corresponding folder on the AWS s3 bucket
print("--- Beginning Upload ---")
def upload_mosaic():
    my_bucket = s3.Bucket('formulations-dev')
    object_name = uploadprefix + os.path.basename(output_mosaic)
    my_bucket.upload_file(output_mosaic, object_name)
upload_mosaic()
    
print("--- Upload Complete ---")

# Remove all .xml and .tif files
print("--- Cleaning Up Files ---")
cleandir = wd
files_in_directory = os.listdir(cleandir)
filtered_files = [file for file in files_in_directory if file.endswith(".tif")]
for file in filtered_files:
	path_to_file = os.path.join(cleandir, file)
	os.remove(path_to_file)
    
files_in_directory = os.listdir(cleandir)
filtered_files = [file for file in files_in_directory if file.endswith(".xml")]
for file in filtered_files:
	path_to_file = os.path.join(cleandir, file)
	os.remove(path_to_file)
    
print("--- 329 Done ---")

print("--- Beginning 337 ---")

# Let's use Amazon S3
s3 = boto3.resource('s3')
print("[INFO:] Connecting to cloud")

formdev = s3.Bucket('formulations-dev')

# prefix to be changed per timestamp
prefix = 'spatial-grids/GLASS/' + attribute + '_raw/' + attribute + '_' + year + '_337'

# final upload prefix
uploadprefix = 'spatial-grids/GLASS/' + attribute + '_mosaic/'

output_mosaic = wd + attribute + '_' + year + '_337.tif'

print("--- Filelist from AWS: ---")
# S3 list all keys with the prefix 'spatial-grids/GLASS/' + attribute + '_raw/'
for formdev in s3.buckets.all():
    for obj in formdev.objects.filter(Prefix=prefix):
        print('{0}:{1}'.format(formdev.name, obj.key))

# Download all objects in a bucket by given prefix (timestamp in this case)
print("--- Beginning Download ---")        
def download_timestamp():
    my_bucket = s3.Bucket('formulations-dev')
    objects = my_bucket.objects.filter(Prefix=prefix)
    for obj in objects:
        path, filename = os.path.split(obj.key)        
        my_bucket.download_file(obj.key, filename)     
download_timestamp()

print("--- Download Complete! ---")  

# Mosaic rasters and save output as Cloud-optimized Geotiff
print("--- Beginning Mosaic ---")
def mosaic_rasters():
    files_to_mosaic=glob.glob(wd+'*.tif')
    files_to_mosaic

    gdal.Warp(output_mosaic, files_to_mosaic, format="COG", options="-overwrite -multi -wm 80% -t_srs EPSG:5070 -co TILED=YES -co BIGTIFF=YES -co COMPRESS=DEFLATE -co NUM_THREADS=ALL_CPUS")
mosaic_rasters()
print("--- Rasters Mosaicked! ---")

#Upload mosaicked raster to the corresponding folder on the AWS s3 bucket
print("--- Beginning Upload ---")
def upload_mosaic():
    my_bucket = s3.Bucket('formulations-dev')
    object_name = uploadprefix + os.path.basename(output_mosaic)
    my_bucket.upload_file(output_mosaic, object_name)
upload_mosaic()
    
print("--- Upload Complete ---")

# Remove all .xml and .tif files
print("--- Cleaning Up Files ---")
cleandir = wd
files_in_directory = os.listdir(cleandir)
filtered_files = [file for file in files_in_directory if file.endswith(".tif")]
for file in filtered_files:
	path_to_file = os.path.join(cleandir, file)
	os.remove(path_to_file)
    
files_in_directory = os.listdir(cleandir)
filtered_files = [file for file in files_in_directory if file.endswith(".xml")]
for file in filtered_files:
	path_to_file = os.path.join(cleandir, file)
	os.remove(path_to_file)
    
print("--- 337 Done ---")

print("--- Beginning 345 ---")

# Let's use Amazon S3
s3 = boto3.resource('s3')
print("[INFO:] Connecting to cloud")

formdev = s3.Bucket('formulations-dev')

# prefix to be changed per timestamp
prefix = 'spatial-grids/GLASS/' + attribute + '_raw/' + attribute + '_' + year + '_345'

# final upload prefix
uploadprefix = 'spatial-grids/GLASS/' + attribute + '_mosaic/'

output_mosaic = wd + attribute + '_' + year + '_345.tif'

print("--- Filelist from AWS: ---")
# S3 list all keys with the prefix 'spatial-grids/GLASS/' + attribute + '_raw/'
for formdev in s3.buckets.all():
    for obj in formdev.objects.filter(Prefix=prefix):
        print('{0}:{1}'.format(formdev.name, obj.key))

# Download all objects in a bucket by given prefix (timestamp in this case)
print("--- Beginning Download ---")        
def download_timestamp():
    my_bucket = s3.Bucket('formulations-dev')
    objects = my_bucket.objects.filter(Prefix=prefix)
    for obj in objects:
        path, filename = os.path.split(obj.key)        
        my_bucket.download_file(obj.key, filename)     
download_timestamp()

print("--- Download Complete! ---")  

# Mosaic rasters and save output as Cloud-optimized Geotiff
print("--- Beginning Mosaic ---")
def mosaic_rasters():
    files_to_mosaic=glob.glob(wd+'*.tif')
    files_to_mosaic

    gdal.Warp(output_mosaic, files_to_mosaic, format="COG", options="-overwrite -multi -wm 80% -t_srs EPSG:5070 -co TILED=YES -co BIGTIFF=YES -co COMPRESS=DEFLATE -co NUM_THREADS=ALL_CPUS")
mosaic_rasters()
print("--- Rasters Mosaicked! ---")

#Upload mosaicked raster to the corresponding folder on the AWS s3 bucket
print("--- Beginning Upload ---")
def upload_mosaic():
    my_bucket = s3.Bucket('formulations-dev')
    object_name = uploadprefix + os.path.basename(output_mosaic)
    my_bucket.upload_file(output_mosaic, object_name)
upload_mosaic()
    
print("--- Upload Complete ---")

# Remove all .xml and .tif files
print("--- Cleaning Up Files ---")
cleandir = wd
files_in_directory = os.listdir(cleandir)
filtered_files = [file for file in files_in_directory if file.endswith(".tif")]
for file in filtered_files:
	path_to_file = os.path.join(cleandir, file)
	os.remove(path_to_file)
    
files_in_directory = os.listdir(cleandir)
filtered_files = [file for file in files_in_directory if file.endswith(".xml")]
for file in filtered_files:
	path_to_file = os.path.join(cleandir, file)
	os.remove(path_to_file)
    
print("--- 345 Done ---")

print("--- Beginning 353 ---")

# Let's use Amazon S3
s3 = boto3.resource('s3')
print("[INFO:] Connecting to cloud")

formdev = s3.Bucket('formulations-dev')

# prefix to be changed per timestamp
prefix = 'spatial-grids/GLASS/' + attribute + '_raw/' + attribute + '_' + year + '_353'

# final upload prefix
uploadprefix = 'spatial-grids/GLASS/' + attribute + '_mosaic/'

output_mosaic = wd + attribute + '_' + year + '_353.tif'

print("--- Filelist from AWS: ---")
# S3 list all keys with the prefix 'spatial-grids/GLASS/' + attribute + '_raw/'
for formdev in s3.buckets.all():
    for obj in formdev.objects.filter(Prefix=prefix):
        print('{0}:{1}'.format(formdev.name, obj.key))

# Download all objects in a bucket by given prefix (timestamp in this case)
print("--- Beginning Download ---")        
def download_timestamp():
    my_bucket = s3.Bucket('formulations-dev')
    objects = my_bucket.objects.filter(Prefix=prefix)
    for obj in objects:
        path, filename = os.path.split(obj.key)        
        my_bucket.download_file(obj.key, filename)     
download_timestamp()

print("--- Download Complete! ---")  

# Mosaic rasters and save output as Cloud-optimized Geotiff
print("--- Beginning Mosaic ---")
def mosaic_rasters():
    files_to_mosaic=glob.glob(wd+'*.tif')
    files_to_mosaic

    gdal.Warp(output_mosaic, files_to_mosaic, format="COG", options="-overwrite -multi -wm 80% -t_srs EPSG:5070 -co TILED=YES -co BIGTIFF=YES -co COMPRESS=DEFLATE -co NUM_THREADS=ALL_CPUS")
mosaic_rasters()
print("--- Rasters Mosaicked! ---")

#Upload mosaicked raster to the corresponding folder on the AWS s3 bucket
print("--- Beginning Upload ---")
def upload_mosaic():
    my_bucket = s3.Bucket('formulations-dev')
    object_name = uploadprefix + os.path.basename(output_mosaic)
    my_bucket.upload_file(output_mosaic, object_name)
upload_mosaic()
    
print("--- Upload Complete ---")

# Remove all .xml and .tif files
print("--- Cleaning Up Files ---")
cleandir = wd
files_in_directory = os.listdir(cleandir)
filtered_files = [file for file in files_in_directory if file.endswith(".tif")]
for file in filtered_files:
	path_to_file = os.path.join(cleandir, file)
	os.remove(path_to_file)
    
files_in_directory = os.listdir(cleandir)
filtered_files = [file for file in files_in_directory if file.endswith(".xml")]
for file in filtered_files:
	path_to_file = os.path.join(cleandir, file)
	os.remove(path_to_file)
    
print("--- 353 Done ---")

print("--- Beginning 361 ---")

# Let's use Amazon S3
s3 = boto3.resource('s3')
print("[INFO:] Connecting to cloud")

formdev = s3.Bucket('formulations-dev')

# prefix to be changed per timestamp
prefix = 'spatial-grids/GLASS/' + attribute + '_raw/' + attribute + '_' + year + '_361'

# final upload prefix
uploadprefix = 'spatial-grids/GLASS/' + attribute + '_mosaic/'

output_mosaic = wd + attribute + '_' + year + '_361.tif'

print("--- Filelist from AWS: ---")
# S3 list all keys with the prefix 'spatial-grids/GLASS/' + attribute + '_raw/'
for formdev in s3.buckets.all():
    for obj in formdev.objects.filter(Prefix=prefix):
        print('{0}:{1}'.format(formdev.name, obj.key))

# Download all objects in a bucket by given prefix (timestamp in this case)
print("--- Beginning Download ---")        
def download_timestamp():
    my_bucket = s3.Bucket('formulations-dev')
    objects = my_bucket.objects.filter(Prefix=prefix)
    for obj in objects:
        path, filename = os.path.split(obj.key)        
        my_bucket.download_file(obj.key, filename)     
download_timestamp()

print("--- Download Complete! ---")  

# Mosaic rasters and save output as Cloud-optimized Geotiff
print("--- Beginning Mosaic ---")
def mosaic_rasters():
    files_to_mosaic=glob.glob(wd+'*.tif')
    files_to_mosaic

    gdal.Warp(output_mosaic, files_to_mosaic, format="COG", options="-overwrite -multi -wm 80% -t_srs EPSG:5070 -co TILED=YES -co BIGTIFF=YES -co COMPRESS=DEFLATE -co NUM_THREADS=ALL_CPUS")
mosaic_rasters()
print("--- Rasters Mosaicked! ---")

#Upload mosaicked raster to the corresponding folder on the AWS s3 bucket
print("--- Beginning Upload ---")
def upload_mosaic():
    my_bucket = s3.Bucket('formulations-dev')
    object_name = uploadprefix + os.path.basename(output_mosaic)
    my_bucket.upload_file(output_mosaic, object_name)
upload_mosaic()
    
print("--- Upload Complete ---")

# Remove all .xml and .tif files
print("--- Cleaning Up Files ---")
cleandir = wd
files_in_directory = os.listdir(cleandir)
filtered_files = [file for file in files_in_directory if file.endswith(".tif")]
for file in filtered_files:
	path_to_file = os.path.join(cleandir, file)
	os.remove(path_to_file)
    
files_in_directory = os.listdir(cleandir)
filtered_files = [file for file in files_in_directory if file.endswith(".xml")]
for file in filtered_files:
	path_to_file = os.path.join(cleandir, file)
	os.remove(path_to_file)
    
print("--- 361 Done ---")