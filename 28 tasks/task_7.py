def WordSearch(len:int, s:str, subs:str)->int:
    import textwrap
    if ' ' in s:
        output = textwrap.wrap(s,len,break_long_words=False, break_on_hyphens=False)
        k=[]
        for i in output:
            for j in i.split(sep=" "):
                if j==subs:
                    k.append(1)
            k.append(0)
        temp=[]
        for idx, value in enumerate(k):
            if value == 1:
                temp.append(idx)
        for o in temp[::-1]:
            k.pop(o+1)
        return k
    output = textwrap.wrap(s, len, break_long_words=True, break_on_hyphens=True)
    k = []
    for i in output:
        if i == subs:
            k.append(1)
        else:
            k.append(0)
    return k