import socks
import socket

import urllib2
import os

class audio:
    def __init__(self,word):
        
        self.title = word

        self.g_path = "https://ssl.gstatic.com/dictionary/static/sounds/de/0/"
        self.mp3_path = self.g_path + word + ".mp3"
        self.loc = "/Users/y1275963/Desktop/v2a/audio"
        
        self.mp3_download()
        
        
    def mp3_download(self):
        try:
            mp3 = urllib2.urlopen(self.mp3_path)
            open(os.path.join(self.loc,self.title)+'.mp3','wb').write(mp3.read())
            print "Downloaded", self.title
        except:
            print "Wrong Word", self.title   

if __name__ == "__main__":
    socks.setdefaultproxy(socks.PROXY_TYPE_SOCKS5, "127.0.0.1", 1080)
    socket.socket = socks.socksocket
    
    au = raw_input('vacubolary ')
    audio(str(au))