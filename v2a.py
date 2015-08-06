#!/Users/y1275963/anaconda/bin/python

import socks
import socket
import sys

import urllib2
import os
import thread

import check

import argparse

import csv


exerpath = os.getcwd()        

class audio:
    def __init__(self,foldername,word):
        
        self.title = word
        
        self.g_path = "https://ssl.gstatic.com/dictionary/static/sounds/de/0/"
        self.mp3_path = self.g_path + word + ".mp3"
        self.loc = os.path.join(exerpath,"audio")#now all goes to audio,foldername)
        
        if not os.path.exists(self.loc):
            os.makedirs(self.loc)  
            
        self.mp3_download()
        
        
    def mp3_download(self):    
        filename = os.path.join(self.loc,self.title)+'.mp3'
        if os.path.isfile(filename):
            print "***Existed", self.title
        else:
            try:
                mp3 = urllib2.urlopen(self.mp3_path)
                open(filename,'wb').write(mp3.read())
                print "Downloaded", self.title
            except:
                print sys.exc_info()

                print "*****Wrong Word:", self.title   
                print self.mp3_path

def download_aud(openfile):
    socks.setdefaultproxy(socks.PROXY_TYPE_SOCKS5, "127.0.0.1", 1080)
    socket.socket = socks.socksocket
    
    lock = thread.allocate_lock()
    for line in openfile:
        aud = str(line)
        lock.acquire()
        audio(openfile.name,aud.strip())
        lock.release()
        
def download_def(openfile):
    checked = []
    
    for line in openfile:
        try:
            word_def = check.checkwords(line.rstrip('\n'))
            definition = '*'+line.rstrip('\n')+': '+word_def
            print definition + '\n'
            
            checked.append([line.rstrip('\n'),word_def.encode('UTF-8')])
        except TypeError:
            print "*****Wrong word(Longman): " + line.rstrip('\n')
            pass   
    openfile.close()
    
    outfilepath = os.path.join(exerpath,"def")
    outfile = os.path.join(outfilepath,openfile.name+'.def')
    
    if not os.path.exists(outfilepath):
        os.makedirs(outfilepath) 
        
    with open(outfile,'wb') as csvfile:
        swriter = csv.writer(csvfile,delimiter=',')
        swriter.writerows(checked)
        
    return checked

    
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('filename',type=file)
    parser.add_argument('-p','--pronunciation',help='Download audio',action='store_true')
    parser.add_argument('-d','--definition',help='Download definition and store it',action='store_true')
    args = parser.parse_args()
    
    if args.pronunciation:
        download_aud(args.filename)
    if args.definition:
        download_def(args.filename)
        
    
        

    
    
#    socks.setdefaultproxy(socks.PROXY_TYPE_SOCKS5, "127.0.0.1", 1080)
#    socket.socket = socks.socksocket
#    lock = thread.allocate_lock()
#        
#    exerpath = os.getcwd()
#    foldername = 'a_list'
##    foldername = sys.argv[1]
#    filepath = os.path.join(exerpath,foldername)
#    outfilepath = os.path.join(exerpath,foldername+'.def')
#    with open(outfilepath,'w') as out_f:
#        with open(filepath,'r') as in_f:
#            for line in in_f:
#                out_f.write(line.rstrip('\n')+': '+check.checkwords(str(line))[0]+'\n')
