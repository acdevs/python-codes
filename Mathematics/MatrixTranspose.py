#for order 2 and 3
a=[[ 2,-3, 5],
   [ 6, 0, 4],
   [ 1, 5,-7]]
#m x n
m=len(a); n=len(a[0])
print('Calculating Transpose...',end='\n\n')
T=[]
for i in range(m):
    tmpT=[]
    for j in range(n):
        tmpT.append(a[j][i])
    T.append(tmpT)
for i in T:
    print('[',end='')
    for j in i:
        print(f'{str(j).rjust(3)}',end='')
    print(' ]')
