m=input()
list1=map(int,raw_input().split())
n=input()
list2=map(int,raw_input().split())
list1.sort()
list2.sort()
d1=dict()
for k in list1:
    d1[k]=d1.get(k,0)+1

d2=dict()
for k in list2:
    d2[k]=d2.get(k,0)+1

l=list()
for k,v in d1.items():
    val=d2.get(k)
    if(v-val!=0):
        l.append(k)

l.sort()
print " ".join(map(str,l))

