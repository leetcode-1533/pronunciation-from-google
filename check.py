#!/Users/y1275963/anaconda/bin/python
"""
Created on Thu Jul 16 11:27:26 2015

@author: y1275963

An utility for checking the most common words from Longman API
"""
import requests
import sys
import xmltodict, json
import simplejson

def checkwords(words):

    try:
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
        
#        return ying
        return definition
    except:
        return None
def getexam(words):
    try:
        dic = requests.get('https://api.pearson.com:443/v2/dictionaries/laad3/entries?headword='+words)
        ying = dic.json()
        if ying['results'] == []:
            raise TypeError(words)
        return ying['results'][0]['senses'][0]['examples'][0]['text']
    except:
        return None
        
def webdic(words):
    url = 'http://www.dictionaryapi.com/api/v1/references/collegiate/xml/%s?key=1a722996-be08-4224-9f5e-643b2da7eba3'%words
    try:
        dic = requests.get(url)
        o = xmltodict.parse(dic.content)
        jdic = simplejson.loads(json.dumps(o))
        return jdic
    except:
        return None
def getid(words):
    try:
        dic = webdic(words)
        return dic['entry_list']['entry']['@id']
    except:
        return None
def treasures(words):
    url = 'http://www.dictionaryapi.com/api/v1/references/thesaurus/xml/%s?key=fe90e889-eefb-470a-afa5-1ee170e5ab88'%words
    try:
        dic = requests.get(url)
        o = xmltodict.parse(dic.content)
        jdic = simplejson.loads(json.dumps(o))
        return jdic
    except:
        return None
def treasurelist(words):
    try:
        li = findkeys(treasures(words),'syn')
        return li.next()
        #return [item for item in li]    
    except:
        return None
    
def findkeys(node, kv):
    if isinstance(node, list):
        for i in node:
            for x in findkeys(i, kv):
               yield x
    elif isinstance(node, dict):
        if kv in node:
            yield node[kv]
        for j in node.values():
            for x in findkeys(j, kv):
                yield x
    
def getre(words):
    return [['words ',words],['Original ',getid(words)],['def ',checkwords(words)],['synonyms: ',treasurelist(words)],['exp',getexam(words)]]
    
if __name__ == "__main__":
    for line in open(sys.argv[1]):
        query = line.encode('utf-8').strip().lower()
    
        if query.startswith('#'):
            # Denote the comments
            print query
        else:
            print '\n', query
            for item in getre(query):
                print item
#    print sys.argv[1],': ',checkwords(sys.argv[1])

