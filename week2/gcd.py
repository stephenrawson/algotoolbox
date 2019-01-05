# From the lecture. Greatest Common Divisor
def gcd_fast(a, b):
    if b == 0:
        return a
    x = a % b
    return gcd_fast(b, x)

if __name__ == '__main__':
    input_numbers = [int(x) for x in input().split()]
    print(gcd_fast(input_numbers[0], input_numbers[1]))