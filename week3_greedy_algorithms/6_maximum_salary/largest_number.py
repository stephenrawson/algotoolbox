# Uses python3
# Good job! (Max time used: 0.03/5.00, max memory used: 9613312/536870912.)
import sys

def is_greater_or_equal(n,m):
    return n + m > m + n

def largest_number(a):
    a = sorted(a, reverse=True)
    res = ""
    while  len(a) > 0:
        maxDigit = '0'
        for digit in a:
            if is_greater_or_equal(digit, maxDigit):
                maxDigit = digit
        res += maxDigit
        a.remove(maxDigit)
    return res

if __name__ == '__main__':
    input = sys.stdin.read()
    data = input.split()
    a = data[1:]
    print(largest_number(a))
    