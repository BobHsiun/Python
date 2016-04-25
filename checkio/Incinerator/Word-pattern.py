def check_command(pattern, command):
    key = str(bin(pattern)).replace("0b", "")
    if len(key) <= len(command):
        key = key.zfill(len(command))
    else:
        return False
    print(key)
    for n in range(len(command)):
        if int(key[n]) == 0 and command[n].isalpha():
            return False
        elif int(key[n]) == 1 and command[n].isdigit():
            return False
    return True

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert check_command(42, "12a0b3e4") == True, "42 is the answer"
    assert check_command(101, "ab23b4zz") == False, "one hundred plus one"
    assert check_command(0, "478103487120470129") == True, "Any number"
    assert check_command(127, "Checkio") == True, "Uppercase"
    assert check_command(7, "Hello") == False, "Only full match"
    assert check_command(8, "a") == False, "Too short command"
    assert check_command(5, "H2O") == True, "Water"
    assert check_command(42, "C2H5OH") == False, "Yep, this is not the Answer"

