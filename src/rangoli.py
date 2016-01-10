N=int(raw_input())
x=N*2-1
y=x
msg="abcdefghijklmnopqrstuvwxyz"
i=0
while i < N: 
    j=1
    msgout=""
    while j < x:
        msgout=msgout+"-"
        #print "-",
        j=j+1
    spc=j    
    k=N-1
    if i==0:
        #print msg[k],
        msgout=msgout+msg[k]
        cnt=1
    else:
        j=1
        p=0
        while p < cnt:
            if j%2!=0:
                 msgout=msgout+msg[k]
                 #print msg[k],
            else:
                 #print '-',
                 msgout=msgout+"-"
                 k=k-1
            j=j+1
            p=p+1
        p=1
        j=1
        while p < cnt:
            if j%2!=0:
                #print '-',
                msgout=msgout+"-"
            else:
                #print msg[k+1],
                msgout=msgout+msg[k+1]
                k=k+1
            j=j+1
            p=p+1
    j=1
    k=1
    while k < spc:
        #print '-',
        msgout=msgout+"-"
        k=k+1
    x=x-2
    i=i+1
    cnt=cnt+2
    print msgout

x=N*2-1
y=x
i=1
spc=2
cnt=cnt-2
#print "cnt",cnt
while i < N: 
    j=1
    msgout=""
    while j <= spc:
        #print '-',
        msgout=msgout+"-"
        j=j+1

    k=N-1
    if i==N-1:
        #print msg[k],
        msgout=msgout+msg[k]
    else:
        j=1
        p=0
        while p < cnt-2:
            if j%2!=0:
                 #print msg[k],
                 msgout=msgout+msg[k]
            else:
                 #print '-',
                 msgout=msgout+"-"
                 k=k-1
            j=j+1
            p=p+1
        p=1
        j=1
        #print "out"
        while p < cnt-2:
            if j%2!=0:
                #print '-',
                msgout=msgout+"-"
            else:
                #print msg[k+1],
                msgout=msgout+msg[k+1]
                k=k+1
            j=j+1
            p=p+1

    j=1
    while j <= spc:
        #print '-',
        msgout=msgout+"-"
        j=j+1

    spc=spc+2    
    cnt=cnt-2
    i=i+1
    print msgout 

