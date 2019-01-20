# Uses python3
# Good job! (Max time used: 0.04/5.00, max memory used: 9601024/536870912.)

def get_change(m):
    arr = [10, 5, 1]
    count, i = 0, 0
    while i < len(arr):
        if m // arr[i] != 0:
            m -= arr[i]
            count += 1
        else:
            i += 1
    return count

if __name__ == '__main__':
    m = int(input())
    print(get_change(m))
