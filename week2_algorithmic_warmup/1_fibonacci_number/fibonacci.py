# Uses python3
def calc_fib_naive(n):
    if (n <= 1):
        return n

    return calc_fib(n - 1) + calc_fib(n - 2)

# Uses python3
def calc_fib(n):
    if n == 0:
        return 0
    arr = [0] * (n+1)
    arr[1] = 1
    for i in range(2, n+1):
        arr[i] = arr[i-1] + arr[i-2]
    return arr[n]

n = int(input())
print(calc_fib(n))


#Good job! (Max time used: 0.06/5.00, max memory used: 9617408/536870912.)