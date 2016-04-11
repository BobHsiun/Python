def checkio(teleports_string):
    tellist = teleports_string.split(",")
    print(tellist)
    templist = ["1"]
    while True:
        tlist = []
        for i in templist:
            current = i[-1]
            print("Current:", current)
            print("Current-i:", i)
            for i2 in tellist:
                print("I2=",i2)
                if current == i2[0] and i2[1] not in i:
                    tlist.append(i + i2[1])
                    print("current == i2[0] and i2[1] not in i:",tlist)
                elif current == i2[1] and i2[0] not in i:
                    tlist.append(i + i2[0])
                    print("current == i2[1] and i2[0] not in i:",tlist)
                else:
                    if current == i2[0] and i2[1] != i[-2] and len(set(i)) < 8:
                        tlist.append(i + i2[1])
                        print("current == i2[0] and i2[1] != i[-2] and len(set(i)) < 8:",tlist)
                    elif current == i2[1] and i2[0] != i[-2] and len(set(i)) < 8:
                        tlist.append(i + i2[0])
                        print(tlist)
                    else:
                        print("++len(set(i))",len(set(i)))
                        if len(set(i)) == 8:
                            print("come...")
                            if current == i2[1] and i[0]!=i[-1] and i2[0] != i[-2]:
                                tlist.append(i + i2[0])
                                print("大于8-",tlist)
                            elif current == i2[0] and i[0] != i[-1] and i2[1] != i[-2]:
                                tlist.append(i + i2[1])
                                print("大于++",tlist)
                            else:
                                print('???')
                                break
                        else:
                            print("路过...",i2)
                            continue
            if len(set(i)) < 8:
                templist = tlist[:]
                print("当前结果：", templist)
                continue
            elif len(set(i)) == 8 and i[0] ==i[-1]:
                templist = tlist[:]
                break
            else:
                print('FFFFFFFFFFFFFFFFF')
                continue

        print("---")
    print(templist)
    return True


checkio("12,23,34,45,56,67,78,81")  #测试
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


