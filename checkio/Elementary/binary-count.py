#Question
# For the Robots the decimal format is inconvenient. If they need to count to "1", their computer brains want to count
# it in the binary representation of that number. You can read more about binary here.
# You are given a number (a positive integer). You should convert it to the binary format and count how many unities (1)
# are in the number spelling. For example: 5 = 0b101 contains two unities, so the answer is 2.
# Input: A number as a positive integer.
# Output: The quantity of unities in the binary form as an integer.
# Precondition: 0 < number ≤ 232

#My answer
import math
def checkio(str_number, radix):
    print("+++++++++++++++++++++++++++++++")
    result=0
    if radix < 11:
        for w in str_number:
            print(w)
            if int(w) >= radix:
                return -1
        for i in range(len(str_number)):
            result+=int(str_number[i])*math.pow(radix,len(str_number)-1-i)
            print("-1-:",result)
        return int(result)
    else:
        for w in str_number:
            if (ord(w)-54) >= radix:
                return -1
        for i in range(len(str_number)):
            if ord(str_number[i]) < 65:
                result+=int(str_number[i])*math.pow(radix,len(str_number)-1-i)
                print("-2-:",result)
            else:
                result+=(ord(str_number[i])-54)*math.pow(radix,len(str_number)-1-i)
                print("-2-:",result)
        return int(result)


#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio("AF", 16) == 175, "Hex"
    assert checkio("101", 2) == 5, "Bin"
    assert checkio("101", 5) == 26, "5 base"
    assert checkio("Z", 36) == 35, "Z base"
    assert checkio("AB", 10) == -1, "B > A > 10"
