import math


def main():
    triangleNum = 0
    i = 1
    numDivisors = 0
    while numDivisors < 500:
        triangleNum = int(1/2 * (i**2 + i))
        i += 1
        numDivisors = countDivisors(triangleNum)
    print(str(triangleNum) + " " + str(numDivisors))

def countDivisors(num):
    count = 1
    for i in range(1, int(math.sqrt(num)) + 1):
        if num % i == 0:
            count += 2
    return count


if __name__ == '__main__':
    main()