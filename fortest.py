import sys
import re
import os

doc_num = len(open('data-bin/cnndm41.tokenized.en-de/test.len.de').readlines())
filew = open('data-bin/cnndm41.tokenized.en-de/test.len.de','w')

for i in range(doc_num):
	filew.write(sys.argv[1]+'\n')
filew.close()
