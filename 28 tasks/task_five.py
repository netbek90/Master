def SynchronizingTables(N:int, ids:list, salary:list)->list:
    ids2 = sorted(ids)
    salary2 = sorted(salary)
    dic = dict(zip(ids2, salary2))
    lst = []
    for i in ids:
        lst.append(dic[i])
    return lst