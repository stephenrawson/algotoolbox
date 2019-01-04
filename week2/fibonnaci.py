# From the Readings DPV (Dasgupta, Papadimitriou, Vazirani - Algorithms)
# python 3

def fib_recursive(n):
    if n <= 1:
        return n
    return (fib_recursive(n-1) + fib_recursive(n-2))

def fib_intermediate_results(n):
    if n == 0:
        return n
    f = [0] * (n+1)
    f[1] = 1
    for i in range(2,n+1):
        f[i] = f[i-1] + f[i-2]
    return f[n]

if __name__ == '__main__':
    input_n = int(input())
    # print(fib_recursive(input_n))
    print(fib_intermediate_results(input_n))