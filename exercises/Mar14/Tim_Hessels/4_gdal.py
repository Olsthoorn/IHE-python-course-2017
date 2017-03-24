# -*- coding: utf-8 -*-
"""
Created on Mon Mar 13 11:53:33 2017

@author: tih
"""

import gdal
import glob
import os

Input_folder = r'D:\Python_Training\CHIRPS' 
os.chdir(Input_folder)
Files = glob.glob('chirps-v2.0.*.tif')
File = Files[0]
File_name = os.path.join(Input_folder, File)
g = gdal.Open(File_name)

# Get GeoTransform and projection
GeoTransform = g.GetGeoTransform()
Proj = g.GetProjection()

# Get Data
# Open gdal data
g = gdal.Open(File_name)

# Open the data
Array = g.GetRasterBand(1).ReadAsArray()
Array[Array == 0.0] = -9999

# Define outputname
file_out = 'CHIRPS_NDVisZero.tif'
file_out_path = os.path.join(Input_folder,file_out)

# Say that you want to create a Gtiff file:
driver = gdal.GetDriverByName("GTiff")
# Define the name, shape and format of the Gtiff file
dst_ds = driver.Create(file_out_path, int(Array.shape[1]), int(Array.shape[0]), 1, gdal.GDT_Float32)
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



