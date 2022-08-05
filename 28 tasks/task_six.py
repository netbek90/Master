def PatternUnlock(N: int, hits: list) -> str:
    matrix = [[6, 1, 9], [5, 2, 8], [4, 3, 7]]
    def distance(a, b):
        index_a = [(row, col.index(a))
                   for row, col in enumerate(matrix) if a in col][0]
        index_b = [(row, col.index(b))
                   for row, col in enumerate(matrix) if b in col][0]

        return ((index_a[0] - index_b[0]) ** 2 + (index_a[1] - index_b[1]) ** 2) ** 0.5

    totalDistance = round(sum(distance(a, b) for a, b in zip(hits[:-1], hits[1:])), 5)

    if '0' in str(totalDistance):
        k = str(totalDistance).replace('0', '')
        return k
    else:
        return totalDistance