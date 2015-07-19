#!/Users/y1275963/anaconda/bin/python
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 18 16:09:11 2015

@author: y1275963
"""


import sys  
import urllib
from bs4 import BeautifulSoup


if __name__ == "__main__":
    
    url = 'http://www.memrise.com/course/735854/gre_3000/'+sys.argv[1]+'/'

    reload(sys)  
    sys.setdefaultencoding('utf8')
    
    html = urllib.urlopen(url).read()
    soup = BeautifulSoup(html)
    
    lists = soup.findAll('div',{'class':'col_a col text'})
    lists_men = soup.findAll('div',{'class':'col_b col text'})
    
    for item in lists:
        subitem = item.find('div',{'class':'text'})
        print str(subitem.text).lower()
    for item in lists_men:
        subitem2 = item.find('div',{'class':'text'})
        print subitem2.text

    


