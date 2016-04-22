def checkio(matrix):
    #判断行
    for l in matrix:
        for n1 in range(0,len(l)-3):
            if l[n1]==l[n1+1] and l[n1+1]==l[n1+2] and l[n1+2]==l[n1+3]:
                print("Row")
                return True
    #判断列
    for m1 in range(0,len(matrix)):
        for m2 in range(0,len(matrix[0])-3):
            if matrix[m2][m1]==matrix[m2+1][m1] and matrix[m2+1][m1]==matrix[m2+2][m1] and matrix[m2+2][m1]==matrix[m2+3][m1]:
                print("Col")
                return True
    #判断对角
    for x in range(0,len(matrix)-3):
        for y in range(0,len(matrix[0])-3):
            if matrix[y][x]==matrix[y+1][x+1]==matrix[y+2][x+2]==matrix[y+3][x+3]:
                print("Diagonal\\")
                return True
    for q in range(0,len(matrix)-3):
        N1=len(matrix)-1
        N2=len(matrix[0])-1
        for w in range(0,len(matrix[0])-3):
            if matrix[N1-q][w]==matrix[N1-q-1][w+1]==matrix[N1-q-2][w+2]==matrix[N1-q-3][w+3]:
                print("Diagona2\\")
                return True
    print("False")
    return False

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio([
        [1, 2, 1, 1],
        [1, 1, 4, 1],
        [1, 3, 1, 6],
        [1, 7, 2, 5]
    ]) == True, "Vertical"
    assert checkio([
        [7, 1, 4, 1],
        [1, 2, 5, 2],
        [3, 4, 1, 3],
        [1, 1, 8, 1]
    ]) == False, "Nothing here"
    assert checkio([
        [2, 1, 1, 6, 1],
        [1, 3, 2, 1, 1],
        [4, 1, 1, 3, 1],
        [5, 5, 5, 5, 5],
        [1, 1, 3, 1, 1]
    ]) == True, "Long Horizontal"
    assert checkio([
        [7, 1, 1, 8, 1, 1],
        [1, 1, 7, 3, 1, 5],
        [2, 3, 1, 2, 5, 1],
        [1, 1, 1, 5, 1, 4],
        [4, 6, 5, 1, 3, 1],
        [1, 1, 9, 1, 2, 1]
    ]) == True, "Diagonal"
