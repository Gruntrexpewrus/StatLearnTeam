#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun  4 13:12:17 2020

@author: marco
"""
from collections import OrderedDict

def from_string_to_list(string):
    string = string.replace('\'', '')    
    t = string.strip('][\'').split(' ') 
    t = [c.replace(' ', '').replace('\n', '').replace(',','') for c in t]
    
    return t
    
import pandas as pd
intopic = pd.read_csv('/home/marco/workspace/git/StatLearnTeam/dataset/intopic_it_articles.csv', sep = ';')
dataset = pd.read_csv('/home/marco/workspace/git/StatLearnTeam/dataset/articles_dataset.csv', sep = ';')
dataset = dataset.drop(columns = ['Unnamed: 0'])

regions_tmp = dataset.region.unique()
regions = {}

for r in regions_tmp:
    r = r.replace('\'', '')    
    t = r.strip('][\'').split(' ') 
    t = [c.replace(' ', '').replace('\n', '').replace(',', '') for c in t]
    
    for reg in t:
        #x1print(reg)
        regions[reg] = dict()
        
authors = dataset.author.unique().tolist()

for author in authors:
    
    region_outlet = dataset['region'][dataset.author == author].unique().tolist()
    region_outlet = [from_string_to_list(x) for x in region_outlet][0]
    
    '''
    for r in region_outlet:
        print(r)
        num_articles_published = len(dataset[dataset.author == author])
        regions[r].append([author, num_articles_published])
        
    '''

for i in dataset.index:
    
    author = dataset['author'][i]
    regions_article = from_string_to_list(dataset['region'][i])
    website = dataset['website-domain'][i]
    
    for r in regions_article:
        
        if author not in regions[r].keys():
            regions[r][author] = [1, [website]]
            
            
        if r in regions.keys():
            #print(regions[r][author])
            
            regions[r][author] = [regions[r][author][0] + 1 , regions[r][author][1] + [website]]
    
    
    
    
for k in regions.keys():
    print(k.upper(), '\n')
    
    authors_in_region = [(auth, regions[k][auth][1], regions[k][auth][0]) for auth in regions[k].keys()]
    
    authors_in_region.sort(key = lambda x : x[2], reverse = True)
    

    
    lim_print = 4    
    if len(regions[k].keys()) < lim_print:
        lim_print = len(regions[k].keys())
            
    for author_info in authors_in_region[:lim_print]:
        website = list(set(author_info[1]))
        num_articles_published =  author_info[2]
        
        print('\t - %s (%s) : %d articles published' % (author_info[0], website, num_articles_published))

    print('\n')

    
    
    
    
    
    
    
    
    
    
    
    