a=[[ 2,1],
   [ 3,2],
   [-1,1]]
#m x n
m=len(a); n=len(a[0])
b=[[ 1,0],
   [-1,2],
   [ 2,3]]
#p x q
p=len(b); q=len(b[0])
if m==p and n==q:
    print('Calculating Addition...',end='\n\n')
    x=[]
    for i in range(m):
        tmp=[]
        for j in range(n):
            elem=a[i][j]+b[i][j]
            tmp.append(elem)
        x.append(tmp)
    for i in x:
        print('[',end='')
        for j in i:
            print(f'{str(j).rjust(3)}',end='')
        print(' ]')
else:
    print('Matrix addition not possible!')
