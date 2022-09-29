#for order 2 and 3
a=[[ 2,-3, 5],
   [ 6, 0, 4],
   [ 1, 5,-7]]
#m x n
m=len(a); n=len(a[0])
if m==n:
    if m!=2:
        print('Calculating Adjoint...',end='\n\n')
    #Co-factors...
        C=[]
        for h in range(m):
            tmpC=[]
            for i in range(m):
                subM=[]
                for k in range(m):
                    if h != k:
                        tmp=[]
                        for j in range(m):
                            if j != i:
                                elem= a[k][j]
                                tmp.append(elem)
                        subM.append(tmp)
                det_subM=(subM[0][0]*subM[1][1]-subM[0][1]*subM[1][0])
                tmpC.append(det_subM*(-1)**(h+i+2))
            C.append(tmpC)
    #Transposing...
        T=[]
        for i in range(m):
            tmpT=[]
            for j in range(m):
                tmpT.append(C[j][i])
            T.append(tmpT)
    #Printing...
        for i in T:
            print('[',end='')
            for j in i:
                print(f'{str(j).rjust(4)}',end='')
            print(' ]')
    else:
        print('Find Yourself :)')
else:
    print('Adjoint not Possible')
