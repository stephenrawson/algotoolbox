# Uses python3
import sys

# Good job! (Max time used: 0.03/5.00, max memory used: 9744384/671088640.)
# Input: 3 50 60 20 100 50 120 30

def get_optimal_value(capacity, weights, values):
    values_weights_dict = dict([(values[i] / weights[i], weights[i]) for i in range(len(values))])

    values_weights = [i for i in values_weights_dict]
    values_weights = sorted(values_weights, reverse=True)

    weights  = [values_weights_dict[i] for i in values_weights]
    values_weights_dict = {}

    arr = [0] * len(weights)
    value = 0.

    for i in range(len(weights)):
        if capacity == 0:
            return value, arr

        a = min(weights[i], capacity)

        value += (a * values_weights[i])
        weights[i] -= a
        arr[i] = arr[i] + a
        capacity -= a

    return value, arr


if __name__ == "__main__":
    # data = list(map(int, sys.stdin.read().split()))
    data = list(map(int, sys.stdin.readline().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value, arr = get_optimal_value(capacity, weights, values)
    print("{:.4f}".format(opt_value))
    # print(arr)
