def checkio(n, m):
    Sn = str(bin(n)).replace("0b","")
    Sm = str(bin(m)).replace("0b","")
    print(Sn,Sm)
    N=max(len(Sn),len(Sm))
    Sn=Sn.zfill(N)
    Sm=Sm.zfill(N)
    print(N,Sn,Sm)
    reslut=[]
    for i in range(0,N):
        reslut.append(int(Sn[i])^int(Sm[i]))
    print(reslut,sum(reslut))
    return sum(reslut)

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio(117, 17) == 3, "First example"
    assert checkio(1, 2) == 2, "Second example"
    assert checkio(16, 15) == 5, "Third example"

#官方推荐解法
def checkio(n, m):

    nbin = list(bin(n)[2:].zfill(20))
    mbin = list(bin(m)[2:].zfill(20))
    distance = sum([1 for (x,y) in zip(nbin, mbin) if x != y])
    return distance
#zip的用法