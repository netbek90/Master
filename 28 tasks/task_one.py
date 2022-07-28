def squirrel(N: int) -> int:
    if N>0:
        k=1
        while N>1:
            k*=N
            N-=1
        return int(str(k)[0])
    return("N<=0!")

