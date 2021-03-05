#!/usr/bin/env python
# coding: utf-8

# """
# Created March 4,   2021
# 
# @author: Andrei Kurbatov
# """

# ### Requirement 1: Time scale file is comma separetd and named TimeScale.csv
# ### Requirement 2: Time scale file  TimeScale.csv column names are: tsdepth and yrb1950
# ### Requirement 3:  File with depths shoudl be named: SamplesDepths.csv with a columnt name: depth

import pandas as pd
import numpy as np
np.set_printoptions(precision=3)

# ## Setup  input and output files
# Create a new file to output data: SamplesDepths.csv
f_wAges='SamplesAges.txt'
# File with a time scale: TimeScale.csv'
tsFilePath='TimeScale.csv'
# Open file SamplesDepths with sample depths stored in the column named depth
sampleDepths = pd.read_csv('SamplesDepths.csv',index_col=False)
# ## Interpolate data
ts_df=pd.read_csv(tsFilePath, sep=',', engine='python',  index_col=False)
#interpolate sample ages from sample depths1 using time scale tsdepth1, yearbp1
samplYr=np.interp(sampleDepths['depth'], ts_df['tsdepth'],  np.float64(ts_df['yrbp1950']))
sampleAges=pd.DataFrame(samplYr, columns=['YearBefore1950'])
sampleAges.to_csv(f_wAges, index = False, header=True)





