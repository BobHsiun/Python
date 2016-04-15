def letter_queue(commands):
    nlist = []
    ruslut=""
    for i in commands:
        if " " in i:
            nlist.append(i.split(" "))
        else:
            nlist.append([i])
    print(nlist)
    for l in nlist:
        if l[0]=="PUSH":
            ruslut+=l[1]
        elif l[0]=="POP":
            if len(ruslut)!=0:
                ruslut=ruslut[1:]
    print(ruslut)
    return ruslut

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert letter_queue(["PUSH A", "POP", "POP", "PUSH Z", "PUSH D", "PUSH O", "POP", "PUSH T"]) == "DOT", "dot example"
    assert letter_queue(["POP", "POP"]) == "", "Pop, Pop, empty"
    assert letter_queue(["PUSH H", "PUSH I"]) == "HI", "Hi!"
    assert letter_queue([]) == "", "Nothing"