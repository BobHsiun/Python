def checkio(numbers_array):
    r=[]
    nl=list(numbers_array)
    print("==================")
    while len(numbers_array) > len(r):
        max=0
        for m in nl:
            if abs(m) >=abs(max) :
                max=m
        r.append(max)
        print("结果：",r)
        nl.remove(max)
        print("nl:",nl)
    return nl[ : :-1]


#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    def check_it(array):
        if not isinstance(array, (list, tuple)):
            raise TypeError("The result should be a list or tuple.")
        return list(array)

    assert check_it(checkio((-20, -5, 10, 15))) == [-5, 10, 15, -20], "Example"  # or (-5, 10, 15, -20)
    assert check_it(checkio((1, 2, 3, 0))) == [0, 1, 2, 3], "Positive numbers"
    assert check_it(checkio((-1, -2, -3, 0))) == [0, -1, -2, -3], "Negative numbers"
