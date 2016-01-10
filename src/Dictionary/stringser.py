msg=raw_input()
sea=raw_input()
count=0
l=len(sea)
j=0
i=0
while i < len(msg):
    if msg[i]==sea[j]:
        j=j+1
    else:
        j=0
    if (j==l):
        count=count+1
        i=i-1
        j=0
    i=i+1    
print count
