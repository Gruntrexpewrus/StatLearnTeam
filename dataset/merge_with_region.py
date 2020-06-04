#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun  4 11:28:50 2020

@author: marco
"""

import pandas as pd


dataset_root = '/home/marco/workspace/git/StatLearnTeam/dataset/'



dataset = pd.read_csv('/home/marco/workspace/git/StatLearnTeam/dataset/intopic_it_articles.csv', sep = ';')
websites = pd.read_csv(dataset_root + 'author_websites.csv', sep = ';')
regions = pd.read_csv(dataset_root + 'quotidiani.csv', sep = ',')

dataset.drop(dataset.columns[dataset.columns.str.contains('unnamed',case = False)],axis = 1, inplace = True)
websites.drop(websites.columns[websites.columns.str.contains('unnamed',case = False)],axis = 1, inplace = True)
regions.drop(regions.columns[regions.columns.str.contains('unnamed',case = False)],axis = 1, inplace = True)

regions.rename(columns = {'Region':'regions', 'Domain':'website-domain'}, inplace = True)

#test_df = pd.concat([dataset, websites])
test_df = dataset.merge(websites, on='author', how='inner')
test_df = test_df.merge(regions, on = 'website-domain', how = 'inner')
test_df.drop(test_df.columns[test_df.columns.str.contains('regions',case = False)],axis = 1, inplace = True)

test_df.drop_duplicates(ignore_index = True)