#!/Users/y1275963/anaconda/bin/python
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 25 13:36:10 2015

@author: y1275963

Get Barron 800's list and meaning
"""

import getlist
import pickle 
import random
import sys
import os
import time
import subprocess

def geterate_pickel():
    baseurl = 'http://www.memrise.com/course/121215/barrons-800-essential-word-list-gre/'
    
    base = {}
    for i in range(1,81):
        print i
        url = baseurl + str(i)
        dic = getlist.getdic(url)
        real_dic = {v: k for k, v in dic.items()}
        base[i] = real_dic
        
    pickle.dump(base, open('b800.pickle','wb'))
    return base
    
def dump(passed,nonepassed,spe):
    pickle.dump(passed,open('b800passed','wb'))
    pickle.dump(nonepassed,open('b800nonepassed','wb'))
    pickle.dump(spe,open('b800speed','wb'))
    
def readpickle():
    ped = pickle.load(open('b800passed','rb'))
    nonepede = pickle.load(open('b800nonepassed','rb'))
    spe = pickle.load(open('b800speed','rb'))
    return ped,nonepede,spe
    
def genpool(num):
    dic = pickle.load(open('b800.pickle','rb'))
    passed,nonepassed,spe = readpickle()
    print "passed:",len(passed)
    print "Nonepassed", nonepassed
    
    ignorepool = passed + nonepassed
    
    dicpool = {}
    for item in dic:
        dicpool.update(dic[item])
    
    testpool = []
    for item in dicpool:
        if item not in ignorepool:
            testpool.append(item)
    
    return list(random.sample(set(testpool),num)),dicpool 
            

def genchoice(right,pool):
    choices = [right]
    while len(choices) != 4:
        pick = random.choice(pool.values())
        if pick not in choices:
            choices.append(pick)
    random.shuffle(choices)
    
    return choices

    
    
    
if __name__ == "__main__":
    squery = 'afplay /Users/y1275963/Desktop/v2a/audio/check_j26_800/'
 
    passed,nonepassed,spe = readpickle()
    questions, dicpool = genpool(20)
    
    print '\n'
    for qitem in questions:  
        
        print qitem
        subprocess.Popen(['afplay','/Users/y1275963/v2a/audio/check_j26_800/'+qitem+'.mp3'])
             
        # Get the choice:
        choices = genchoice(dicpool[qitem],dicpool)
        
        for index,item in enumerate(choices):
            print index+1,item
            
        # prompt input:
        start = time.time()
        
        sel = raw_input('You choices:\n')
        if str(sel) == 'q':
            break
        elif int(sel) == 5:
            print qitem ,"*****wrong,the right answer is:\n",dicpool[qitem],'\n'
            nonepassed.append(qitem)
        else: 
            if choices[int(sel)-1] == dicpool[qitem]:
                print qitem ,"passed\n"
                passed.append(qitem)
                end = time.time()
                spe[qitem] = end - start
            else:
                print qitem ,"*****wrong,the right answer is:\n",dicpool[qitem],'\n'
                nonepassed.append(qitem)
        
        dump(passed,nonepassed,spe)