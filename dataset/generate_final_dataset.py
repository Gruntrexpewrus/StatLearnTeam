#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul  4 15:16:34 2020

@author: marco
"""

import pandas as pd

dataset_root = '/home/marco/workspace/git/StatLearnTeam/dataset/'

articles = pd.read_csv(dataset_root + 'old_articles.csv', sep = ';', index_col = [0])

articles.dropna(inplace = True)
articles.drop_duplicates(subset = ['title', 'content', 'url'], inplace = True)

articles.drop(['tags', 'url', 'region', 'website-domain'], axis = 1, inplace = True)

articles.rename({'author_head_office_region':'region', 'author_italy_zone':'zone'}, axis = 1, inplace = True)

prev_index = -1

for i in articles.index:
    '''
    if (int(i) - 1) != prev_index:
        print('Prev index = ', prev_index)
        print('Index error at', i)
        print('i-1 = ', (int(i) - 1))
    prev_index = int(i)
    '''
    
    
    
    # Fix dates
    string_date = articles.loc[i, 'date']
    date_tokens = string_date.split('-')
    
    year = date_tokens[0]
    month = date_tokens[1]
    day = date_tokens[2]
    
    if month == '01' or month == '06':
        articles.drop(index = i, inplace = True)
    elif month == '02' and (int(day) < 24):
        articles.drop(index = i, inplace = True)
    elif year != '2020':
        articles.drop(index = i, inplace = True)
    else:

        if len(month) < 2:
            month = '0' + month
        if len(day) < 2:
            day = '0' + day
        
        updated_string_date = year + '-' + month + '-' + day
        
        # Fix author leading and trailing spaces
        articles.loc[i, 'date'] = updated_string_date
        articles.loc[i, 'author'] = articles.loc[i, 'author'].strip()
    
        
    
articles.index = range(0, len(articles.index))

articles.to_csv(dataset_root + 'articles.csv', sep = ';', na_rep = 'NULL')

# Fix author spacing (trim left and right)