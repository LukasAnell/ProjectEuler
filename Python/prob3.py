import math


def main():
    maxFactor = 0
    num = 600851475143
    for i in range(1, int(math.sqrt(num))):
        if num % i == 0 and isPrime(i):
            maxFactor = max(maxFactor, i)
    print(maxFactor)

def isPrime(num):
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

if __name__ == '__main__':
    main()