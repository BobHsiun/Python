def checkio(number):
    result = ""
    x = 0
    while len(str(number)) > 1:
        temp = x
        for n in range(9,1,-1):
            print("nnnn:",n)
            if number % n == 0:
                result += str(n)
                number = int(number / n)
                x += 1
                break
        print("While 1:", result, number, x)
        if x == temp:
            return 0
    result += str(number)
    result="".join(sorted(list(result)))
    print("结果：", result)
    return int("".join(sorted(list(result))))


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio(20) == 45, "1st example"
    assert checkio(21) == 37, "2nd example"
    assert checkio(17) == 0, "3rd example"
    assert checkio(33) == 0, "4th example"
    assert checkio(3125) == 55555, "5th example"
    assert checkio(9973) == 0, "6th example"



# def checkio(number):
#     result = ""
#     x = 0
#     while len(str(number)) > 1 or number in {4, 6, 8, 9}:
#         temp = x
#         for n in range(2, 10):
#             if number % n == 0:
#                 result += str(n)
#                 number = int(number / n)
#                 x += 1
#                 break
#         print("While 1:", result, number, x)
#         if x == temp:
#             return 0
#     result += str(number)
#     N = 0
#     while N == 0:
#         r = ""
#         for i in range(1, len(result)):
#             n = int(result[i]) * int(result[i - 1])
#             print(i, result[i - 1], result[i])
#             print("n:", n)
#             if len(str(n)) == 1:
#                 r = result[:i - 1] + str(n) + result[i + 1:]
#                 print("R:", r)
#                 result = r
#                 break
#             elif i == len(result) - 1 and len(str(n)) > 1:
#                 N += 1
#                 break
#         print(result)
#     # result="".join(sorted(list(result)))
#     print("结果：", result)
#     return int("".join(sorted(list(result))))
