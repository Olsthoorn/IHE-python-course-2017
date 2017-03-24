# -*- coding: utf-8 -*-
"""
Created on Mon Mar 13 10:42:22 2017

@author: tih
"""
import pandas as pd
import os
import gdal
import glob
import numpy as np

# Functions
def Create_Tiff(name, Array, Proj, GeoTransform):
    
    # Say that you want to create a Gtiff file:
    driver = gdal.GetDriverByName("GTiff")
    # Define the name, shape and format of the Gtiff file
    dst_ds = driver.Create(name, int(Array.shape[1]), int(Array.shape[0]), 1, gdal.GDT_Float32)
    # Set projection for the new tiff file
    dst_ds.SetProjection(Proj)
    # Set the geotransform of the new tiff file
    dst_ds.SetGeoTransform(GeoTransform)
    # Set the No Data Value of the new tiff file
    dst_ds.GetRasterBand(1).SetNoDataValue(-9999)
    # Set the values of the new tiff file
    dst_ds.GetRasterBand(1).WriteArray(Array)
    # Close the tiff file
    dst_ds = None
    
    return()    

# Definitions that must be set by the user
Startdate = '2016-10-01'
Enddate = '2016-12-31'
Input_folder = r'D:\Python_Training\CHIRPS' 

# Change work directory
os.chdir(Input_folder)

# Define months
Dates = pd.date_range(Startdate,Enddate,freq='MS')

# Loop over every month
for Date in Dates:
    # Define year and month of current loop
    Year = Date.year
    Month = Date.month   
    # Find all tiff files with that specific year and month
    Files = glob.glob('*%d.%02d.*.tif' %(Year, Month))  
    
    # Create an empty array
    Array_month = np.zeros([1600,1500])
    
    # Loop over the files
    for File in Files:
        # Define File name
        File_name = os.path.join(Input_folder, File)
        # Open File name
        g = gdal.Open(File_name)
        # Get Raster data
        Array_one_day = g.GetRasterBand(1).ReadAsArray()
        # Set -9999 to 0
        Array_one_day[Array_one_day==-9999.] = 0.
        # Add daily data to monthly dataset
        Array_month += Array_one_day
    
    # Set all 0 values to the No data value
    Array_month[Array_month == 0.] = -9999
    
    # Get geotransfrom and projection
    GeoTransform = g.GetGeoTransform()
    Proj = g.GetProjection() 
        
    # Define file name    
    File_out = 'CHIRPS_monthly_%d_%02d.tif' %(Year, Month)
    File_name_out = os.path.join(Input_folder, File_out)

    # Use the function to create a tiff file
    Create_Tiff(File_name_out, Array_month, Proj, GeoTransform)
   












