#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun  7 15:55:34 2020

@author: marco
"""


import pandas as pd
import glob

csv_paths = glob.glob('/home/marco/workspace/git/StatLearnTeam/dataset/updated_contents/*.csv')

dataset = pd.DataFrame()

for path in csv_paths:
    dataset = dataset.append(pd.read_csv(path, sep = ';', index_col = [0]))
    
    
dataset = dataset.dropna(how = 'any')
dataset = dataset.reset_index(drop = True)