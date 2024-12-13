import math


def main():
    sum = 0
    for i in range(2, 2_000_001):
        if isPrime(i):
            sum += i
    print(sum)

def isPrime(num):
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

if __name__ == "__main__":
    main()