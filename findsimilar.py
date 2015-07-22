#!/Users/y1275963/anaconda/bin/python
import sys
import Levenshtein
import numpy

reload(sys)  
sys.setdefaultencoding('utf8')

datafile = 'wiki-100k.txt'
data = []
for line in open(datafile):
    if not line.startswith('#'):
        data.append(line.rstrip())

dis = []
for item in data:
    dis.append(Levenshtein.distance(sys.argv[1],item))


vals = numpy.array(dis)
for item in vals.argsort()[:int(sys.argv[2])]:
    print data[item]
 
