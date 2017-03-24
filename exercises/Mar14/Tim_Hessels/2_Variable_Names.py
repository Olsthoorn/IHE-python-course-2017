# -*- coding: utf-8 -*-
"""
Created on Mon Mar 13 10:53:35 2017

@author: tih
"""
# ----------------------------- Method 1 --------------------------------
import pandas as pd

# Define the start en enddate
Startdate = '2016-12-01'
Enddate = '2016-12-31' 

# Define the daily date range
Dates = pd.date_range(Startdate, Enddate, freq = 'D')

for Date in Dates:
    Year = Date.year
    Month = Date.month
    Day = Date.day

    name_CHIRPS_tif = 'chirps-v2.0.%d.%02d.%02d.tif' %(Year, Month, Day)
    print(name_CHIRPS_tif)  
  
# ----------------------------- Show glob -------------------------------
import os
import glob

# directory to the CHIRPS data
Input_folder = r'D:\Python_Training\CHIRPS' 

# Change working directory 
os.chdir(Input_folder)

# Get all files in directory
CHIRPSAllFiles = glob.glob('*.tif')
  
# Get all files starting with chirps
CHIRPSAllFiles1 = glob.glob('chirps*')  
 
# Get all files with v2.0 in middle
CHIRPSAllFiles2 = glob.glob('*v2.0*')  
 
# Get all files ending with .gz
CHIRPSAllFiles3 = glob.glob('*.gz')  
 
 
# ----------------------------- Method 2 --------------------------------

import os
import glob

# directory to the CHIRPS data
Input_folder = r'D:\Python_Training\CHIRPS' 

# Change working directory 
os.chdir(Input_folder)

Files = glob.glob('*.tif')

for File in Files:
    print(File)





