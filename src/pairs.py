m,d=map(int,raw_input().strip().split()) 
ar = [int(i) for i in raw_input().strip().split()] 
ar.sort()
cnt=0
l=0
r=1
while(r < len(ar)):
     cur=abs(ar[r]-ar[l])
     if(cur==d):
        cnt=cnt+1
        l=l+1
        r=r+1
     elif cur > d:
        l=l+1
        if(l==r):
            r=r+1
     else:
         r=r+1
print cnt        





