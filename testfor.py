#!/Users/y1275963/anaconda/bin/python
# -*- coding: utf-8 -*-
"""
Created on Wed Aug  5 19:38:18 2015

@author: y1275963
"""
import socks
import socket
import urllib2
from multiprocessing import Pool
import json
import os
import time
import requests
from PIL import Image
from StringIO import StringIO
from requests.exceptions import ConnectionError

import getlist
import pickle
import sys
import check
def down(query):
    
    if set([ query + str(x) +'.jpg' for x in range(4)]) & set(os.listdir('/Users/y1275963/Pictures/dicima')) == set():
        BASE_URL = 'https://ajax.googleapis.com/ajax/services/search/images?'\
                 'v=1.0&q=' + query + '&start=%d'
        BASE_PATH = '/Users/y1275963/Pictures/dicima'
        
        # rec =[]
        # if query.startswith('#'):
        #     # Denote the comments
        #     print query
        # else:
        #     ans1 = None
        #     ans2 = None
            
        #     try:
        #         ans1 = 'Dic, ',dic[query]
        #     except KeyError:
        #         pass
            
        #     try: 
        #         tk= check.checkwords(query)
        #         ans2 = 'Lon, ', tk
        #     except TypeError:
        #         pass
                
        #     if ans1 != None or ans2 != None:
        #         print query
        #     if ans1 != None:
        #         print ans1
        #         rec.append(r'Dic, '+dic[query].encode('utf8')+'\n')
        #     if ans2 != None:
        #         print ans2
        #         rec.append(r'Lon, '+tk.encode('utf8')+'\n')
        #     if ans1 == None and ans2 == None:
        #         print "###None found", query
        #         rec.append('"###None found", query')
        #     print '\n'
        #     filename = query+'.txt'
             
        #     with open(os.path.join(BASE_PATH(filename, "w"))) as text_file:
        #         text_file.write('***'.join(rec))
    
        start = 0 
        r = requests.get(BASE_URL % start)
        for index,image_info in enumerate(json.loads(r.text)['responseData']['results']):
          url = image_info['unescapedUrl']
          try:
            image_r = requests.get(url)
          except ConnectionError, e:
            print 'could not download %s' % url
            continue
            
          # Remove file-system path characters from name.
          title = query + str(index)
          
          file = open(os.path.join(BASE_PATH, '%s.jpg') % title, 'w')
          try:
            Image.open(StringIO(image_r.content)).save(file, 'JPEG')
          except IOError, e:
            # Throw away some gifs...blegh.
            print 'could not save %s' % url
            continue
          finally:
            file.close()
            print "Finished" + query
            
def sockdown(query):
    socks.setdefaultproxy(socks.PROXY_TYPE_SOCKS5, "127.0.0.1", 1080)
    socket.socket = socks.socksocket

    pool = Pool(processes=14)              # process per core
    pool.map(down, query)

if __name__ == '__main__':
    socks.setdefaultproxy(socks.PROXY_TYPE_SOCKS5, "127.0.0.1", 1080)
    socket.socket = socks.socksocket

    dic = pickle.load(open('data8003000.pick','rb'))
  
    with open(sys.argv[1]) as temp_file:
        imagelist = [line.strip() for line in temp_file]
    pool = Pool(processes=4)              # process per core
    pool.map(down, imagelist)  
