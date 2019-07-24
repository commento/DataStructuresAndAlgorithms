def get_min_max(ints):
    """
    Return a tuple(min, max) out of list of unsorted integers.

    Args:
       ints(list): list of integers containing one or more integers
    """
    min = ints[0]
    max = ints[0]

    for i in ints:
        if min > i:
            min = i
        if max < i:
            max = i

    return min, max

## Example Test Case of Ten Integers
import random


print("Test1")
l = [i for i in range(0, 10)]  # a list containing 0 - 9
random.shuffle(l)
print ("Pass" if ((0, 9) == get_min_max(l)) else "Fail")

print("Test2")
l = [i for i in range(-200, 200)]  # a list containing -200 - 199
random.shuffle(l)
print ("Pass" if ((-200, 199) == get_min_max(l)) else "Fail")

print("Test3")
l = [i for i in range(0, 1)]  # a list containing 0 - 0
random.shuffle(l)
print ("Pass" if ((0, 0) == get_min_max(l)) else "Fail")