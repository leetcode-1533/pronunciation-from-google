#!/Users/y1275963/anaconda/bin/python
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 18 16:09:11 2015

@author: y1275963
"""


import sys  
import urllib
from bs4 import BeautifulSoup

def returnitem(cala):
    for item in cala:
        subitem = item.find('div',{'class':'text'})
        yield subitem.text.encode('utf-8')

def getdic(url):
    
    empdic = {}
    html = urllib.urlopen(url).read()
    soup = BeautifulSoup(html)
    
    lists_men = soup.findAll('div',{'class':'col_a col text'})
    lists = soup.findAll('div',{'class':'col_b col text'})
    
    for item,meaning in zip(returnitem(lists),returnitem(lists_men)):
        empdic[item] = meaning
    
    return empdic
    
        
    
    
    


if __name__ == "__main__":
    
    url = 'http://www.memrise.com/course/735854/gre-3000-10/'+str(sys.argv[1]).rstrip()+'/'

#    reload(sys)  
#    sys.setdefaultencoding('utf8')
    dic = getdic(url)
    
    print '\n'.join(dic.keys())

    


