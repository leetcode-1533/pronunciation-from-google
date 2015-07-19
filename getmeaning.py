#!/Users/y1275963/anaconda/bin/python
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 18 16:09:11 2015

@author: y1275963
"""


import sys  
import urllib
from bs4 import BeautifulSoup

from tabulate import tabulate

def returnitem(cala):
    for item in cala:
        subitem = item.find('div',{'class':'text'})
        yield str(subitem.text).decode('utf-8')

    
if __name__ == "__main__":
    
    url = 'http://www.memrise.com/course/735854/gre_3000/'+sys.argv[1]+'/'

    reload(sys)  
    sys.setdefaultencoding('utf8')
    
    html = urllib.urlopen(url).read()
    soup = BeautifulSoup(html)
    
    lists_men = soup.findAll('div',{'class':'col_a col text'})
    lists = soup.findAll('div',{'class':'col_b col text'})
    
    gen_list = []
    
    for item,meaning in zip(returnitem(lists),returnitem(lists_men)):
        gen_list.append([meaning,item])
    
    re = tabulate(gen_list,tablefmt="latex")
    
    text_file = open("meaning_"+sys.argv[1],"w")
    text_file.write(re)
    text_file.close()
    

    


