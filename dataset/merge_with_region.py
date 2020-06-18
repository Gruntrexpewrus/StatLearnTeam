#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun  4 11:28:50 2020

@author: marco
"""

import pandas as pd

   
def from_string_to_list(string):
    string = string.replace('\'', '')
    t = string.strip('][\'').split(' ') 
    t = [c.replace(' ', '').replace('\n', '').replace('\'', '').replace(',','') for c in t]
    
    return t

dataset_root = '/home/marco/workspace/git/StatLearnTeam/dataset/'


# Loading datasets
dataset = pd.read_csv('/home/marco/workspace/git/StatLearnTeam/dataset/intopic_it_articles.csv', sep = ';')
websites = pd.read_csv(dataset_root + 'author_websites.csv', sep = ';')
quotidiani = pd.read_csv(dataset_root + 'quotidiani.csv', sep = ',')

# Dropping unwanted columns 
dataset.drop(dataset.columns[dataset.columns.str.contains('unnamed',case = False)],axis = 1, inplace = True)
websites.drop(websites.columns[websites.columns.str.contains('unnamed',case = False)],axis = 1, inplace = True)
quotidiani.drop(quotidiani.columns[quotidiani.columns.str.contains('unnamed',case = False)],axis = 1, inplace = True)

# Renaming columns of regions for consistency
quotidiani.rename(columns = {'Region':'regions', 'Domain':'website-domain'}, inplace = True)

#test_df = pd.concat([dataset, websites])

#test_df = dataset.merge(websites, on='author', how='inner')
#test_df = test_df.merge(regions, on = 'website-domain', how = 'inner')
#test_df.drop(test_df.columns[test_df.columns.str.contains('regions',case = False)],axis = 1, inplace = True)

#test_df = test_df.drop_duplicates(subset = 'url', ignore_index = True)

#test_df.to_csv('/home/marco/workspace/git/StatLearnTeam/dataset/articles_dataset.csv', sep = ';', na_rep = 'NA')


authors = dict()

for i in dataset.index:
    author = dataset['author'][i]
    dataset['region'][i] = ''
    
    ## ADD REGION BY TAG
    tags = from_string_to_list(dataset.tags[i])
    reg_articles = set()
    
    for tag in tags:
        tag = tag.lower().replace(' ', '_')
            
        
        if tag in quotidiani.regions.unique().tolist():            
            reg_articles.add(tag)
            
    ### ADD REGION BY REGIONS DATASET (quotidiani dataset)
    #websites = dataset['website-domain'][dataset.author == ]
    website = dataset['website-domain'][i]
    region_by_website = quotidiani.regions[quotidiani['website-domain'] == website].tolist()
    reg_articles.update(region_by_website)
    
    ### Try and tokenize the url to look for more clues about regions
    url = dataset['url'][i]
    url_tokens = url.split('/')
    url_tokens = [t.split('-') for t in url_tokens]
    
    for token in url_tokens:
        if token in quotidiani.regions.unique().tolist():            
            reg_articles.add(token)
    
    #### UPDATE VALUES FOR EACH AUTHOR
    if author not in authors.keys():
        authors[author] = set()
    if len(reg_articles) > 0:
        authors[author].update(reg_articles)
        dataset['region'][i] = str(list(reg_articles))
    else:
        dataset['region'][i] = '[]'
            

cols = ['author', 'regions']
author_regions = pd.DataFrame(data = None, columns = cols)
for author in authors.keys():
    author_regions = author_regions.append(pd.DataFrame([[author, str(list(authors[author]))]], columns = cols, index = [len(author_regions.index)]))
    
dataset = dataset[dataset.region != '[]']
author_regions = author_regions[author_regions.regions != '[]']

dataset.to_csv('/home/marco/workspace/git/StatLearnTeam/dataset/articles_dataset.csv', sep = ';', na_rep = 'NA')         
author_regions.to_csv('/home/marco/workspace/git/StatLearnTeam/dataset/author_regions.csv', sep = ';', na_rep = 'NA') 
            
            
            
            
            
            
            
            
            
            