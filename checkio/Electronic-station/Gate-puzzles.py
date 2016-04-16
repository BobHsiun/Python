def find_word(message):
    slist=[s.lower() for s in message.split(" ")]
    print(slist)
    for n in range(0,len(slist)):
        


    return ""

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert find_word("Speak friend and enter.") == "friend", "Friend"
    assert find_word("Beard and Bread") == "bread", "Bread is Beard"
    assert find_word("The Doors of Durin, Lord of Moria. Speak friend and enter. "
                     "I Narvi made them. Celebrimbor of Hollin drew these signs") == "durin", "Durin"
    assert find_word("Aoccdrnig to a rscheearch at Cmabrigde Uinervtisy."
                     " According to a researcher at Cambridge University.") == "according", "Research"
    assert find_word("One, two, two, three, three, three.") == "three", "Repeating"
