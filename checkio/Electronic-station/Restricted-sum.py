def checkio(data):
    s = 0
    print(data)

    def fn(data, s):
        if len(data) > 0:
            s = s + data.pop()
            print(s)
            return fn(data, s)
        else:
            return s

    return fn(data, s)


checkio([1, 2, 3])
