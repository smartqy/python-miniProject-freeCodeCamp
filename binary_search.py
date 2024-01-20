import random
import time

def naive_search(l, target):
    for i in range(len(l)):
        if target == l[i]:
            return i
    return -1


def binary_search(l, target, low = None, high = None):
    if low is None:
        low = 0
    
    if high is None:
        high = len(l) - 1

    if high < low:
        return -1
    
    mid = (low + high) // 2

    if target == l[mid]:
        return mid
    elif target < l[mid]:
        return binary_search(l, target, low, mid-1)
    else:
        return binary_search(l, target, mid+1, high)
    
if __name__ == '__main__':
    length = 10000
    sorted_list = set()
    while len(sorted_list) < length:
        sorted_list.add(random.randint(-3*length, 3*length))
    sorted_list = sorted(list(sorted_list))


    start = time.time()
    for target in sorted_list:
        naive_search(sorted_list, target)
    end = time.time()
    print('naive_search time is:' , (end-start)/length)

    start = time.time()
    for target in sorted_list:
        binary_search(sorted_list, target)
    end = time.time()
    print('binary_search time is:' , (end-start)/length)

    
