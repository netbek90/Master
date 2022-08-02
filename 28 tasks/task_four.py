def MadMax(N:int,Tele:list)->list:
    if N>2:
        C=int((N-1)/2)
    else:
        C=N
    Tele=(sorted(Tele)[0:C]+sorted(Tele)[:C-1:-1])
    return Tele