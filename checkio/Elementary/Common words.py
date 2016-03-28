def checkio(first, second):
    flist=first.split(",")
    slist=second.split(",")
    print(flist,slist)
    reslut=list(set(flist)&set(slist))
    print(reslut)
    reslut.sort()
    r=",".join(reslut)
    print(r)
    return r

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio("hello,world", "hello,earth") == "hello", "Hello"
    assert checkio("one,two,three", "four,five,six") == "", "Too different"
    assert checkio("one,two,three", "four,five,one,two,six,three") == "one,three,two", "1 2 3"

#更好的解法
# def checkio(first, second):
#     set1 = set(first.split(','))
#     set2 = set(second.split(','))
#     return ",".join(sorted(set1 & set2))