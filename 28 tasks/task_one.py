N=int(input)
def squirrel(N):
    if N>0:
        k=1
        while N>1:
            k*=N
            N-=1
        return str(k)[0]
    return("N<=0!")

print(squirrel(N))

