import re
N=input()
ls=list()
for i in range(N):
    link=raw_input()
    out=re.findall('href=\"(.+?)\"',link)
    #out1=re.findall('href=\".*\">[<hb1-9]*([a-zA-Z\s]+)',link)
    out1=re.findall('href=\".*\"[^>]*>(.*?)</a',link)
    #print out1
    if len(out) > 0 or len(out1) > 0:
        ans=out[0]+','+out1[0]
        print ans
