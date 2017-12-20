# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import numpy as np
import pandas as pd

from pandas import read_csv

"""
Importing data from plants2017 as DataFrame and removing data for trees.
"""
plants = read_csv('environmental_survey/plants2017.csv')
#print(plants["Plant"=="tree"])
plants.drop(plants.index[plants.Plant == 'tree'], inplace = True)
#display(plants)

plants.reset_index(drop=True, inplace = True)
#display(plants)

def Lat_Long(df):
    X = df["GPS_lat"]
    Y = df["GPS_lon"]
    Y = 40008000*Y/360*np.cos(np.deg2rad(X))
    X = 40075160*X/360
    df["GPS_lon"] = Y
    df["GPS_lat"] = X
    df.rename(columns={"GPS_lon":"Lon","GPS_lat":"Lat"}, inplace=True)
    
Lat_Long(plants)
#display(plants)

def Select_height(df,height=0.5):
    df.drop(df.index[df.height_m < height], inplace = True)
    df.reset_index(drop=True, inplace = True)
    
Select_height(plants)

pH = read_csv('environmental_survey/pH2017.csv')

Lat_Long(pH)

def scale(df):
    X = df["Lat"]
    Y = df["Lon"]
    X_scaled = (X-np.min(X))/(np.max(X)-np.min(X))*3000
    Y_scaled = (Y-np.min(Y))/(np.max(Y)-np.min(Y))*3000
    df["Lat"] = X_scaled
    df["Lon"] = Y_scaled
    df.rename(columns={"Lon":"X_scaled","Lat":"Y_scaled"}, inplace=True)
    df.insert(loc=1,column='x',value=X_scaled//200)
    df.insert(loc=3,column='y',value=Y_scaled//200)
     
    
    
scale(pH)



    