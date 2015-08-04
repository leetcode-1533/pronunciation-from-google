#!/Users/y1275963/anaconda/bin/python
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 26 08:36:21 2015

@author: y1275963
"""

import getlist
import pickle
import sys
import check

def crawl():

    
    spider = {}
    
    baseurl = 'http://www.memrise.com/course/735854/gre-3000-10/'
    
    i = 12 # 12 is a special module
    url = baseurl + str(i)
    dic = getlist.getdic(url)
    spider[i] = dic
    # The rest are the same 
    for i in range(1,12) + range(13,35):
        print i 
        url = baseurl + str(i)
        dic = getlist.getdic(url)
        real_dic = {v: k for k, v in dic.items()}
        spider[i] = real_dic
        
    pickle.dump(spider,open('course_details.pickle','wb'))

def to_lower(d):


    return dict((k.lower(), v) for k, v in d.iteritems())


if __name__ == "__main__":


    # spi = pickle.load(open('course_details.pickle','rb'))
    # dic = {}
    # for item in spi:
    #     dic.update(spi[item])

    # b800 = pickle.load(open('b800.pickle','rb'))
    # for item in b800:
    #     dic.update(b800[item])

    dic = pickle.load(open('data8003000.pick','rb'))

    for line in open(sys.argv[1]):
        query = line.encode('utf-8').strip().lower()

        if not query.startswith('#'):

            ans1 = None
            ans2 = None
            
            try:
                ans1 = 'Dic, ',dic[query]
            except KeyError:
                pass
            
            try: 
                ans2 = 'Lon, ', check.checkwords(query)
            except TypeError:
                pass
                
            if ans1 != None or ans2 != None:
                print query
            if ans1 != None:
                print ans1
            if ans2 != None:
                print ans2
            if ans1 == None and ans2 == None:
                print "###None found", query
            print '\n'
        
         
         
