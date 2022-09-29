x=int(input('size number= '))
spc=x
for i in range(1,2*x,2):
    spc=spc-1
    print(' '*spc+'*'*i)
