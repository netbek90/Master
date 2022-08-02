def MadMax(N:int,Tele:list)->list:
    C=int((N-1)/2)
    temp=(sorted(Tele)[0:C]+[max(Tele)])
    Tele=temp+sorted([i for i in Tele[C:]],reverse=True)
    return Tele