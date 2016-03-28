#Question
# In this task, you are given a set of words in lower case. Check whether there is a pair of words, such that one word
# is the end of another (a suffix of another). For example: {"hi", "hello", "lo"} -- "lo" is the end of "hello",
# so the result is True.
# Input: Words as a set of strings.
# Output: True or False, as a boolean.

#My answer
def checkio(words_set):
    max=""
    print("----------")
    if len(words_set)<2:
        return False
    for s in words_set:
        print("S:",s)
        for w in words_set:
            print("W:",w)
            if len(s)<len(w):
                if w[len(w)-len(s):]==s:
                    return True
                else:
                    continue
            elif len(s)==len(w):
                continue
            else:
                if s[len(w)-len(s):]==w:
                    return True
                else:
                    continue
    return False

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio({"hello", "lo", "he"}) == True, "helLO"
    assert checkio({"hello", "la", "hellow", "cow"}) == False, "hellow la cow"
    assert checkio({"walk", "duckwalk"}) == True, "duck to walk"
    assert checkio({"one"}) == False, "Only One"
    assert checkio({"helicopter", "li", "he"}) == False, "Only end"
