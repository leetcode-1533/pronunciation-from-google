# pronunciation-from-google

This script will download English Vocabulary Prounciation from "https://ssl.gstatic.com/dictionary/static/sounds/de/0/"

##Usage:

  python v2a.py file
  
Where file is the vocabulary file name containing list of the words you want the program to download, one at each line. 

A folder called "audio" will be created at the the same directory as the script. 

And a subfolder will be created under folder "audio" using the name of the vocabulary file name.

##Needed Modification:

  1. Due to GFW, I used sockets proxy, pleaes remove:
      import socks
      import socket
    and 
      socks.setdefaultproxy(socks.PROXY_TYPE_SOCKS5, "127.0.0.1", 1080)
      socket.socket = socks.socksocket


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
    
  Personally, this script is for the conquering of GRE. I used it to facilitate creating course for memrise.com, where to create a course an audio for each word must be provided.
