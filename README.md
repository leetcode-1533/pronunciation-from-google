# pronunciation-from-google

This script will download English Vocabulary Prounciation from "https://ssl.gstatic.com/dictionary/static/sounds/de/0/"

##Usage:

  python v2a.py file
  
Where file is the list of the words you want the program to download, one at each line. 

##Needed Modification:
1. Due to GFW, I used sockets proxy, pleaes remove:
    import socks
    import socket
and 
    socks.setdefaultproxy(socks.PROXY_TYPE_SOCKS5, "127.0.0.1", 1080)
    socket.socket = socks.socksocket

2. exerpath is the variable of the absolute path of the script, after execution, a subfolder called "audio" will be created under this path.

##Sample output:
    [~/Desktop/v2a y1275963$]python v2a.py a1
    Downloaded abase
    Downloaded abash
    Downloaded abet
    Downloaded abhor
    Downloaded abiding
    Downloaded abnegate
    Downloaded abominate
    Downloaded anomalous
    Downloaded aboveboard
    Downloaded abrade
    Downloaded abridge
    Downloaded absolve
    Downloaded abstain
    Downloaded abstruse
    Downloaded absurd
    
  Personally, this script this for the conquering of GRE. I used it to facilitate creating course for memrise.com. Where you have to provide audio for each words.
