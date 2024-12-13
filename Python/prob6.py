def main():
    sumOfSquares = 0
    squareOfSum = 0
    for i in range(1, 101):
        sumOfSquares += i * i
        squareOfSum += i
    squareOfSum = squareOfSum ** 2
    print(squareOfSum - sumOfSquares)

if __name__ == '__main__':
    main()