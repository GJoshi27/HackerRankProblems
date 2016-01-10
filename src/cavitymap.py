#!/bin/python

import sys


n = int(raw_input().strip())
grid = []
grid_i = 0
for grid_i in xrange(n):
   grid_t = str(raw_input().strip())
   grid.append(grid_t)
print grid[0]
if n==1:
    exit()
for i in xrange(1,n-1):
    j=1
    msg=grid[i][j-1]
    #print msg
    while(j < n-1):
        #print grid[i][j]
        x=grid[i][j]
        if(x > grid[i-1][j] and x > grid[i][j-1] and x > grid[i+1][j] and x > grid[i][j+1]):
            msg=msg+"X"
            #grid[i][j]=str(x)
        else:
            msg=msg+x
        j=j+1 
    msg=msg+grid[i][j]
    print msg
print grid[n-1]
