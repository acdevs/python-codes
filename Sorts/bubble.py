def bubble(*x):
    for i in range(len(x)):
        for j in range(len(x)-i-1):
            if x[j]>x[j+1]:
                x[j],x[j+1]=x[j+1],x[j]
    return x
                
