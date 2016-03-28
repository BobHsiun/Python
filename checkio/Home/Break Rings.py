#Question
# A blacksmith gave his apprentice a task, ordering them to make a selection of rings. The apprentice is not yet skilled in the craft and as a result of this, some (to be honest, most) of rings came out connected together. Now he’s asking for your help separating the rings and deciding how to break enough rings to free so as to get the maximum number of rings possible.
#
# All of the rings are numbered and you are told which of the rings are connected. This information is given as a sequence of sets. Each set describes the connected rings. For example: {1, 2} means that the 1st and 2nd rings are connected. You should count how many rings we need to break to get the maximum of separate rings. Each of the rings are numbered in a range from 1 to N, where N is total quantity of rings.
#
# example-rings
#
# In the above image you can see the connections: ({1,2},{2,3},{3,4},{4,5},{4,6},{6,5}). The optimal solution here would be to break 3 rings, making 3 full and separate rings. So the result is 3.
#
# Input: Information about the connected rings as a tuple of sets with integers.
#
# Output: The number of rings to break as an integer.

#My answer
from itertools import groupby, chain
from collections import Counter
def ring_to_destroy(rings):
    """
    find out which element connects with the least connection element
    :param rings:
    :return: element to destroy
    """
    least_connected = Counter(chain(*[i for i in rings if len(i) > 1])) \
        .most_common()[-1][0]
    return [j for i in rings if least_connected in i for j in i if j != least_connected][0]


def has_connection(rings):
    return any([1 for i in rings if len(i) > 1])


def remove_duplicates(rings):
    return list(set(map(tuple, rings)))


def destroy_ring(rings, ring):
    ret = []
    for i in rings:
        ret.append({j for j in i if j != ring})
    return tuple([k for k, v in groupby(sorted(remove_duplicates(ret))) if len(k) > 1])


def break_rings(rings):
    ring_counter = 0
    while has_connection(rings):
        rings = destroy_ring(rings, ring_to_destroy(rings))
        ring_counter += 1
    return ring_counter


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert break_rings(({1, 2}, {2, 3}, {3, 4}, {4, 5}, {5, 6}, {4, 6})) == 3, "example"
    assert break_rings(({1, 2}, {1, 3}, {1, 4}, {2, 3}, {2, 4}, {3, 4})) == 3, "All to all"
    assert break_rings(({5, 6}, {4, 5}, {3, 4}, {3, 2}, {2, 1}, {1, 6})) == 3, "Chain"
    assert break_rings(({8, 9}, {1, 9}, {1, 2}, {2, 3}, {3, 4}, {4, 5}, {5, 6}, {6, 7}, {8, 7})) == 5, "Long chain"


#无法通过全部的测试。暂时无解，need hlep！
