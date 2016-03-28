#Question
# What is your favourite day of the week? Check if it's the most frequent day of the week in the year.
# You are given a year as integer (e. g. 2001). You should return the most frequent day(s) of the week in that year.
# The result has to be a list of days sorted by the order of days in week (e. g. ['Monday', 'Tuesday']). Week starts
# with Monday.
# Input: Year as an int.
# Output: The list of most frequent days sorted by the order of days in week (from Monday to Sunday).

#My answer

import time,datetime
#def most_frequent_days(year):
def get_week_day(date):
    week_day_dict = {
    0 : '星期一',
    1 : '星期二',
    2 : '星期三',
    3 : '星期四',
    4 : '星期五',
    5 : '星期六',
    6 : '星期天',}
    day = date.weekday(day)
    return week_day_dict()
    print get_week_day(today())
    return ['Monday']

if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert most_frequent_days(2399) ==  ['Friday'], "1st example"
    assert most_frequent_days(1152) == ['Tuesday', 'Wednesday'], "2nd example"
    assert most_frequent_days(56) == ['Saturday', 'Sunday'], "3rd example"
    assert most_frequent_days(2909) == ['Tuesday'], "4th example"


