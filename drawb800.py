#!/Users/y1275963/anaconda/bin/python
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 25 13:36:10 2015

@author: y1275963

Get Barron 800's list and meaning
"""

import pickle 
import random
import sys
import os
import time
import subprocess

        
class quer:
    def __init__(self,num):
        self.data = pickle.load(open('bigpool.pick','rb'))
        self.genq(num)
        print self.qpool,'\n'

    
    def test(self):
        for qitem in self.qpool:
            start = time.time()
            
            print qitem
            subprocess.Popen(['afplay','/Users/y1275963/v2a/audio/check_j26_800/'+qitem+'.mp3'])
            
            choices = self.genchoice(self.data[qitem]['exp'],self.qpool)
            raw_input('think first')
            for index,item in enumerate(choices):
                print index+1,item
                
            sel = raw_input('You choices:\n')
            end = time.time()
            timeuse = end - start
            
            if str(sel) == 'q':
                break
            elif int(sel) == 5:
                print qitem ,"*****wrong,the right answer is:\n",self.data[qitem]['exp'],'\n'
                self.data[qitem]['wrong'].append([time.strftime("%d/%m/%Y"),timeuse,'No idea'])
                raw_input('wait for review')
            else: 
                if choices[int(sel)-1] == self.data[qitem]['exp']:
                    print qitem ,"passed\n"
                    self.data[qitem]['right'].append([time.strftime("%d/%m/%Y"),timeuse])
                else:
                    print qitem ,"*****wrong,the right answer is:\n",self.data[qitem]['exp'],'\n'
                    self.data[qitem]['wrong'].append([time.strftime("%d/%m/%Y"),timeuse,choices[int(sel)-1]])
                    raw_input('wait for review')
            
            pickle.dump(self.data,open('bigpool.pick','wb'))
         
         
    def genq(self,num):
        qpool = []
        for item in self.data :
            if self.data[item]['class'] =='b800' and len(self.data[item]['wrong']) == 0 and  len(self.data[item]['right']) == 0:
#            if self.data[item]['class'] == 'b800' and self.data[item]['wrong'] == [] and self.data[item]['right'] == []:
                qpool.append(item)  
        
        self.poll = qpool
        
        self.qpool = list(random.sample(set(qpool),num))
                    
        
    def genchoice(self,right,choicepool):
        choices = [right]
        while len(choices) != 4:
            pick = random.choice(choicepool)
            pick = self.data[pick]['exp']
            if pick not in choices:
                choices.append(pick)
        random.shuffle(choices) 
        return choices
        
            
    
def quifind(data,query):
    tk = []
    for item in data:
        if len(data[item][query])>0 and data[item]['class'] =='b800':
            tk.append([item,data[item]])
    return tk
def quifind2(data,query):
    tk = []
    for item in data:
        if len(data[item]['right'])==0 and len(data[item]['wrong'])==0  and data[item]['class'] =='b800':
            tk.append([item,data[item]])
    return tk   
def getf(listl):
    tk = []
    for item in listl:
        tk.append(item[0])
    return tk
        
    
if __name__ == "__main__":
    tk = quer(20)
    tk.test()  
    
    right = quifind(tk.data,'right')
    wrong = quifind(tk.data,'wrong')
    pool = tk.poll