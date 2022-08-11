def WordSearch(len:int, s:str, subs:str)->int:
    import textwrap
    output = textwrap.wrap(s,len,break_long_words=False, break_on_hyphens=False)
    k=[]
    for i in output:
        for j in i.split(sep=" "):
            if j==subs:
                k.append(1)
            k.append(0)
    return k

