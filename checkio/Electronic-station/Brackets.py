def checkio(expression):
    reslut = True
    brackets = "{}()[]"
    bracketset = {'{': "}", '[': ']', '(': ')'}
    print(bracketset['{'])
    newex = []
    for s in expression:
        if s in brackets:
            newex.append(s)
    print(newex)
    if len(newex) == 0:
        reslut = True
    elif len(newex) % 2 != 0:
        reslut = False
    else:
        while reslut:
            N = len(newex)
            if N== 0:
                break
            for n in range(0,N):
                if newex[n] not in bracketset.keys():
                    if bracketset[newex[n-1]] == newex[n]:
                        newex.pop(n-1)
                        newex.pop(n-1)
                        break
                    else:
                        reslut = False
                        break
    return reslut


# These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio("((5+3)*2+1)") == True, "Simple"
    assert checkio("{[(3+1)+2]+}") == True, "Different types"
    assert checkio("(3+{1-1)}") == False, ") is alone inside {}"
    assert checkio("[1+1]+(2*2)-{3/3}") == True, "Different operators"
    assert checkio("(({[(((1)-2)+3)-3]/3}-3)") == False, "One is redundant"
    assert checkio("2+3") == True, "No brackets, no problem"
