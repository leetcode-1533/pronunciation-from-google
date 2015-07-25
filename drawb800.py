#!/Users/y1275963/anaconda/bin/python
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 25 13:36:10 2015

@author: y1275963

Get Barron 800's list and meaning
"""

import getlist
baseurl = 'http://www.memrise.com/course/121215/barrons-800-essential-word-list-gre/'

base = {}
for i in range(1,81):
    print i
    url = baseurl + str(i)
    dic = getlist.getdic(url)
    real_dic = {v: k for k, v in dic.items()}
    base[i] = real_dic