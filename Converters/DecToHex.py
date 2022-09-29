n=int(input('dec number'))
s=0
i=0
h=''
while n>0:
    d=n%16
    hex=[10,11,12,13,14,15]
    for j in hex:
        if d==j:
            d=chr(65+j-10)
    h=str(d)+h
    n//=16
print(h)
