N=int(raw_input())
ls=list()
for i in range(N):
    name=raw_input()
    marks=float(raw_input())
    lsN=[name,marks]
    ls.append(lsN)
    #print ls[i]
#s=set([marks for name,marks in ls])
#print s
#lsT=list(set)
#print lsT
second_highest = sorted(list(set([marks for name, marks in ls ])))[1]
print('\n'.join([a for a,b in sorted(ls) if b == second_highest]))

