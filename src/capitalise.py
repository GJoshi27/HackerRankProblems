import re
msg=raw_input()
msg1=msg.split(' ')
print msg1
l=len(msg1)
out=""
for i in xrange(l-1):
    out=out + msg1[i].capitalize() +' '
out=out+msg1[l-1].capitalize()    
print out    
