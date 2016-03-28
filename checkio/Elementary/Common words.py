def checkio(first, second):
    flist=first.split(",")
    slist=second.split(",")
    print(flist,slist)
    reslut=set(flist)&set(slist)
    print(reslut)
    r=",".join(list(reslut))
    print(r)
    return r

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio("hello,world", "hello,earth") == "hello", "Hello"
    assert checkio("one,two,three", "four,five,six") == "", "Too different"
    assert checkio("one,two,three", "four,five,one,two,six,three") == "one,three,two", "1 2 3"