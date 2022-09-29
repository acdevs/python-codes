#for order 2 and 3
a=[[ 1,3,3],
   [ 1,4,3],
   [ 1,3,4]]
#m x n
m=len(a); n=len(a[0])
if m==n:
    print('Calculating Inverse...',end='\n\n')
    if m!=2:
    #Determinant...
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
        if D != 0:
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
        #Transposing & Inversing...
            T=[]
            for i in range(m):
                tmpT=[]
                for j in range(m):
                    tmpT.append(round(C[j][i]/D,2))
                T.append(tmpT)
        #Printing...
            for i in T:
                print('[',end='')
                for j in i:
                    print(f'{str(j).rjust(7)}',end='')
                print(' ]')
        else:
            print("Determinant=0, Inverse doesn't exists")
    else:
        print('Find Yourself :)')
else:
    print('Inverse not possible!')
