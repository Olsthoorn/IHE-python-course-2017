# -*- coding: utf-8 -*-
"""
Created on Mon Mar 13 13:02:15 2017

@author: tih
"""

def Create_Tiff(name, Array, Proj, GeoTransform):

    import gdal
    
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