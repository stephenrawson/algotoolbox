# Uses python3
import sys

def fibonacci_partial_sum_naive(from_, to):
    sum = 0

    current = 0
    next  = 1

    for i in range(to + 1):
        if i >= from_:
            sum += current

        current, next = next, current + next

    return sum % 10

def fibonacci_partial_sum(m, n):
    if n <= 1:
        return n

    a, b, x = 0, 1, 10
    pisano = []
    pisano.append(0)
    pisano.append(1)

    while(True):
        current_fib = a + b
        pisano.append(current_fib**2 % x)

        # handle fibonacci numbers
        a = b
        b = current_fib

        if pisano[-2] == 0 and pisano[-1] == 1:
            break
    print(pisano)

    sum = 0
    for i in range(n%60+1):
        sum += pisano[i]
    
    return sum % 10


if __name__ == '__main__':
    from_, to = map(int, input().split())
    print(fibonacci_partial_sum_naive(from_, to))