# -*- coding: utf-8 -*-
"""
Created on Mon Mar 13 11:12:22 2017

@author: tih
"""

import gdal
import glob
import os

# directory to the CHIRPS data
Input_folder = r'D:\Python_Training\CHIRPS'

# Change working directory
os.chdir(Input_folder)

# Get all files in working directory ending with tiff
Files = glob.glob('chirps-v2.0.*.tif')

# Get the first tiff file
File = Files[0]

# Define the complete file name
File_name = os.path.join(Input_folder, File)

# Open gdal data
g = gdal.Open(File_name)

# Open the band
Band_data = g.GetRasterBand(1)

# Open the array
Array = Band_data.ReadAsArray()

print('Maximum Value:', Array.max())

# Limit the maximum value
Array[Array>=20.] = 20.

print('Maximum Value:', Array.max())

# set all 0 values to -9999
Array[Array==0.] = -9999.









