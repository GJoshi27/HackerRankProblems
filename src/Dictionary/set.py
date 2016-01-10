N=int(raw_input())
s=set(map(int,raw_input().split()))
print sum([k for k in s])/float(len(s))

