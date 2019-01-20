#Uses python3

import sys

# Good job! (Max time used: 0.05/5.00, max memory used: 9895936/536870912.)
# input: 5 1 2 3 4 5 1 0 1 0 1
# output: 12 
# Why 12 = 5 * 1 + 4 * 1 + 3 * 1 + 2 * 0 + 1 * 0

# Another example 
# input: 3 1 3 -5 -2 4 1
# output: 23
# Why 23 =  3 · 4 + 1 · 1 + (−5) · (−2)

def max_dot_product(a, b):

    a.sort()
    b.sort()

    res = 0
    for i in range(len(a)):
        if a[i] * b[i] > 0:
            res += a[i] * b[i]
    return res

if __name__ == '__main__':
    # input = sys.stdin.read()
    input = sys.stdin.readline()
    data = list(map(int, input.split()))
    n = data[0]
    a = data[1:(n + 1)]
    b = data[(n + 1):]
    print(max_dot_product(a, b))
    
