raw_input();ls=map(int,raw_input().split())
ls.sort(reverse=True)
#print ls
lset=list(set(ls))
lset.sort(reverse=True)
print lset[1]
