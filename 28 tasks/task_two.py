def odometer(N:list)->int:
    k=0
    K=[N[i] for i in range(len(N)) if i%2!=0]
    if len(K)>1:
        diff = [K[n]-K[n-1] for n in range(1,len(K))]
        diff.insert(0,K[0])
    else:
        diff=K
    try:
        for i,j in zip(diff,N[::2]):
            k+=i*j
        return k
    except:
        return k