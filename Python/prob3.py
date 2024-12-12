import numpy as np
def main():
    maxFactor = 0
    num = 600851475143
    for i in range(1, int(np.sqrt(num))):
        if num % i == 0 and isPrime(i):
            maxFactor = max(maxFactor, i)
    print(maxFactor)

def isPrime(num):
    for i in range(2, num // 2):
        if num % i == 0:
            return False
    return True

if __name__ == '__main__':
    main()