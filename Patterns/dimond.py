x=int(input('size number, except 0= '))
spc=x
for i in range(1,2*x,2):
    spc=spc-1
    print(' '*spc+'*'*i)
    k=i-2
for j in range(k,0,-2):
    spc=spc+1
    print(' '*spc+'*'*j)
