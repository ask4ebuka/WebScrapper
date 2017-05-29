# -*- coding: utf-8 -*-
"""
Created on Sat May 27 09:06:05 2017

@author: abdulrahman
"""
"""
properly aligned csv created

"""
from bs4 import BeautifulSoup
import urllib
import csv
data = []
file = urllib.request.urlopen('http://racing.hkjc.com/racing/info/meeting/Racecard/english/Local')
soup = BeautifulSoup(file,"lxml")
soup = soup.find("body")
# body of HTML acquired

soup = soup.find("table",{"class":"draggable hiddenable"})
table_body = soup

rows = table_body.find_all('tr')
for row in rows:
    cols = row.find_all('td')    
    cols = [ele.text.strip() for ele in cols]
    data.append(cols) 
      
#    data.append([ele for ele in cols if ele]) # Get rid of empty values
print (data)

with open("output1.csv", "w") as f:
    writer = csv.writer(f)
    writer.writerows(data)
    
