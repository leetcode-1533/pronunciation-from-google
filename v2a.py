#!/Users/y1275963/anaconda/bin/python

import socks
import socket
import sys

import urllib2
import os
import thread

exerpath = '/Users/y1275963/Desktop/v2a'
foldername = sys.argv[1]

class audio:
    def __init__(self,foldername,word):
        
        self.title = word
        
        self.g_path = "https://ssl.gstatic.com/dictionary/static/sounds/de/0/"
        self.mp3_path = self.g_path + word + ".mp3"
        self.loc = os.path.join(exerpath,"audio",foldername)
        
        if not os.path.exists(self.loc):
            os.makedirs(self.loc)  
            
        self.mp3_download()
        
        
    def mp3_download(self):    
        try:
            mp3 = urllib2.urlopen(self.mp3_path)
            open(os.path.join(self.loc,self.title)+'.mp3','wb').write(mp3.read())
            print "Downloaded", self.title
        except:
            print "Wrong Word:", self.title   
            print self.mp3_path


if __name__ == "__main__":
    socks.setdefaultproxy(socks.PROXY_TYPE_SOCKS5, "127.0.0.1", 1080)
    socket.socket = socks.socksocket
    
    lock = thread.allocate_lock()
    
    with open(os.path.join(exerpath,foldername)) as f:
        for line in f:
            lock.acquire()
            aud = str(line)
            audio(foldername,aud.strip())
            lock.release()

    
    
#    au = raw_input('vacubolary ')
#    audio(str(au))
