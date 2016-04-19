import math


def get_circle_center_and_radius(x1, y1, x2, y2, x3, y3):
    # http://okwave.jp/qa/q7112206.html
    d = 2.0 * ((y1 - y3) * (x1 - x2) - (y1 - y2) * (x1 - x3))
    x = ((y1 - y3) * (y1 ** 2 - y2 ** 2 + x1 ** 2 - x2 ** 2) - (y1 - y2)
         * (y1 ** 2 - y3 ** 2 + x1 ** 2 - x3 ** 2)) / d
    y = ((x1 - x3) * (x1 ** 2 - x2 ** 2 + y1 ** 2 - y2 ** 2) - (x1 - x2)
         * (x1 ** 2 - x3 ** 2 + y1 ** 2 - y3 ** 2)) / -d
    r = math.sqrt((x - x1) ** 2 + (y - y1) ** 2)
    return (x, y), r


def checkio(data):
    (x1, y1), (x2, y2), (x3, y3) = eval(data)
    (x0, y0), r = get_circle_center_and_radius(x1, y1, x2, y2, x3, y3)
    return "(x-{:g})^2+(y-{:g})^2={:g}^2".format(round(x0, 2),
                                                 round(y0, 2),
                                                 round(r, 2))


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


#更简单的解法
def checkio(matrix, l=3):
    q = range(len(matrix))
    ls = lambda x:len(set(x))
    for i in q:
        for j in q:
            if i+l in q and ls([matrix[i+n][j] for n in range(4)])==1: return True
            if j+l in q and ls([matrix[i][j+n] for n in range(4)])==1: return True
            if j+l in q and i+l in q and ls([matrix[i+n][j+n] for n in range(4)])==1: return True
            if j-l in q and i+l in q and ls([matrix[i+n][j-n] for n in range(4)])==1: return True
    return False