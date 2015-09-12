#!/Users/y1275963/anaconda/bin/python
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 17 17:46:41 2015

@author: y1275963
"""
import pickle

listfile = '/Users/y1275963/v2a/merged-file'
data = pickle.load(open('bigpool.pick','rb'))

lines = []
with open(listfile,'r') as f:
    for line in f:
        li = line.strip()
        if not li.startswith('#'):
            lines.append(li)
        

    
        
    
tk = set(lines)

b800 = sorted([x for x in data if data[x]['class'] == 'b800'])
p3000 = sorted([x for x in data if data[x]['class'] == 'p3000'])
aband = sorted([x for x in data if data[x]['class'] == 'abandon'])
llist = list(set(b800) | set(p3000) | set(aband))

tets = [x for x in tk if x not  in llist ]