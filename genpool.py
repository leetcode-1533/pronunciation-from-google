#!/Users/y1275963/anaconda/bin/python
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 28 16:25:33 2015

@author: y1275963
"""
import time
import pickle

bigpool = {}

test = pickle.load(open('course_details.pickle','rb'))
p3000 = {}
for item in test:
    p3000.update(test[item])

for item in dicpool:
    bigpool[item] = {'exp':dicpool[item],'class' : 'b800'}

for item in p3000:
    if item not in bigpool:
        bigpool[item] = {'exp':p3000[item],'class':'p3000'}
    
    
for item in bigpool:
    if item in spe:
        bigpool[item]['right'] = [time.strftime("%d/%m/%Y"),spe[item]]

for item in bigpool:
    if item in passed and item not in spe:
        bigpool[item]['right'] = [time.strftime("%d/%m/%Y"),15]

for item in bigpool:
    if item in nonepassed:
        bigpool[item]['wrong'] = [time.strftime("%d/%m/%Y"),15]
        
