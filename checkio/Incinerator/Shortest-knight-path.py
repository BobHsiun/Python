import copy


def checkio(cells):
    startP = [cells[0], int(cells[1])]
    endP = [cells[3], int(cells[4])]
    resultList = [[startP]]
    print("===", startP, endP, resultList)
    result = 0
    n = 0
    while result == 0:
        newresultList = []
        for r in resultList:
            currentL = r
            currentR = r[-1]
            # print("循环",resultList,currentL,currentR)
            if ord(currentR[0]) - 1 >= ord("a"):
                if currentR[1] - 2 >= 1 and [chr(ord(currentR[0]) - 1), currentR[1] - 2] not in currentL:
                    currentL.append([chr(ord(currentR[0]) - 1), currentR[1] - 2])
                    newresultList.append(copy.deepcopy(currentL))
                    currentL.remove([chr(ord(currentR[0]) - 1), currentR[1] - 2])
                if currentR[1] + 2 <= 8 and [chr(ord(currentR[0]) - 1), currentR[1] + 2] not in currentL:
                    currentL.append([chr(ord(currentR[0]) - 1), currentR[1] + 2])
                    newresultList.append(copy.deepcopy(currentL))
                    currentL.remove([chr(ord(currentR[0]) - 1), currentR[1] + 2])
            if ord(currentR[0]) + 1 <= ord("h"):
                if currentR[1] - 2 >= 1 and [chr(ord(currentR[0]) + 1), currentR[1] - 2] not in currentL:
                    currentL.append([chr(ord(currentR[0]) + 1), currentR[1] - 2])
                    newresultList.append(copy.deepcopy(currentL))
                    currentL.remove([chr(ord(currentR[0]) + 1), currentR[1] - 2])
                if currentR[1] + 2 <= 8 and [chr(ord(currentR[0]) + 1), currentR[1] + 2] not in currentL:
                    currentL.append([chr(ord(currentR[0]) + 1), currentR[1] + 2])
                    newresultList.append(copy.deepcopy(currentL))
                    currentL.remove([chr(ord(currentR[0]) + 1), currentR[1] + 2])
            if ord(currentR[0]) - 2 >= ord("a"):
                if currentR[1] - 1 >= 1 and [chr(ord(currentR[0]) - 2), currentR[1] - 1] not in currentL:
                    currentL.append([chr(ord(currentR[0]) - 2), currentR[1] - 1])
                    newresultList.append(copy.deepcopy(currentL))
                    currentL.remove([chr(ord(currentR[0]) - 2), currentR[1] - 1])
                if currentR[1] + 1 <= 8 and [chr(ord(currentR[0]) - 2), currentR[1] + 1] not in currentL:
                    currentL.append([chr(ord(currentR[0]) - 2), currentR[1] + 1])
                    newresultList.append(copy.deepcopy(currentL))
                    currentL.remove([chr(ord(currentR[0]) - 2), currentR[1] + 1])
            if ord(currentR[0]) + 2 <= ord("h"):
                if currentR[1] - 1 >= 1 and [chr(ord(currentR[0]) + 2), currentR[1] - 1] not in currentL:
                    currentL.append([chr(ord(currentR[0]) + 2), currentR[1] - 1])
                    newresultList.append(copy.deepcopy(currentL))
                    currentL.remove([chr(ord(currentR[0]) + 2), currentR[1] - 1])
                if currentR[1] + 1 <= 8 and [chr(ord(currentR[0]) + 2), currentR[1] + 1] not in currentL:
                    currentL.append([chr(ord(currentR[0]) + 2), currentR[1] + 1])
                    newresultList.append(copy.deepcopy(currentL))
                    currentL.remove([chr(ord(currentR[0]) + 2), currentR[1] + 1])
        n += 1
        resultList = copy.deepcopy(newresultList)
        print("循环" + str(n) + "次：", resultList, "\n-----------------------\n")
        for i in resultList:
            if endP in i:
                result = n
                break
    return n


if __name__ == "__main__":
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio("b1-d5") == 2, "1st example"
    assert checkio("a6-b8") == 1, "2nd example"
    assert checkio("h1-g2") == 4, "3rd example"
    assert checkio("h8-d7") == 3, "4th example"
    assert checkio("a1-h8") == 6, "5th example"
