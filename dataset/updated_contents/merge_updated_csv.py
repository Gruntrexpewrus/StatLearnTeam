#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun  7 15:55:34 2020

@author: marco
"""


import pandas as pd
import glob
import re

csv_paths = glob.glob('/home/marco/workspace/git/StatLearnTeam/dataset/updated_contents/*.csv')

dataset = pd.DataFrame()

for path in csv_paths:
    dataset = dataset.append(pd.read_csv(path, sep = ';', index_col = [0]))
    
    
# Cleaning data section
dataset = dataset.dropna(how = 'any')
dataset['content'] = dataset['content'].map(lambda x: x.replace('(ASIpress)', ''))
dataset['content'] = dataset['content'].map(lambda x: x.replace('(Adnkronos)', ''))
dataset['content'] = dataset['content'].map(lambda x: re.sub(r'\n', '.', x))
dataset['content'] = dataset['content'].map(lambda x: re.sub(r'\t', '', x))
dataset['content'] = dataset['content'].map(lambda x: re.sub(r'.Stampa', '', x))
dataset['content'] = dataset['content'].map(lambda x: x.strip('.$,#-'))
dataset['content'] = dataset['content'].map(lambda x: x.strip())
dataset = dataset[dataset.content != ' ']
dataset = dataset[dataset.content != '']
dataset = dataset.drop_duplicates(subset = ['content'], keep = 'first')

dataset = dataset.reset_index(drop = True)


authors_region = {' La Gazzetta del Mezzogiorno': '',
 ' Il Giornale': '',
 ' ASIpress': '',
 ' Il Fatto Quotidiano': '',
 ' Stretto Web': '',
 ' Arma dei Carabinieri': '',
 ' Corriere Adriatico': '',
 ' Il Gazzettino Web': '',
 ' La Gazzetta dello Sport': '',
 ' Liguria Notizie': '',
 ' La Repubblica': '',
 ' Fanpage': '',
 ' Marche Notizie': '',
 ' Libero Quotidiano': '',
 ' Blitz': '',
 ' Ragusa Oggi': '',
 ' Il Messaggero': '',
 ' CalabriaPage': '',
 ' Salernonotizie': '',
 ' Il Meridiano News': '',
 ' Tgcom24': '',
 ' Tgcom': '',
 ' Il Sussidiario': '',
 ' Il Secolo XIX': '',
 ' Il Crotonese': '',
 ' Meteo Web': '',
 ' CalcioWeb': '',
 ' Campanianotizie': '',
 " L'Eco del Chisone": '',
 ' Vivere Marche': '',
 ' La Stampa': ''}











dataset.to_csv('/home/marco/workspace/git/StatLearnTeam/dataset/articles.csv' , sep = ';', na_rep = 'NULL')


def from_string_to_list(string):
    string = string.replace('\'', '')    
    t = string.strip('][\'').split(' ') 
    t = [c.replace(' ', '').replace('\n', '').replace(',','') for c in t]
    
    return t





