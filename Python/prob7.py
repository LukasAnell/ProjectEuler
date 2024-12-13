import math


def main():
    numPrimes = 0
    i = 1
    while numPrimes < 10_000:
        i += 2
        isPrime = True
        for j in range(2, int(math.sqrt(i)) + 1):
            if i % j == 0:
                isPrime = False
                break
        if isPrime:
            numPrimes += 1
    print(i)

if __name__ == '__main__':
    main()