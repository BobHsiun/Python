def checkio(data):
    def fline(point1,point2):
        if point1[0]==point2[0]:#aX+bY=c  b=0
            a1=1.0
            b1=0.0
            c1=point1[0]
            return (a1,b1,c1)
        elif point1[1]==point2[1]:#aX+bY=c  a=0
            a2=0.0
            b2=1.0
            c2=point1[1]
            return (a2,b2,c2)
        else:#aX+bY=c  a、b ≠0
            b=1
            a=float((point1[1]-point2[1]/(point1[0]-point2[0]))
            c=float((point1[1]-b)/point1[0])
            return (a,1,c)
        print(fline(data[0],data[1]))

    #replace this for solution
    return ""

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio("(2,2),(6,2),(2,6)") == "(x-4)^2+(y-4)^2=2.83^2"
    assert checkio("(3,7),(6,9),(9,7)") == "(x-6)^2+(y-5.75)^2=3.25^2"