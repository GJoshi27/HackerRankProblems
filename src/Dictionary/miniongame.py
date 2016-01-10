import re

def substring(A,X):
    match = re.findall('(?='+X+')',A)
    #print len(match)
    return len(match)

CONSONANTS="bcdfghjklmnpqrstvwxyz".upper()
VOWELS="aeiou".upper()
#print VOWELS
#print CONSONANTS
string=raw_input()
l=len(string)
lst=list()
for i in range(l):
    lst.append(string[i])
#print lst
s=set(lst)
dictvow=dict()
dictcon=dict()
for val in s:
    #print val
    if CONSONANTS.find(val) != -1 :
        patt=val
        idx=string.find(patt)
        while True :
            dictcon[patt]=dictcon.get(patt,0) + substring(string,patt)
            idx=idx+1
            sz=len(patt)
            if(sz==l or (string.find(patt)+sz >=l)) :
                break
            patt=patt+string[idx]
            #print patt
    else:
        patt=val
        idx=string.find(patt)
        while  True:
            dictvow[patt]=dictvow.get(patt,0) + substring(string,patt)
            #print "idx",idx
            idx=idx+1
            sz=len(patt)
            if(sz==l or (string.find(patt)+sz >=l)) :
                break
            patt=patt+string[idx]
            #print patt

#print dictcon
#print dictvow
consum=sum([ v for  k,v in dictcon.items()]) 
vowsum=sum([ v for  k,v in dictvow.items()]) 
if consum==vowsum:
    print "DRAW"
elif consum > vowsum    :
    print "Stuart",consum
else:
    print "Kevin",vowsum



