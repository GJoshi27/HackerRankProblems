#!/bin/python

m = input()
ar = [int(i) for i in raw_input().strip().split()]
pivot=ar[0]
small=[]
big=[]
for i in xrange(1,m):
    if ar[i] < pivot:
        small.append(ar[i])
    else:
        big.append(ar[i])
    
small.sort()
big.sort()
print small
print big
ar.sort()
print ar

