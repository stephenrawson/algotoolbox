# Uses python3
# Good job! (Max time used: 0.22/5.00, max memory used: 27480064/536870912.)
import sys

def get_majority_element(a, left, right):
    n = {}
    for i in range(len(a)):
        if str(a[i]) in n:
            value = n[str(a[i])]
            n[str(a[i])] = value + 1
        else:
            n[str(a[i])] = 1
    for i in range(len(a)):
        if n[str(a[i])] > len(a) // 2:
            return 1
    return -1


def get_majority_element_naive(a, left, right):
    if left == right:
        return -1
    if left + 1 == right:
        return a[left]
    for i in range(left, right):
        current_element = a[i]
        count = 0
        for j in range(left, right):
            if a[j] == current_element:
                count += 1
        if count > right // 2:
            return current_element
    return -1

if __name__ == '__main__':
    # input = sys.stdin.read()
    n, *a = list(map(int, input().split()))
    if get_majority_element(a, 0, n) != -1:
    # if get_majority_element_naive(a, 0, n) != -1:
        print(1)
    else:
        print(0)
