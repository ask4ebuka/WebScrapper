# -*- coding: utf-8 -*-
"""
Created on Sat May 27 09:06:05 2017

@author: abdulrahman
"""
# WEb scraper 1
#successful conversion from list to csv


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
    data.append([ele for ele in cols if ele]) # Get rid of empty values

with open("output.csv", "w") as f:
    writer = csv.writer(f)
    writer.writerows(data)
    
#with open('csvfile', 'w') as myfile:
#    wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
#    wr.writerow(list(data))

#thecsv = csv.writer(open("your.csv", 'w'))
#for value in data:
#    thecsv.writerow(value)

#out = csv.writer(open("myfile.csv","w"), delimiter=',',quoting=csv.QUOTE_ALL)
#out.writerow(data)
#print (data)