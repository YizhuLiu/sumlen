import sys
import re 
import os

#class_ = sys.argv[1]

for class_ in ['train','valid','test']:
    fileread = open('data/cnndm41.tokenized.en-de/'+class_+'.de')
    filewrite = open('data/cnndm41.tokenized.en-de/'+class_+'.len.de','w')
    for line in fileread.readlines():
	    filewrite.write(str(len(line.strip().split(' ')))+'\n')
    filewrite.close()
