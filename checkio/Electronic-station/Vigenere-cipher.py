def decode_vigenere(old_decrypted, old_encrypted, new_encrypted):
    #生成密码表
    dictList=["ABCDEFGHIJKLMNOPQRSTUVWXYZ"]
    for i in range(1,26):
        dictList.append("")
        dictList[i]=dictList[i-1][1:]+dictList[i-1][:1]
    #print(dictList)
    #获取解密KEY
    def get_key(old_decrypted, old_encrypted):
        key=""
        n=0
        for k in old_decrypted:
            key+=dictList[0][dictList[ord(k)-65].index(old_encrypted[n])]
            n+=1
        print("解码出来的Key:",key,len(key))
        if len(key)>1:
            for i in range(1,int(len(key)/2)):
                is_only=True
                keyTemp=key[:i]
                N=int(len(key)/i)
                M=len(key)%i
                if M!=0:
                    if keyTemp[:M]!=key[-M:]:
                        continue
                for l in range(N):
                    if keyTemp != key[len(keyTemp)*l:len(keyTemp)*(l+1)]:
                        is_only=False
                        break
                if is_only==True :
                    print("KeyT:",keyTemp)
                    return keyTemp
        print("Key:",key)
        return key
    #新密码
    key=get_key(old_decrypted, old_encrypted)
    if len(new_encrypted)<=len(key):
        newKey = key[:len(new_encrypted)]
    else:
        x=int(len(new_encrypted)/len(key))
        y=len(new_encrypted)%len(key)
        newKey=key*x+key[:y]
    #新解密
    new_decrypted=""
    m=0
    for w in newKey:
        new_decrypted+=dictList[0][dictList[ord(w)-65].index(new_encrypted[m])]
        m+=1
    print("最终结果：",new_decrypted,"\n")
    return new_decrypted


#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert decode_vigenere('DONTWORRYBEHAPPY',
                           'FVRVGWFTFFGRIDRF',
                           'DLLCZXMFVRVGWFTF') == "BEHAPPYDONTWORRY", "CHECKIO"
    assert decode_vigenere('HELLO', 'OIWWC', 'ICP') == "BYE", "HELLO"
    assert decode_vigenere('LOREMIPSUM',
                           'OCCSDQJEXA',
                           'OCCSDQJEXA') == "LOREMIPSUM", "DOLORIUM"

#学习新解法
getkey=lambda d, e:chr((ord(e) - ord(d)) % (ord("Z") - ord("A") + 1) + ord("A"))
decrypt=lambda e, k:getkey(k, e)
​
def normalize(key):
    for n in range(1,len(key)+1):
        if all(i + n >= len(key) or key[i] == key[i + n] for i in range(len(key))):
            return key[:n]
​
def decode_vigenere(old_decrypted, old_encrypted, new_encrypted):
    key = "".join(getkey(old_decrypted[i], old_encrypted[i]) for i in range(len(old_encrypted)))
    key = normalize(key)
    return "".join(decrypt(new_encrypted[i], key[i % len(key)]) for i in range(len(new_encrypted)))