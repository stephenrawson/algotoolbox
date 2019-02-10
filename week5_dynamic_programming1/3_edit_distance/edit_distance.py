# Uses python3
# Good job! (Max time used: 0.04/5.00, max memory used: 9662464/536870912.)
def edit_distance(n, m):

    d = [[None] * (len(m)+ 1) for i in range(len(n)+1)]
    for i in range(len(n)+1):
        d[i][0] = i
    for j in range(len(m)+1):
        d[0][j] = j
    # for row in d:
    #     print(' '.join([str(elem) for elem in row]))

    for j in range(1, len(m)+1):
        for i in range(1, len(n)+ 1):
            # print('d('+str(i)+','+str(j)+') = ' + str(d[i][j]))
            insertion = d[i][j-1] + 1
            deletion = d[i-1][j] + 1
            match = d[i-1][j-1]
            mismatch = d[i-1][j-1] + 1
            
            if n[i-1] == m[j-1]:
                d[i][j] = min([insertion, deletion, match])
            else:
                d[i][j] = min([insertion, deletion, mismatch])
            # for row in d:
            #     print(' '.join([str(elem) for elem in row]))
    return d[len(n)][len(m)]


# D(i, j- 1) + 1
# D(i - 1, j) + 1
# D(i-1,j-1) + 1 if A[i] != B[j]
# D(i-1, j-1) if A[i] = B[j]

if __name__ == "__main__":
    print(edit_distance(input(), input()))
