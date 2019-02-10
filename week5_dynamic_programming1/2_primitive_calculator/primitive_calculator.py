# Uses python3
import sys

def optimal_sequence(n):
    sequence = []
    while n >= 1:
        sequence.append(n)
        if n % 3 == 0:
            n = n // 3
        elif n % 2 == 0:
            n = n // 2
        else:
            n = n - 1
    return reversed(sequence)

def primitive_calculator(n):
    operations_count = [0] * (n + 1)

    operations_count[1] = 1
    for i in range(2, n + 1):
        count_index = [i - 1]
        if i % 2 == 0:
            count_index.append(i // 2)
        if i % 3 == 0:
            count_index.append(i // 3)

        min_count = min([operations_count[x] for x in count_index])
        operations_count[i] = min_count + 1

    #print(operations_count)
    current_value = n
    value_trail = [current_value]
    while current_value != 1:
        option_list = [current_value - 1]
        if current_value % 2 == 0:
            option_list.append(current_value // 2)
        if current_value % 3 == 0:
            option_list.append(current_value // 3)

        current_value = min(
            [(c, operations_count[c]) for c in option_list],
            key=lambda x: x[1]
        )[0]
        value_trail.append(current_value)
    value_trail.reverse()
    return value_trail
    # all_parents = [None] * (n + 1)
    # all_min_ops = [0] + [None] * n

    # for k in range(1, n + 1):
    #     curr_parent = k - 1
    #     curr_min_ops = all_min_ops[curr_parent] + 1

    #     if k % 3 == 0:
    #         parent = k // 3
    #         num_ops = all_min_ops[parent] + 1
    #         if num_ops < curr_min_ops:
    #             curr_parent, curr_min_ops = parent, num_ops

    #     if k % 2 == 0:
    #         parent = k // 2
    #         num_ops = all_min_ops[parent] + 1
    #         if num_ops < curr_min_ops:
    #             curr_parent, curr_min_ops = parent, num_ops

    #     all_parents[k], all_min_ops[k] = curr_parent, curr_min_ops

    # numbers = []
    # k = n
    # while k > 0:
    #     numbers.append(k)
    #     k = all_parents[k]
    # numbers.reverse()

    # return numbers
    # values = [None] * (n + 1)
    # min_ops = [0] + [None] * n

    # for i in range(1, n+1):
    #     current_value = i - 1
    #     current_min_ops = min_ops[i - 1] + 1
    #     if i % 3 == 0:
    #         current = i // 3
    #         current_op = min_ops[current] + 1
    #         if current_op < current_min_ops:
    #             current_value, current_min_ops = current, current_op
    #     if i % 2 == 0:
    #         current = i // 2
    #         current_op = min_ops[current] + 1
    #         if current_op < current_min_ops:
    #             current_value, current_min_ops = current, current_op
    #     values[i], min_ops[i] = current_value, current_min_ops
    
    # print(values)
    # print(min_ops)
    # # backtrack
    # operations = []
    # i = n
    # while i > 0:
    #     operations.append(i)
    #     i = values[i]
    # operations.reverse()
    # return operations



input = sys.stdin.read()
n = int(input)
#n = int(input())
sequence = list(primitive_calculator(n))
print(len(sequence) - 1)
for x in sequence:
    print(x, end=' ')


# sequence = primitive_calculator(n)
# print(sequence)
# for x in sequence:
#     print(x, end=' ')
