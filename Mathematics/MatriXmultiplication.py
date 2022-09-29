a=[[ 1],
   [ 2],
   [ 3],
   [ 4],
   [ 5],
   [ 6],
   [ 7],
   [ 8],
   [ 9],
   [ 10]]
#m x n
m=len(a); n=len(a[0])
b=[[ 11,12,13,14,15,16,17,18,19,20]]
#p x q
p=len(b); q=len(b[0])
if n==p:
    print('Calculating Product...',end='\n\n')
    x=[]
    for i in range(m):
        tmp=[]
        for j in range(q):
            sum_elem=0
            for k in range(n):
                sum_elem+= a[i][k]*b[k][j]
            tmp.append(sum_elem)
        x.append(tmp)
    for i in x:
        print('[',end='')
        for j in i:
            print(f'{str(j).rjust(4)}',end='')
        print(' ]')
else:
    print('Matrix product not possible!')
