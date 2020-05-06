#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May  6 20:03:05 2020

@author: marco
"""


''' 

HERE WE WILL UPDATE EACH ARTICLE CONTENT 

'''

from newsparsers.fanpage_parser import FanpageParser

intopic_dataset_path = '/home/marco/workspace/git/StatLearnTeam/dataset/intopic_it_articles.csv'

f = FanpageParser('www.fanpage.it', dataset_path = intopic_dataset_path)
data = f.get_updated_dataset()

