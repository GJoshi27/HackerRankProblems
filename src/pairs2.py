n,k=map(int,raw_input().split())
l=map(int,raw_input().split())
ans=0
for i in l:
        if i+k in l:
                ans+=1
print ans

