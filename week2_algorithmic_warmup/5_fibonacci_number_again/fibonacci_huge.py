# Uses python3
# Grader output -> Good job! (Max time used: 0.03/5.00, max memory used: 9916416/536870912.)
import sys

def calc_fib(n):
    if n == 0:
        return 0
    arr = [0] * (n+1)
    arr[1] = 1
    for i in range(2, n+1):
        arr[i] = arr[i-1] + arr[i-2]
    return arr[n]

def fibonacci_pisano_period(m):
    if n <= 2:
        return n+1
    a, b = 0, 1

    pisano = []
    pisano.append(0)
    pisano.append(1)

    while(True):
        current_fib = a + b
        pisano.append(current_fib % m)

        # handle fibonacci numbers
        a = b
        b = current_fib

        if pisano[-2] == 0 and pisano[-1] == 1:
            return len(pisano) - 2

def get_fibonacci_huge(n, m):
    pisano = fibonacci_pisano_period(m)
    remainder = n % pisano
    return calc_fib(remainder) % m

def get_fibonacci_huge_naive(n, m):
    if n <= 1:
        return n

    previous = 0
    current  = 1

    for _ in range(n - 1):
        previous, current = current, previous + current

    return current % m

if __name__ == '__main__':
    n, m = map(int, input().split())
    #print(get_fibonacci_huge_naive(n, m))
    #print(fibonacci_pisano_period(n,m))
    #print(calc_fib(n))
    #print(fibonacci_pisano_period(m))
    print(get_fibonacci_huge(n,m))

