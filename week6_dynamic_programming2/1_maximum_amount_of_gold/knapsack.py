# Uses python3
import sys



def optimal_weight(W, w):
    c = [0]*(W+1)
    for i in range(len(w)):
        #print('Pring c: ' + str(c))
        #print('Printing w[i]-1: ' + str(w[i]-1))
        for j in range(W, w[i]-1, -1):
            #print('w['+ str(i) + ']= ' + str(w[i]) + ' ' + str(c[j]) + ' or '+ str(c[j-w[i]]+w[i]))
            c[j] = max(c[j], c[j-w[i]]+w[i])
            #print(c)
    #print(c)
    return c[W]


    # print(W)
    # value = [ [0 for j in range(len(w)+1)] for i in range(W+1)]
    # #print(value)

    # for j in range(len(w)):
    #     for i in range(1, W+1):
    #         last = value[i][j - 1]
    #         currrent = w[j] + value[W - w[j]][j - 1]
    #         if currrent > i:
    #             value[i][j] = last
    #         else:
    #             value[i][j] = max(last, currrent)
    # print(value)
    # return value[W][len(w)-1]

# max { value(w - wi) + vi, value(w, i-1)}

if __name__ == '__main__':
    #input = sys.stdin.read()
    W, n, *w = list(map(int, input().split()))
    print(optimal_weight(W, w))
