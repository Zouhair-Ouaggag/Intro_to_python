# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import numpy as np
from pandas import read_csv
plants = read_csv('environmental_survey/plants2017.csv')
#print(plants["Plant"=="tree"])
plants.drop(plants.index[plants.Plant == 'tree'], inplace = True)
#display(plants)

plants.reset_index(drop=True, inplace = True)
#display(plants)

def Lat_Lon(df):
    X = df["GPS_lat"]
    Y = df["GPS_lon"]
    Y = 40008000*Y/360*np.cos(np.deg2rad(X))
    X = 40075160*X/360
    df["GPS_lon"] = Y
    df["GPS_lat"] = X
    df.rename(columns={"GPS_lon":"Lon","GPS_lat":"Lat"}, inplace=True)
    
Lat_Lon(plants)
#display(plants)