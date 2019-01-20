# Uses python3
# Good job! (Max time used: 0.10/5.00, max memory used: 10743808/536870912.)
# input: 6
# Output: 3
#         1 2 3

# input: 8
# Output: 3
#         1 2 5

def optimal_summands(n):
    summands = []
    if n <= 2:
        return [n]
    i = 1
    while n > 0:
        tmp = n - i
        if tmp > i or tmp == 0:
            summands.append(i)
            n -= i
        i += 1

    return summands

if __name__ == '__main__':
    #input = sys.stdin.read()
    n = int(input())
    summands = optimal_summands(n)
    print(len(summands))
    for x in summands:
        print(x, end=' ')
    print('')
