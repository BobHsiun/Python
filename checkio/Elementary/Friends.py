class Friends:
    def __init__(self, connections):
        self.connections = [a for a in connections]
        print("输入：",self.connections,type(self.connections))
        self.conlist = list(self.connections)
        self.newset = set()

    def add(self, connection):
        if connection in self.conlist:
            print("Add False")
            return False
        else:
            self.conlist.append(connection)
            print("add",self.conlist)
            return True

    def remove(self, connection):
        if connection in self.conlist:
            self.conlist.remove(connection)
            print("remove:",self.conlist)
            return True
        else:
            print("Remove False")
            return False

    def names(self):
        newset = set()
        for i in self.conlist:
            newset = newset | i
        print("names:",set(sorted(newset)))
        return set(sorted(newset))

    def connected(self, name):
        nlist=[]
        rset=set()
        for i in self.conlist:
            if name in i:
                nlist.append(i)
        print(name,"关系列表：",nlist)
        if len(nlist)==0:
            print(name,"关系集合：",rset)
            return rset
        else:
            for l in nlist:
                rset = rset | l
            rset.remove(name)
            print(name,"关系集合：",rset)
            return rset


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    letter_friends = Friends(({"a", "b"}, {"b", "c"}, {"c", "a"}, {"a", "c"}))
    digit_friends = Friends([{"1", "2"}, {"3", "1"}])
    assert letter_friends.add({"c", "d"}) is True, "Add"
    assert letter_friends.add({"c", "d"}) is False, "Add again"
    assert letter_friends.remove({"c", "d"}) is True, "Remove"
    assert digit_friends.remove({"c", "d"}) is False, "Remove non exists"
    assert letter_friends.names() == {"a", "b", "c"}, "Names"
    assert letter_friends.connected("d") == set(), "Non connected name"
    assert letter_friends.connected("a") == {"b", "c"}, "Connected name"



#其他解法学习
# from itertools import chain
# class Friends:
#     def __init__(self, connections):
#         self.connections = set(frozenset(c) for c in connections)
#
#     def add(self, connection):
#         not_exist = connection not in self.connections
#         self.connections.add(frozenset(connection))
#         return not_exist
#
#     def remove(self, connection):
#         exist = connection in self.connections
#         self.connections.discard(connection)
#         return exist
#
#     def names(self, connections=None):
#         return set(chain.from_iterable(connections or self.connections))
# ​
#     def connected(self, name):
#         return self.names((s for s in self.connections if name in s)) - {name}