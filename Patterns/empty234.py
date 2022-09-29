n=int(input('size: '))
p=n//2+1
spc=0
chr=0
for i in range(1,p+1):
    print('*'+' '*spc+'*'*chr)
    if chr==0:
        chr+=1
    if i<2:
        spc=0
        continue
    spc+=1
spc=spc-1
for j in range(p-1,0,-1):
    spc-=1
    if j==1: chr=0
    if j==2: spc=0
    print('*'+' '*spc+'*'*chr)
