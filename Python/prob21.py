import math


def main():
    sumAmicable = 0
    for i in range(1, 10_001):
        sumI = sumDivisors(i)
        if sumDivisors(sumI) == i and sumI != i:
            sumAmicable += i
            print(i)
    print(sumAmicable)


def sumDivisors(num):
    sum = 0
    for i in range(1, int(math.sqrt(num)) + 1):
        if num % i == 0:
            sum += i
    return sum

if __name__ == '__main__':
    main()