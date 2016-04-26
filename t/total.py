import json

data = []
with open('b.txt') as f:
    for line in f:
            data.append(line)
    
    answer = []
    for i in data:
    	    if not i['label'] == 1:
    	        print i
	        print ""
#temp = ''.join([i[u'text']])
#   	    answer.append(temp)
#   print answer
#print i[u'text']print"\t"
#	    print i[u'_id']
#	    print ""

