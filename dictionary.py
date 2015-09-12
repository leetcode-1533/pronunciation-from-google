#!/Users/y1275963/anaconda/bin/python
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 10 12:30:16 2015

@author: y1275963
"""
import pickle 
import check
import unicodecsv
import os
import time
import sys

import sys
from DictionaryServices import *
import re

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
                    #print data[li]['exp'],'\n'
                    csvdata.append([li,dictdef(li)])
                except Exception as e:
                    print li
                    print '\n'
                    csvdata.append([li,None])
    return csvdata
    

def listdefine(filename):
    csvdata = []
    for line in filename:
        li = line.strip()
        if not li.startswith('#'):
            try:
                print li
                #print data[li]['exp'],'\n'
                csvdata.append([li,dictdef(li)])
            except Exception as e:
                print li
                print '\n'
                csvdata.append([li,None])
    return csvdata
    
def redecorator(func):
    def func_wrapper(name):
        try:
            return re.search(ur'\xb6(.*?)[\xe2$]', func(name)).group(0)[1:-1:]
        except:
            return None
            
    return func_wrapper

@redecorator   
def oxsys(test):
    try:
        searchword = test.decode('utf-8')
    except IndexError:
        errmsg = 'You did not enter any terms to look up in the Dictionary.'
        return errmsg
        sys.exit()
    wordrange = (0, len(searchword))
    dictresult = DCSCopyTextDefinition(None, searchword, wordrange)
    if not dictresult:
        errmsg = "'%s' not found in Dictionary." % (searchword)
        return errmsg.encode('utf-8')
    else:
        return dictresult.encode('utf-8')
        
def tolower(d):
    for k in d.keys():
        v = d.pop(k)
        if (type(k) == str) and (not k.islower()):
            k = k.lower()
        d[k] = v
    
    pickle.dump(d,open('bigpool.pick','wb'))
    pickle.dump(d,open(os.path.join('rec',time.strftime("%Y%m%d-%H%M%S")),'wb'))

def dictdef(words):
    try:
        test = data[words]['exp']
    except:
        test = None
        
    if test != None:
        return test
    else:
        return check.checkwords(words)

if __name__ == "__main__":
    csvdata = define(sys.argv[1])

    with open('/tmp/'+sys.argv[1]+'.csv','wb') as f:
        wr = unicodecsv.writer(f,delimiter=',',quoting=unicodecsv.QUOTE_ALL)
        wr.writerow(['Words','Explanation'])
        wr.writerows(csvdata)
