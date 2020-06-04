#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 30 17:51:13 2020

@author: marco
"""


import pandas as pd
from collections import OrderedDict

dataset_root = '/home/marco/workspace/git/StatLearnTeam/dataset/'
dataset = pd.read_csv('/home/marco/workspace/git/StatLearnTeam/dataset/intopic_it_articles.csv', sep = ';')


info = dataset.groupby(['author']).size()
count_articles = []
for index in info.index:
    count_articles.append([index, info[index]])
    
count_articles.sort(key=lambda x:x[1], reverse = True)

cols = ['author', 'web-domains']
domain_dataset = pd.DataFrame(data = None, columns = cols)

for author in dataset.author:
    
    if author not in domain_dataset['author'].values.tolist():
        print(author)
        domains =  dataset.loc[dataset['author'] == author]['website-domain'].unique().tolist()
        
        domain_dataset = domain_dataset.append(pd.DataFrame(data = [[author, domains]], columns = cols, index=[len(domain_dataset.index)]))
        
        
#domain_dataset.to_csv(dataset_root + 'author_websites.csv', sep = ';', na_rep = 'NA')

regions = pd.read_csv(dataset_root + 'quotidiani.csv', sep = ';')