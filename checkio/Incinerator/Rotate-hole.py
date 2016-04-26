def rotate(state, pipe_numbers):
    pipe_numbers=list(set(pipe_numbers))
    result = []
    newState = state
    for n in range(len(state)):
        TorF = True
        for l in pipe_numbers:
            if newState[l]==0:
                TorF = False
                break
        if TorF:
            result.append(n)
        newState = newState[-1:]+newState[:-1]
    return result

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert rotate([1, 0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 1], [0, 1]) == [1, 8], "Example"
    assert rotate([1, 0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 1], [0, 1, 2]) == [], "Mission impossible"
    assert rotate([1, 0, 0, 0, 1, 1, 0, 1], [0, 4, 5]) == [0], "Don't touch it"
    assert rotate([1, 0, 0, 0, 1, 1, 0, 1], [5, 4, 5]) == [0, 5], "Two cannonballs in the same pipe"


#学习新解法

import collections
​
​
def rotate(state, pipe_numbers):
    result = []
    queue = collections.deque(state)
    for i in range(len(state)):
        if all(queue[i] for i in pipe_numbers):
            result.append(i)
        queue.rotate(1)
    return result
