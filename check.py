#!/Users/y1275963/anaconda/bin/python
"""
Created on Thu Jul 16 11:27:26 2015

@author: y1275963

An utility for checking the most common words from Longman API
"""
import requests
import sys

def checkwords(words):

    
    dic = requests.get('https://api.pearson.com:443/v2/dictionaries/laad3/entries?headword='+words)
    #dic.raise_for_status()
    # Longman dictionary will return status 200 no matter found or not 
    ying = dic.json()
    if ying['results'] == []:
        raise TypeError(words)
        
    ying1 = ying['results']
    ying2 = ying1[0]
    ying3 = ying2['senses'][0]
    definition = ying3['definition']
    
    return definition

if __name__ == "__main__":
    print sys.argv[1],': ',checkwords(sys.argv[1])

