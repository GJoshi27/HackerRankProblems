def fact(n):
    #print "isnide fact"
    if(n==0 or n==1):
        return 1

    return fact(n-1)*n

m=input()
for i in xrange(m):
    n=input()
    l=map(int,raw_input().split())
    d=dict()
    cnt=0
    for k in l:
        d[k]=d.get(k,0)+1
    #print d    
    for k,v in d.items():
        #print v
        if (v>1):
            cnt=cnt+v*(v - 1)
    print  cnt       


