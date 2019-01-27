# Uses python3
import sys
import random

# Good job! (Max time used: 0.51/5.00, max memory used: 20357120/536870912.)

def partition_3(a, low, high):
    # From Geeksforgeeks
    if high - low <= 1:
        if a[high] < a[low]:
            a[high], a[low] = a[low], a[high]
            return low, high
    mid = low
    pivot = a[high]

    while mid <= high:
        if a[mid] < pivot:
            a[low], a[mid] = a[mid], a[low]
            low += 1
            mid += 1
        elif a[mid] == pivot:
            mid += 1
        else:
            a[mid], a[high] = a[high], a[mid]
            high -= 1
    return low - 1, mid

def partition3(a, l, r):
    x = a[l] # pivot 
    p_l = i = l
    p_r = r
    while i <= p_r:
        if a[i] < x:
            a[i], a[p_l] = a[p_l], a[i]
            p_l += 1
            i += 1
        elif a[i] == x:
            i += 1
        else:
            a[i], a[p_r] = a[p_r], a[i]
            p_r -= 1
        p = [p_l, p_r]
    return p

def partition2(a, l, r):
    x = a[l] # pivot 
    j = l
    for i in range(l + 1, r + 1):
        if a[i] <= x:
            j += 1
            a[i], a[j] = a[j], a[i]
    a[l], a[j] = a[j], a[l]
    return j


def randomized_quick_sort(a, l, r):
    if l >= r:
        return
    k = random.randint(l, r)
    a[l], a[k] = a[k], a[l]
    #use partition3
    #m = partition3(a, l, r)
    i, j = partition_3(a, l, r)
    randomized_quick_sort(a, l, i)
    randomized_quick_sort(a, j, r)


if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    # n, *a = [int(x) for x in input().split()]
    randomized_quick_sort(a, 0, n - 1)
    for x in a:
        print(x, end=' ')
