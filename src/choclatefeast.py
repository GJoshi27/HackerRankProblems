#!/bin/python

import sys


t = int(raw_input().strip())
for a0 in xrange(t):
    n,c,m = raw_input().strip().split(' ')
    n,c,m = [int(n),int(c),int(m)]
    nc=n/c
    wrap=nc
    while(wrap >= m):
        morC=wrap/m
        wrap=morC+wrap%m
        nc=nc+morC
    print nc    
