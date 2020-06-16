#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May  6 20:03:05 2020

@author: marco
"""


''' 

HERE WE WILL UPDATE EACH ARTICLE CONTENT 

'''
import pandas as pd

from newsparsers.fanpage_parser import FanpageParser #www.fanpage.it
from newsparsers.gazzetta_mezzogiorno import LaGazzettaDelMezzogiornoParser #www.lagazzettadelmezzogiorno.it
from newsparsers.meridiano_news import IlMeridianoNewsParser #www.ilmeridianonews.it
from newsparsers.blitz_quotidiano import BlitzParser # www.blitzquotidiano.it
from newsparsers.strettoweb import StrettoWebParser # www.strettoweb.com
from newsparsers.salernonotizie import SalernonotizieParser # www.salernonotizie.it
from newsparser.meteoweb import MeteowebParser # www.meteoweb.eu
from newsparser.ilfattoquotidiano import IlFattoQuotidianoParser # www.ilfattoquotidiano.it


intopic_dataset_path = '/home/marco/workspace/git/StatLearnTeam/dataset/intopic_it_articles.csv'
updated_datasets_root_path = '/home/marco/workspace/git/StatLearnTeam/dataset/updated_contents/'

dataset = pd.read_csv(intopic_dataset_path, sep = ';')

#f = FanpageParser('www.fanpage.it', dataset_path = intopic_dataset_path)
#data = f.get_updated_dataset()
#f.write_dataset_to_file(updated_datasets_root_path)
