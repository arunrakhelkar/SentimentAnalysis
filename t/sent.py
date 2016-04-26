import json

data = []
with open('a.txt') as f:
    for line in f:
            data.append(json.loads(line))
    
    answer = []
    for i in data:
    	    data = str(i[u'text'])
	    label = str(i['label'])
    	    print repr(data)+"\t"+(label)
	    print ""
#temp = ''.join([i[u'text']])
#   	    answer.append(temp)
#   print answer
#print i[u'text']print"\t"
#	    print i[u'_id']
#	    print ""

