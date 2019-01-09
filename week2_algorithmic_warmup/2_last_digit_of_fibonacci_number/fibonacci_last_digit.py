# Uses python3

def get_fibonacci_last_digit_naive(n):
    if n <= 1:
        return n

    previous = 0
    current  = 1

    for _ in range(n - 1):
        print(n)
        previous, current = current, previous + current

    return current % 10

def get_fibonacci_last_digit(n):
    if n <= 1:
        return n
    
    arr = [0] * (n+1)
    arr[1] = 1

    for i in range(2, n+1):
        arr[i] = (arr[i-1] + arr[i-2]) % 10
    
    print(arr)
    return arr[n]

if __name__ == '__main__':
    n = int(input())
    # print(get_fibonacci_last_digit_naive(n))
    print(get_fibonacci_last_digit(n))


# (Max time used: 0.28/5.00, max memory used: 13684736/536870912.)