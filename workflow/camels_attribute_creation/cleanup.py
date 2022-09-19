# Author: Rich Gibbs, NOAA, NWS, Office of Water Prediction, National Water Center

import os
import subprocess

# Remove all .xml and .tif files
def del_files(cleandir):
    print("--- Cleaning Up Files ---")
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
    
    print("--- Done ---")