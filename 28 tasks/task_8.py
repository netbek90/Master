def SumOfThe(N:int, data:list)->int:
    for i in data:
        data2=data.copy()
        data2.pop(data.index(i))
        if sum(data2)==i:
            return i


