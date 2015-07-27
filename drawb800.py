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
    
def read():
    ped = pickle.load(open('b800passed','rb'))
    nonepede = pickle.load(open('b800nonepassed','rb'))
    spe = pickle.load(open('b800speed','rb'))
    return ped,nonepede,spe
    
    
if __name__ == "__main__":
    dic = pickle.load(open('b800.pickle','rb'))
    passed,nonepassed,spe = read()
    print "passed:",len(passed)
    print "Nonepassed", nonepassed
    # Set the question periphery 
    dicpool = {}
    for i in range(int(sys.argv[1]),int(sys.argv[2])):
        dicpool.update(dic[i])
    # Random generate 20 items from the lists
    questions = []
    keypool = dicpool.keys()
    random.shuffle(keypool)
    for item in keypool:
        if (item not in passed) and (item not in nonepassed):
            questions.append(item)
    if len(questions) > 50:
        questions = questions[1:51]
    print questions
    print '\n'
    
    
    squery = 'afplay /Users/y1275963/Desktop/v2a/audio/check_j26_800/'
    
    for qitem in questions:
        
        if qitem in passed:
            pass
        else:       
            print qitem
            subprocess.Popen(['afplay','/Users/y1275963/Desktop/v2a/audio/check_j26_800/'+qitem+'.mp3'])
            
            
            # Get the choice:
            choices = [dicpool[qitem]]
            
            while len(choices) != 4:
                pick = random.choice(dicpool.values())
                if pick not in choices:
                    choices.append(pick)
            random.shuffle(choices)
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
            
        

        
    
    
        
     