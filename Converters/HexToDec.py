n=input('hex number').lower()
lt=list(n)
s=0
for i in range(len(lt)):
    hex=['a','b','c','d','e','f']
    for j in hex:
        if j in lt:
            lt[lt.index(j)]=(10+s)
        s+=1
lt.reverse()
p=0
dec=0
for k in lt:
   dec+=int(k)*16**p
   p+=1
print(lt,dec)
