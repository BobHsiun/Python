def checkio(matrix):
    setM = set()
    for l in matrix:
        setM = setM | set(l)
    print(setM, len(matrix))
    checkedList = []
    treslutList = []

    def spiderlist(x, y):
        resultn = matrix[x][y]
        n = len(checkedList)
        checkedList.append(str(x) + str(y))
        tempList = [str(x) + str(y)]
        while len(tempList):
            l = tempList
            tempList = []
            for i in l:
                if int(i[0]) - 1 >= 0 and matrix[int(i[0]) - 1][int(i[1])] == resultn and str(int(i[0]) - 1) + i[
                    1] not in checkedList:
                    tempList.append(str(int(i[0]) - 1) + i[1])
                    checkedList.append(str(int(i[0]) - 1) + i[1])
                if int(i[0]) + 1 < len(matrix) and matrix[int(i[0]) + 1][int(i[1])] == resultn and str(int(i[0]) + 1) + \
                        i[1] not in checkedList:
                    tempList.append(str(int(i[0]) + 1) + i[1])
                    checkedList.append(str(int(i[0]) + 1) + i[1])
                if int(i[1]) - 1 >= 0 and matrix[int(i[0])][int(i[1]) - 1] == resultn and i[0] + str(
                                int(i[1]) - 1) not in checkedList:
                    tempList.append(i[0] + str(int(i[1]) - 1))
                    checkedList.append(i[0] + str(int(i[1]) - 1))
                if int(i[1]) + 1 < len(matrix) and matrix[int(i[0])][int(i[1]) + 1] == resultn and i[0] + str(
                                int(i[1]) + 1) not in checkedList:
                    tempList.append(i[0] + str(int(i[1]) + 1))
                    checkedList.append(i[0] + str(int(i[1]) + 1))
        m = len(checkedList)
        return m - n

    while len(checkedList) != len(matrix) ** 2:
        for x in range(len(matrix)):
            for y in range(len(matrix)):
                if str(x) + str(y) not in checkedList:
                    treslutList.append([spiderlist(x, y), matrix[x][y]])
                    print(treslutList)
                else:
                    continue
    maxN = 0
    maxM = 0
    for n in treslutList:
        if n[0] > maxN:
            maxN = n[0]
            maxM = n[1]
            print(maxN, maxM)

    return [maxN, maxM]


checkio([
    [2, 1, 2, 2, 2, 4],
    [2, 5, 2, 2, 2, 2],
    [2, 5, 4, 2, 2, 2],
    [2, 5, 2, 2, 4, 2],
    [2, 4, 2, 2, 2, 2],
    [2, 2, 4, 4, 2, 2]
])
# These "asserts" using only for self-checking and not necessary for auto-testing
# if __name__ == '__main__':
#     assert checkio([
#         [1, 2, 3, 4, 5],
#         [1, 1, 1, 2, 3],
#         [1, 1, 1, 2, 2],
#         [1, 2, 2, 2, 1],
#         [1, 1, 1, 1, 1]
#     ]) == [14, 1], "14 of 1"
#
#     assert checkio([
#         [2, 1, 2, 2, 2, 4],
#         [2, 5, 2, 2, 2, 2],
#         [2, 5, 4, 2, 2, 2],
#         [2, 5, 2, 2, 4, 2],
#         [2, 4, 2, 2, 2, 2],
#         [2, 2, 4, 4, 2, 2]
#     ]) == [19, 2], '19 of 2'
