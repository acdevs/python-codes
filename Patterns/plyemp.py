x=int(input('size number= '))
f=r=0
for i in range(1,2*x,2):
    print(' *'+' '*f+'*'*r)
    f=f+2
    if f==2:
        f=1;r=1
    k=i-2
    fmx=f-4
for j in range(k,0,-2):
    print(' *'+' '*fmx+'*'*r)
    fmx=fmx-2
    if fmx==-1:
        r=0
