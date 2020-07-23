#!/bin/python
import pandas as pd
import glob, os

os.chdir("/home/marco/workspace/git/StatLearnTeam/DataCovidNEW/")
all_files = glob.glob("new*.csv")

li = []

for filename in all_files:
    df = pd.read_csv(filename, index_col=None, header=0)
    li.append(df)

frame = pd.concat(li, axis=0, ignore_index=True)

frame.to_csv('/home/marco/workspace/git/StatLearnTeam/articles_analysis/new_prociv_data.csv', sep = ';', na_rep = 'NULL')
