import json

data = []
with open('b.txt') as f:
    for line in f:
    	    j=line.split('":')
	    g = j[3].replace(',"label','')
	    g=g.replace('"','')
#print g
	    data.append(g)
    
#   answer = []
    for i in data:
   	    j = str(i)
    	    print (j)
#print ""
#temp = ''.join([i[u'text']])
#   	    answer.append(temp)
#   print answer
#print i[u'text']print"\t"
#	    print i[u'_id']
#	    print ""

