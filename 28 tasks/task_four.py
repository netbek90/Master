def MadMax(N:int,Tele:list)->list:
    C=int((N-1)/2)
    Tele=(sorted(Tele)[0:C]+sorted(Tele)[:C-1:-1])
    return Tele