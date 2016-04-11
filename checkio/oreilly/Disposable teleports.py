import time
def checkio(teleports_string):
    tellist = teleports_string.split(",")
    print(tellist,teleports_string)
    temlist=[]
    rlist=['1']
    result=[]

    while True:
        temr=[]
        for s in rlist:
            current=s[-1]
            print("S：",s)
            for i in tellist:
                if current in i and current==i[0] and i[1] not in s:
                    temr.append(s+i[1])
                elif current in i and current==i[1] and i[0] not in s:
                    temr.append(s+i[0])
                else:
                    if len(set(s))==8:
                        if current in i and current==i[0] and i[1]==s[0]:
                            temr.append(s+i[1])
                        elif current in i and current==i[1] and i[0]==s[0]:
                            temr.append(s+i[0])
                        else:
                            temr.append(s)
                    elif len(set(s))<8:
                        if current in i and current==i[0] and i[1] in s and i[1] != s[-2]:
                            temr.append(s+i[1])
                        elif current in i and current==i[1] and i[0] in s and i[0] != s[-2]:
                            temr.append(s+i[0])

        if len(temr)>0:
            rlist=temr[:]
            for s in temr:
                if len(set(s))==8 and s[0]==s[-1]:
                    result.append(s)
            print(":",rlist)
        else:
            print("结束")
            break
        time.sleep(2)



    return True


checkio("12,28,87,71,13,14,34,35,45,46,63,65")  # 测试
# This part is using only for self-testing
# if __name__ == "__main__":
#     def check_solution(func, teleports_str):
#         route = func(teleports_str)
#         teleports_map = [tuple(sorted([int(x), int(y)])) for x, y in teleports_str.split(",")]
#         if route[0] != '1' or route[-1] != '1':
#             print("The path must start and end at 1")
#             return False
#         ch_route = route[0]
#         for i in range(len(route) - 1):
#             teleport = tuple(sorted([int(route[i]), int(route[i + 1])]))
#             if not teleport in teleports_map:
#                 print("No way from {0} to {1}".format(route[i], route[i + 1]))
#                 return False
#             teleports_map.remove(teleport)
#             ch_route += route[i + 1]
#         for s in range(1, 9):
#             if not str(s) in ch_route:
#                 print("You forgot about {0}".format(s))
#                 return False
#         return True
#
#     assert check_solution(checkio, "12,23,34,45,56,67,78,81"), "First"
#     assert check_solution(checkio, "12,28,87,71,13,14,34,35,45,46,63,65"), "Second"
#     assert check_solution(checkio, "12,15,16,23,24,28,83,85,86,87,71,74,56"), "Third"
#     assert check_solution(checkio, "13,14,23,25,34,35,47,56,58,76,68"), "Fourth"