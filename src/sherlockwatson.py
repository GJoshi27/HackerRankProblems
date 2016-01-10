N,K,Q=map(int,raw_input().split())
ar=map(int,raw_input().split())
if(K%N!=0):
    K=K%N
    arr=ar[N-K:N]+ar[:N-K]
#print arr
for k in xrange(Q):
    q=int(raw_input())
    print arr[q]
