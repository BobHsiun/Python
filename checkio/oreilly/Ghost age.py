def checkio(opacity):
    Fibonacci=[1,1]
    while Fibonacci[-1]+Fibonacci[-2]<5000:
        Fibonacci.append(Fibonacci[-1]+Fibonacci[-2])
    print(Fibonacci)
    n=0
    start=10000
    while start!=opacity:
        n += 1
        if n in Fibonacci:
            start=start-n
        else:
             start=start+1
        print(n,"=====",start)
    print(n)
    return n
checkio(9995)
#These "asserts" using only for self-checking and not necessary for auto-testing
# if __name__ == '__main__':
#     assert checkio(10000) == 0, "Newborn"
#     assert checkio(9999) == 1, "1 year"
#     assert checkio(9997) == 2, "2 years"
#     assert checkio(9994) == 3, "3 years"
#     assert checkio(9995) == 4, "4 years"
#     assert checkio(9990) == 5, "5 years"


#其他解法
# def checkio(op):
#     f1,f2,age,x=1,0,0,10000
#     while(1):
#         age+=1
#         if(age==f1+f2):
#             f1,f2=f1+f2,f1
#             x-=f1
#         else:
#             x=x+1
#         if(x==op):
#             break
#     return age