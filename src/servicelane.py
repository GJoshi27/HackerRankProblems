#!/bin/python
import sys
n,t = raw_input().strip().split(' ')
n,t = [int(n),int(t)]
width = map(int,raw_input().strip().split(' '))
#print width
for a0 in xrange(t):
    i,j = raw_input().strip().split(' ')
    #print  i,j
    i,j = [int(i),int(j)]
    minx=4
    while ( i <= j):
        if(width[i]< minx):
            minx=width[i]
        i=i+1    
    print minx        




