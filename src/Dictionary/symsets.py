raw_input()
S=set(map(int,raw_input().split()))
#print S
raw_input()
Q=set(map(int,raw_input().split()))
#print Q
sint=S.intersection(Q)
sunion=S.union(Q)
sunion=sunion.difference(sint)
# print S^Q
lS=list(sunion)
#print lS
lS.sort()
#print (lambda x:print (x,end="\n"),for i in xrange(len(lS)))
for i in range(len(lS)):
    print lS[i]
