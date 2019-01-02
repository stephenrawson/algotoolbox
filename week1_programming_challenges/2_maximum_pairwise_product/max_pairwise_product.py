# python3
import math
import pickle
import random

def stress_test(n, m):
    while True:
        num_1 = random.randint(2, n)
        arr = [i for i in range(0, num_1)]
        for i in range(num_1-1):
            arr[i] = random.randint(0, m)
        print(arr)
        result_1 = max_pairwise_product_naive(arr)
        result_2 = max_pairwise_product(arr)

        if result_1 == result_2:
            print('OK')
        else:
            print('Wrong answer: {0}, {1}'.format(result_1, result_2))


def max_pairwise_product_naive(numbers):
    n = len(numbers)
    max_product = 0
    for first in range(n):
        for second in range(first + 1, n):
            max_product = max(max_product,
                              numbers[first] * numbers[second])
    return max_product

def max_pairwise_product(numbers):
    n = len(numbers)
    #max_product = 0
    # for first in range(n):
    #     for second in range(first + 1, n):
    #         max_product = max(max_product,
    #                           numbers[first] * numbers[second])
    index_one = 0
    index_two = 0
    for i in range(1,n):
        if numbers[i] > numbers[index_one]:
            index_one = i

    if index_one == 0:
        index_two = 1

    for i in range(1,n):
        if i != index_one and numbers[i] > numbers[index_two]:
            index_two = i

    return numbers[index_one] * numbers[index_two]


if __name__ == '__main__':
    input_n = int(input())
    input_numbers = [int(x) for x in input().split()]
    print(max_pairwise_product(input_numbers))
    #print(max_pairwise_product_naive(input_numbers))
    #stress_test(10, 10000)
    # 
    # arr = []
    # for i in range(1, (2 * 10**5) +1):
    #     arr.append(i)
    
    #print(max_pairwise_product(arr))