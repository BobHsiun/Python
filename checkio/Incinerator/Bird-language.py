VOWELS = "aeiouy"

def translate(phrase):
    phraseList = phrase.split(" ")
    print(phraseList)
    newphraseList = []
    for h in phraseList:
        n = 0
        newH=""
        while n!=len(h):
            if h[n] not in VOWELS and h[n+1] in VOWELS:
                newH+=h[n]
                n+=2
                continue
            elif h[n] in VOWELS and h[n+1]==h[n+2]==h[n]:
                newH+=h[n]
                n+=3
                continue
            else:
                newH+=h[n]
                n+=1
                continue
        newphraseList.append(newH)
        print(newphraseList)
    return " ".join(newphraseList)

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert translate("hieeelalaooo") == "hello", "Hi!"
    assert translate("hoooowe yyyooouuu duoooiiine") == "how you doin", "Joey?"
    assert translate("aaa bo cy da eee fe") == "a b c d e f", "Alphabet"
    assert translate("sooooso aaaaaaaaa") == "sos aaa", "Mayday, mayday"
