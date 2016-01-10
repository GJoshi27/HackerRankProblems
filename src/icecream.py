for k in range(int(raw_input())):
    M=input()
    N=input()
    ar=map(int,raw_input().split())
    l=list()
    d=dict()
    for i in range(N):
        d[ar[i]]=i

    #print d
    an=0
    for i in range(N):
        if (d.get(M-ar[i])!=i):
            #print "in"
            l=[i+1,d.get(M-ar[i])+1]
            break
    print  " ".join(map(str,l))     



