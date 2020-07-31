import sys
import re
import os

filewrite = open('settings.xml','w')
writestring ='<ROUGE_EVAL version="1.55">\n'
for filename in os.listdir('models'):
    number = filename
    each = '<EVAL ID="'+number+'">\n\t<MODEL-ROOT>\n\t/home/yizhu/anaconda2/'+sys.argv[1]+'/models\n\t</MODEL-ROOT>\n'+'\t<PEER-ROOT>\n\t/home/yizhu/anaconda2/'+sys.argv[1]+'/systems\n\t</PEER-ROOT>\n'+'\t<INPUT-FORMAT TYPE="SPL">\n\t</INPUT-FORMAT>\n'+'\t<PEERS>\n\t\t<P ID="S">'+number+'</P>\n\t</PEERS>\n'+'\t<MODELS>\n\t\t<M ID="T">'+filename+'</M>\n\t</MODELS>\n</EVAL>\n\n'
    writestring+=each

writestring+='</ROUGE_EVAL>'
filewrite.write(writestring)
filewrite.close()
