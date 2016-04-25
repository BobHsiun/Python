def checkio(number):
    def get_min_k(ns):
        maxs = "0"
        for s in ns:
            if ord(maxs) < ord(s):
                maxs = s
        if ord(maxs) < 60:
            return ord(maxs) - 48 + 1
        else:
            return ord(maxs) - 55 + 1

    def sum_number(number1,k1):
        sumNumber = 0
        for n in range(len(number1)):
            if ord(number1[n]) < 60:
                sumNumber += int(number1[n]) * (k1 ** (len(number1) - 1 - n))
            else:
                sumNumber += (ord(number1[n]) - 55) * (k1 ** (len(number1) - 1 - n))
        print("sumNumber:", sumNumber)
        return sumNumber
    k = get_min_k(number)
    print("K:", k)
    while k < 37:
        if sum_number(number,k) % (k - 1) == 0:
            return k
        else:
            k += 1
            print("K+1:", k)

    if k == 37:
        return 0

if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio("18") == 10, "Simple decimal"
    assert checkio("1010101011") == 2, "Any number is divisible by 1"
    assert checkio("222") == 3, "3rd test"
    assert checkio("A23B") == 14, "It's not a hex"
    assert checkio("IDDQD") == 0, "k is not exist"
    print('Local tests done')


#学习大牛解法
# def checkio(number):
#     k = 2
#     while k < 37:
#         try:
#             cur_number = int(number, k)
#             if cur_number % (k-1) == 0:
#                 return k
#         except: pass
#         finally:
#             k +=1
#     return 0
#对try：    except：的应用