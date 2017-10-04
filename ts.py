#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Modified on  June 29  2016

@author: andrei Kurbatov
"""
import pandas as pd
import numpy as np
np.set_printoptions(precision=3)
# Open file to output data
f_out=open('SamplesAges.txt','w')

depth = pd.read_csv('SamplesDepths.csv',
                            usecols=['depth'])
                            
#print(depth)
tsdepth = pd.read_csv('TimeScale.csv',
                            usecols=['tsdepth'])
yearbp = pd.read_csv('TimeScale.csv',
                            usecols=['yrbp1950'])
#Convert object from pandas Data frame type  to 1D array type
depth1=np.array(depth.as_matrix())
#Reshape object from column to raw 
depth1=depth1[:, 0]
tsdepth1=np.array(tsdepth.as_matrix())
tsdepth1=tsdepth1[:, 0]
yearbp1 = np.array(yearbp.as_matrix())
yearbp1 = yearbp1[:, 0]
#interpolate sample ages from sample depths1 using time scale tsdepth1, yearbp1
samplYr1=np.interp(depth1, tsdepth1, yearbp1)
samplYr =np.round(samplYr1,2)
f_out.write('YearBefore1950 \n')
for samplYr in samplYr:
    f_out.write(str(samplYr))
    f_out.write('\n')
    
f_out.close
#print(samplYr)

print('Done Ages are in file SamplesAges.txt')
