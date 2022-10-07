# File Defining functions to merge StreamCats dataset by BPU
# pairs with streamCAT_merge.py
# Author : Rich Gibbs NWC, OWP, NOAA

import pandas as pd
import glob, os
import re

# function to extract region from filename and append as new column in table
def add_region(workdir, outdir, vpu):
    print("Adding VPU " + vpu)
    
    filelist = glob.glob(workdir + '*' + vpu + '.csv')
    print(filelist)

    for file in filelist:
        if file.endswith('.csv'):
            df_new = pd.read_csv(file)
            search = re.search(r'(?<=_Region)\w+', file)
            region = search.group(0)
            searchPrefix = re.search('^[^_]+(?=_)', os.path.basename(file))
            prefix = searchPrefix.group(0)
            #print(prefix)
            df_new['VPU'] = region
            #print(region)
            df = df_new.append(df_new, ignore_index=True)
            output = outdir + prefix + '_' + region + '.csv'
            df.to_csv(output, index=False)


def join_csv(workdir, vpu):
    print("Joining csvs")
    filelist = glob.glob(workdir + '*' + vpu + '.csv')
    #print(filelist)
    
    # Create a csv with a column of only COMIDs for use as a joinfile
    joinfile = pd.DataFrame(list())
    readfile = pd.read_csv(workdir + 'AgMidHiSlopes_' + vpu + '.csv')
    comid = readfile['COMID']
    joinfile['COMID'] = comid
    df = joinfile.append(joinfile)
    joinout = workdir + vpu + 'streamCAT' + '.csv'
    df.to_csv(joinout, index=False)
    
    del joinfile, readfile, comid, df
    
    # loop through filelist and merge csvs to COMID file
    for file in filelist:
        # read in csv
        file_to_join = pd.read_csv(file)  
        # read in COMID csv
        df = pd.read_csv(joinout)
        
        file_to_join.set_index('COMID')
        df.set_index('COMID')       
        
        # merge files by COMID field
        join = df.merge(file_to_join, how='left', on='COMID')
        
        # drop duplicate columns by suffix
        join.columns = join.columns.str.replace("\_.*", "", regex=True)
        
        # output array as csv
        output = workdir + vpu + 'streamCAT.csv'
        outfile = join.drop_duplicates(keep='first')
        outfile.to_csv(output, index=False)
        
        del file_to_join, df, join, outfile

# Clean and remove duplicates from merged csvs   
def prune_csv(outdir, vpu):
    csv = outdir + vpu + 'streamCAT.csv'
    outfile = outdir + vpu + 'streamCAT_test.csv'
        
    df = pd.read_csv(csv)
    
    df.columns = df.columns.str.replace(r"\..*", "", regex=True)
    
    df1 = df.reset_index().T.drop_duplicates().T
    df1.to_csv(outfile, index=False)
    
    del df, df1
    