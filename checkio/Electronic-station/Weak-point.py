def weak_point(matrix):
    N = len(matrix)
    rowRlist = []
    colRlist = []
    for n in range(0, N):
        rowRlist.append(sum(matrix[n]))
        col = 0
        for m in range(0, N):
            col += matrix[m][n]
        colRlist.append(col)
    print(rowRlist, colRlist)

    return [rowRlist.index(min(rowRlist)), colRlist.index(min(colRlist))]


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert isinstance(weak_point([[1]]), (list, tuple)), "The result should be a list or a tuple"
    assert list(weak_point([[7, 2, 7, 2, 8],
                            [2, 9, 4, 1, 7],
                            [3, 8, 6, 2, 4],
                            [2, 5, 2, 9, 1],
                            [6, 6, 5, 4, 5]])) == [3, 3], "Example"
    assert list(weak_point([[7, 2, 4, 2, 8],
                            [2, 8, 1, 1, 7],
                            [3, 8, 6, 2, 4],
                            [2, 5, 2, 9, 1],
                            [6, 6, 5, 4, 5]])) == [1, 2], "Two weak point"
    assert list(weak_point([[1, 1, 1],
                            [1, 1, 1],
                            [1, 1, 1]])) == [0, 0], "Top left"


# 更简单的解法
def weak_point(matrix):
    x = [sum(x) for x in matrix]
    y = [sum(x) for x in zip(*matrix)]
    return x.index(min(x)), y.index(min(y))
