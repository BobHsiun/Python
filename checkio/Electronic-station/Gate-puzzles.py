def find_word(message):
    newm=""
    for s in message:
        if s.isalpha():
            newm+=s
        elif s==" ":
            newm+=s
    message = newm
    slist=[s.lower() for s in message.split(" ")]
    slist.reverse()
    print(slist)
    sumlist=[]
    averlist= []
    for n in range(0,len(slist)):
        sumlist.append(0.0)
        averlist.append(0.0)
        for m in range(0,len(slist)):
            if m==n:
                continue
            else:
                if slist[n][0] == slist[m][0] :
                    sumlist[n]+=10.0
                if slist[n][-1] == slist[m][-1] :
                    sumlist[n]+=10.0
                if len(slist[n]) >= len(slist[m]):
                    sumlist[n]+=30*float('%.3f' %(len(slist[m])/len(slist[n])))
                else:
                    sumlist[n]+=30*float('%.3f' %(len(slist[n])/len(slist[m])))
                sumlist[n]+= 50*float('%.3f' %(len(set(slist[n])&set(slist[m]))/len(set(slist[n])|set(slist[m]))))
        averlist[n]=sumlist[n]/(len(slist)-1)
    print(sumlist,averlist)
    print("R:::",slist[averlist.index(max(averlist))])
    return slist[averlist.index(max(averlist))]

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert find_word("Speak friend and enter.") == "friend", "Friend"
    assert find_word("Beard and Bread") == "bread", "Bread is Beard"
    assert find_word("The Doors of Durin, Lord of Moria. Speak friend and enter. "
                     "I Narvi made them. Celebrimbor of Hollin drew these signs") == "durin", "Durin"
    assert find_word("Aoccdrnig to a rscheearch at Cmabrigde Uinervtisy."
                     " According to a researcher at Cambridge University.") == "according", "Research"
    assert find_word("One, two, two, three, three, three.") == "three", "Repeating"
