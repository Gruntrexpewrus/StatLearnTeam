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


authors_region = {' La Gazzetta del Mezzogiorno': 'South',
 ' Il Giornale': 'North',
 ' ASIpress': 'South',
 ' Il Fatto Quotidiano': 'Centre',
 ' Stretto Web': 'South',
 ' Arma dei Carabinieri': '',
 ' Corriere Adriatico': 'Centre',
 ' Il Gazzettino Web': 'North',
 ' La Gazzetta dello Sport': 'North',
 ' Liguria Notizie': 'North',
 ' La Repubblica': 'Lazio',
 ' Fanpage': 'South',
 ' Marche Notizie': 'Centre',
 ' Libero Quotidiano': 'North',
 ' Blitz': 'Centre',
 ' Ragusa Oggi': 'Islands',
 ' Il Messaggero': 'Centre',
 ' CalabriaPage': 'South',
 ' Salernonotizie': 'South',
 ' Il Meridiano News': 'South',
 ' Tgcom24': 'North',
 ' Tgcom': 'North',
 ' Il Sussidiario': 'North',
 ' Il Secolo XIX': 'North',
 ' Il Crotonese': 'South',
 ' Meteo Web': '',
 ' CalcioWeb': '',
 ' Campanianotizie': 'South',
 " L'Eco del Chisone": 'North',
 ' Vivere Marche': 'Centre',
 ' La Stampa': 'North'}

authors_actual_region = {' La Gazzetta del Mezzogiorno': 'Puglia',
 ' Il Giornale': 'Lombardia',
 ' ASIpress': 'Abruzzo',
 ' Il Fatto Quotidiano': 'Lazio',
 ' Stretto Web': 'Calabria',
 ' Arma dei Carabinieri': '',
 ' Corriere Adriatico': 'Marche',
 ' Il Gazzettino Web': 'Veneto',
 ' La Gazzetta dello Sport': 'Lombardia',
 ' Liguria Notizie': 'Liguria',
 ' La Repubblica': 'Lazio',
 ' Fanpage': 'Campania',
 ' Marche Notizie': 'Marche',
 ' Libero Quotidiano': 'Lombardia',
 ' Blitz': 'Lazio',
 ' Ragusa Oggi': 'Sicilia',
 ' Il Messaggero': 'Lazio',
 ' CalabriaPage': 'Calabria',
 ' Salernonotizie': 'Campania',
 ' Il Meridiano News': 'Campania',
 ' Tgcom24': 'Lombardia',
 ' Tgcom': 'Lombardia',
 ' Il Sussidiario': 'Lombardia',
 ' Il Secolo XIX': 'Liguria',
 ' Il Crotonese': 'Calabria',
 ' Meteo Web': '',
 ' CalcioWeb': '',
 ' Campanianotizie': 'Campania',
 " L'Eco del Chisone": 'Piemonte',
 ' Vivere Marche': 'Marche',
 ' La Stampa': 'Piemonte'}










dataset.to_csv('/home/marco/workspace/git/StatLearnTeam/dataset/articles.csv' , sep = ';', na_rep = 'NULL')


def from_string_to_list(string):
    string = string.replace('\'', '')    
    t = string.strip('][\'').split(' ') 
    t = [c.replace(' ', '').replace('\n', '').replace(',','') for c in t]
    
    return t





