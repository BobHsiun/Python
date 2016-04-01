import datetime

def most_frequent_days(year):
    fyear = str(year + 1).zfill(4)
    print("输入的年份：", year,"=========================")
    t1 = datetime.datetime(year, 1, 1)
    count = dict()
    while t1.strftime("%Y") != fyear:
        if t1.strftime("%A") not in count:
            count[t1.strftime("%A")] = 0
            # print(count)
        else:
            count[t1.strftime("%A")] += 1
            # print(count)
        t1 = t1 + datetime.timedelta(1)
    print("统计结果：", count)
    maxnum = max(count.values())
    print("最大数值：", maxnum)
    result = []
    for key in count:
        if count[key] == maxnum:
            result.append(key)
    print("最多的结果：",sorted(result))

    return sorted(result)


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert most_frequent_days(2399) == ['Friday'], "1st example"
    assert most_frequent_days(1152) == ['Tuesday', 'Wednesday'], "2nd example"
    assert most_frequent_days(56) == ['Saturday', 'Sunday'], "3rd example"
    assert most_frequent_days(2909) == ['Tuesday'], "4th example"
