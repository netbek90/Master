def squirrel(N: int) -> int:
    if N==1 or N==0:
        return 1
    elif N>1:
        k=1
        while N>1:
            k*=N
            N-=1
        return int(str(k)[0])
    return("N<0!")
