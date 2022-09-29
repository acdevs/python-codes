x=int(input('size number= '))
spc=x
inn=0
f=0
for i in range(1,2*x,2):
    spc=spc-1
    print(' '*spc+'*'+' '*inn+'*'*f)
    k=i-2
    inn=inn+2
    if inn==2 and f==0:
        inn=1;f=1
    imx=inn-2
f=1
for j in range(k,0,-2):
    if imx==1:
        f=0
    spc=spc+1
    imx=imx-2
    print(' '*spc+'*'+' '*imx+'*'*f)
    
