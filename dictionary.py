#!/Users/y1275963/anaconda/bin/python
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 10 12:30:16 2015

@author: y1275963
"""
import pickle 
import check
import csv
import os
import time
import sys

data = pickle.load(open('bigpool.pick','rb'))
alldic = sorted([x for x in data ])
b800 = sorted([x for x in data if data[x]['class'] == 'b800'])

def printb800():
    for item  in b800:
        print item
        print data[item]['exp'],'\n'

def define(filename):
    csvdata = []
    with open(filename,'r') as f:
        for line in f:
            li = line.strip()
            if not li.startswith('#'):
                try:
                    print li
                    print data[li]['exp'],'\n'
                    csvdata.append([li,data[li]['exp']])
                except:
                    print li
                    print '\n'
                    csvdata.append([li,None])
    return csvdata
    
def tolower(d):
    for k in d.keys():
        v = d.pop(k)
        if (type(k) == str) and (not k.islower()):
            k = k.lower()
        d[k] = v
    
    pickle.dump(d,open('bigpool.pick','wb'))
    pickle.dump(d,open(os.path.join('rec',time.strftime("%Y%m%d-%H%M%S")),'wb'))
         

if __name__ == "__main__":
    csvdata = define(sys.argv[1])

    with open('/tmp/rev3000_1.csv','wb') as f:
        wr = csv.writer(f,delimiter=',',quoting=csv.QUOTE_ALL)
        wr.writerow(['Words','Explanation'])
        wr.writerows(csvdata)

