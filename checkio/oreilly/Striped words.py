import re

def checkio(text):
    VOWELS = "AEIOUY"
    CONSONANTS = "BCDFGHJKLMNPQRSTVWXZ"
    p=re.compile("[^a-zA-Z0-9]")
    tlist=p.split(text)
    print("text列表：",tlist)
    nlist=[]
    for i in tlist:
        n=i.upper()
        if not re.match('[^A-Z]+',n) and len(i)>1:
            nlist.append(n)
    print("转换过滤后：",nlist)
    count=0
    for x in nlist:
        count+=1
        for y in range(1,len(x)):
            if (x[y] in VOWELS and x[y-1]  in CONSONANTS) or (x[y] in CONSONANTS and x[y-1]  in VOWELS):
                continue
            else:
                count-=1
                break

    print(text,count)
    return count

checkio("1st 2a ab3er root rate")
#These "asserts" using only for self-checking and not necessary for auto-testing
# if __name__ == '__main__':
#     assert checkio("My name is ...") == 3, "All words are striped"
#     assert checkio("Hello world") == 0, "No one"
#     assert checkio("A quantity of striped words.") == 1, "Only of"
#     assert checkio("Dog,cat,mouse,bird.Human.") == 3, "Dog, cat and human"




#学习新解法
# import re
# ​
# ​
# def checkio(text):
#
#     data = re.sub(r'[,\.?!:;]', ' ', text.lower()).split()
#     data = [word for word in data if len(word) > 1 and word.isalpha()]
#     data = [''.join(["v" if x in 'aeiouy' else "c" for x in word]) for word in data]
#
#     return sum([0 if 'cc' in x or 'vv' in x else 1 for x in data])