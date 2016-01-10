raw_input();m=raw_input().split()
raw_input();n=raw_input().split()
print "\n".join(sorted(list(set(m)^set(n)),key=int))
