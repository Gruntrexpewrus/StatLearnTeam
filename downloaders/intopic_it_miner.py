#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import urllib3
import random
import time

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning) # No SSL certificate, so ignore https warnings


website_url = "https://www.intopic.it/crono/varie/cronaca/?pagina="
http = urllib3.PoolManager()

for i in range(604, 1300):
    url = website_url + str(i)
    
    
    
    file_path = "/home/marco/workspace/git/StatLearnTeam/web_pages_index/" + str(i) + ".html"


        
    hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
           'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8', 
           'Connection': 'keep-alive'}

    try:
        response = http.request('GET', url, headers=hdr)
        
        content = response.data.decode('ISO-8859-1')
        
        f = open(file_path, 'w') # Saving path: files will be like 234.html
        f.write(str(content))
        f.close()
        print('Downloaded %s.html' % str(i))
    
        wait_time = random.randint(8,  11)#Wait for a period of time from 1 to 4 seconds. 
        time.sleep(wait_time)
        
    except Exception as e: # In case something happens, wait 
        print(e)
        time.sleep(60)
