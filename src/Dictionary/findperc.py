a=int(raw_input())
dicdata=dict()
for i in range(a):
    inp=raw_input()
    data=inp.split()
    print data
    avg=(int(data[1])+int(data[2])+int(data[3]))/3
    print avg
    dicdata[data[0]]=dicdata.get(data[0],0)+avg

name=raw_input()
ans=float(dicdata.get(name))
print ('%.2f'%ans)

