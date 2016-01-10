# Enter your code here. Read input from STDIN. Print output to STDOUT
m = input()  
ar = [int(i) for i in raw_input().strip().split()]
ar.sort()
#print ar
l=list()
minx=abs(ar[0]-ar[1])
l=[ar[0],ar[1]]
for k in xrange(1,m):
    if(k+1==m):
        break
    current=abs(ar[k]-ar[k+1])
    t=k,k+1
    if minx>current :
        minx=current
        l=[ar[k],ar[k+1]]
    elif (minx==current):
        l.append(ar[k])
        l.append(ar[k+1])
print " ".join(map(str,l))
