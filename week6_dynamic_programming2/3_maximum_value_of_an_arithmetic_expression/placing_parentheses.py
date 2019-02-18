# Uses python3
def evalt(a, b, op):
    #print(str(a)+str(b)+op)
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    else:
        assert False

def MinAndMax(i, j, m, M, op):
    minimum = float("inf")
    maximum = float("-inf")

    for k in range(i, j):
        a = evalt(M[i][k], M[k+1][j], op[k])
        b = evalt(M[i][k], m[k+1][j], op[k])
        c = evalt(m[i][k], M[k+1][j], op[k])
        d = evalt(m[i][k], m[k+1][j], op[k])
        
        minimum = min(minimum, a, b, c, d)
        maximum = max(maximum, a, b, c, d)
    
    return(minimum, maximum)    


def get_maximum_value(dataset):
    n  = len(dataset)
    op = dataset[1 : len(dataset) : 2] # parse operators
    digits = dataset[0 : len(dataset)+1 : 2] # parse digits
    # print(op)
    # print(digits)

    n = len(digits)
    m = [ [0] * n for _ in range(n)]
    M = [ [0] * n for _ in range(n)]
    
    for i in range(n):
        m[i][i] = int(digits[i])
        M[i][i] = int(digits[i])
    
    for s in range(1, n):
        for i in range(n-s):
            j = i + s
            m[i][j], M[i][j] = MinAndMax(i, j, m, M, op)

    return M[0][n-1]


if __name__ == "__main__":
    print(get_maximum_value(input()))
