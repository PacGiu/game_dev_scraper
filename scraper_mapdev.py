#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 25 2018

@author: Paco
"""

from bs4 import BeautifulSoup
import requests as r
import io
import csv

# if saving the file
url='view-source_https___www.gamedevmap.com_index.php_location=Prague.htm'

# from url
url1='https://www.gamedevmap.com/index.php?location=Prague'

# get BS object
source=r.get(url1).content
soup=BeautifulSoup(source,'lxml')

#opens new file to write on
csv_file=open('gamedev_scrape.csv','w')
csv_writer=csv.writer(csv_file)
csv_writer.writerow(['Company','link','Type','city','region','country'])

#if some entry is missing use try as follows 
#try:
#    pass
#except Exception as e:
#        pass

# finds all the tr and select the td enclosing the data
for tab_string in soup.find_all('tr', {'class':{'row1','row2'}}):
    sub_tab=tab_string.find_all('td')
    
    company=sub_tab[0].text
    link=sub_tab[0].a['href']
    Type=sub_tab[1].text
    city=sub_tab[2].text
    region=sub_tab[3].text
    country=sub_tab[4].text

    print(company,link,Type,city,region,country)
    
    # write the date into the file
    csv_writer.writerow([company,link,Type,city,region,country])

csv_file.close()
  
