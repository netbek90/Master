import copy


def ConquestCampaign(N: int, M: int, L: int, battalion: list) -> int:
    matrix = [[0] * M for i in range(N)]
    battalion = battalion[::-1]
    battalion_new = []

    for i in range(L):
        x = battalion.pop() - 1
        y = battalion.pop() - 1

        matrix[x][y] = 1

        battalion_new.append((x, y))

    matrix_new = copy.deepcopy(matrix)
    count = 1

    while not all([all([s == 1 for s in i]) for i in matrix]):

        for row_num in range(len(matrix)):
            for square_num in range(len(matrix[row_num])):

                if matrix[row_num][square_num] == 1:
                    for con in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                        try:
                            if (row_num + con[0]) >= 0 and (square_num + con[1]) >= 0:
                                matrix_new[row_num + con[0]][square_num + con[1]] = 1
                        except IndexError:
                            pass


        matrix = copy.deepcopy(matrix_new)
        count += 1
    return count