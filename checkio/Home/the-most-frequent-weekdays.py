import time,datetime
def most_frequent_days(year):
    week_day_dict = {0 : '星期一', 1 : '星期二', 2 : '星期三', 3 : '星期四', 4 : '星期五', 5 : '星期六', 6 : '星期天',}
    day = date.weekday(day)
    return ['Monday']

if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert most_frequent_days(2399) ==  ['Friday'], "1st example"
    assert most_frequent_days(1152) == ['Tuesday', 'Wednesday'], "2nd example"
    assert most_frequent_days(56) == ['Saturday', 'Sunday'], "3rd example"
    assert most_frequent_days(2909) == ['Tuesday'], "4th example"
