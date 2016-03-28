#Question
# A pangram (Greek:παν γράμμα, pan gramma, "every letter") or holoalphabetic sentence for a given alphabet is a
# sentence using every letter of the alphabet at least once. Perhaps you are familiar with the well known pangram "The
# quick brown fox jumps over the lazy dog".
# For this mission, we will use the latin alphabet (A-Z). You are given a text with latin letters and punctuation
# symbols. You need to check if the sentence is a pangram or not. Case does not matter.

#My answer
def check_pangram(text):
    newt=text.lower()
    alplist=list(chr(i)  for i in  range(97,123))
    print("---------",alplist)
    for w in alplist:
        if w in newt:
            continue
        else:
            return False
    return True

if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert check_pangram("The quick brown fox jumps over the lazy dog."), "brown fox"
    assert not check_pangram("ABCDEF"), "ABC"
    assert check_pangram("Bored? Craving a pub quiz fix? Why, just come to the Royal Oak!"), "Bored?"


#其他思路
# import string
# def check_pangram(text):
#     return len(set([c for c in text.lower() if c in string.ascii_lowercase])) == 26