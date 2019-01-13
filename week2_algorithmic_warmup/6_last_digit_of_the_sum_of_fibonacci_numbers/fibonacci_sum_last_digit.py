# Uses python3
import sys

def fibonacci_sum_naive(n):
    if n <= 1:
        return n

    previous = 0
    current  = 1
    sum      = 1

    for _ in range(n - 1):
        previous, current = current, previous + current
        sum += current

    return sum % 10

def fibonacci_sum(n):
    if n <= 1:
        return n

    a, b, m = 0, 1, 10
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
            break
    #print(pisano)

    sum = 0
    for i in range(n%60+1):
        sum += pisano[i]
    
    return sum % 10

if __name__ == '__main__':
    n = int(input())
    #print(fibonacci_sum_naive(n))
    print(fibonacci_sum(n))
