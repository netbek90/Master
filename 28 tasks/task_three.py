def ConquestCampaign(N:int, M:int, L:int, battalion:list)-> int:
    matrix = [[0] * M for i in range(N)]
    battalion=[i-1 for i in battalion]
    for i in range(len(battalion)):
        if i % 2 == 0 and i<len(battalion):
            matrix[battalion[i]][battalion[i+1]]=1
    x_list=[]
    y_list=[]
    for x in battalion[1::2]:
        x_list.append(x)
    for y in battalion[::2]:
        y_list.append(y)
    def neighbors(x, y,matrix=matrix):
        if x + 1 < len(matrix[0]):
            matrix[y][x + 1]=1
            y_list.append(y)
            x_list.append(x + 1)
        if x - 1 >= 0:
            matrix[y][x - 1]=1
            y_list.append(y)
            x_list.append(x - 1)
        if y + 1 < len(matrix):
            matrix[y + 1][x]=1
            y_list.append(y+1)
            x_list.append(x)
        if y - 1 >= 0:
            matrix[y - 1][x]=1
            y_list.append(y - 1)
            x_list.append(x + 1)
        return matrix


    round=1
    while any(0 in x for x in matrix):
        round+=1
        for i in range(len(x_list)):
            if any(0 in x for x in matrix):
                try:
                    neighbors(x_list[i],y_list[i])
                except:
                    continue
    return round