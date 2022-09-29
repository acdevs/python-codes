#for order 2 and 3
a=[[ 2,-3, 5],
   [ 6, 0, 4],
   [ 1, 5,-7]]
#m x n
m=len(a); n=len(a[0])
if m==n:
    print('Calculating Determinant...',end='\n')
    if m!=2:
        D=0
        for i in range(m):
            subM=[]
            for k in range(1,m):
                tmp=[]
                for j in range(m):
                    if j != i:
                        elem= a[k][j]
                        tmp.append(elem)
                subM.append(tmp)
            M=subM[0][0]*subM[1][1]-subM[0][1]*subM[1][0]
            D+=a[0][i]*M*(-1)**(i+2)
    else:
        D=(a[0][0]*a[1][1]-a[0][1]*a[1][0])
    print(D)
else:
    print('Determinant not possible!')
