#Uses python3
# Good job! (Max time used: 0.04/5.00, max memory used: 9740288/536870912.)
import sys

def lcs2(x, y):
    m = len(x)
    n = len(y)

    c = [[None for i in range(n+1)] for j in range(m+1)]

    for i in range(m+1):
        for j in range(n+1):
    #         print('d('+str(i)+','+str(j)+')')
    #         print('d('+str(i)+','+str(j)+') = ' + str(c[i][j]))
            if i == 0 or j==0:
                c[i][j] = 0
            elif x[i-1] == y[j-1]:
                c[i][j] = c[i-1][j-1] + 1
            else:
                c[i][j] = max(c[i-1][j], c[i][j-1])

    # for row in c:
    #     print(' '.join([str(elem) for elem in row]))
    # print(c[m][n])
    return c[m][n]

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    # data = list(map(int, input().split())) 
    n = data[0]
    data = data[1:]
    a = data[:n]

    data = data[n:]
    m = data[0]
    data = data[1:]
    b = data[:m]

    print(lcs2(a, b))
