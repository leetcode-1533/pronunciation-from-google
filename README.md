# pronunciation-from-google

##Current Usage:

Hi, I create this repo completely for personal usage. And it has been half a year since I finish my GRE exam. I would say this repo somehow helped me. It can render words into CSV format for me to print and save in the phone, check the pronunciation and images(not fully developed). But I have to admit I spent more time than I should in developing this, because I should have put GRE in the first place.

Anyway, after half a year, I was happy to see that this project is still working. For now, I would recommend use 'python dictionary.py check_m17' to check new vocabularies.


##Stale information:
This script will download English Vocabulary pronunciation from "https://ssl.gstatic.com/dictionary/static/sounds/de/0/"

##Usage:

  python v2a.py file
  
Where file is the vocabulary file name containing list of the words you want the program to download, one at each line. 

A folder called "audio" will be created at the same directory as the script. 

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
