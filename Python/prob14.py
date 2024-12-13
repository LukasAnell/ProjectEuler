def main():
    longestChain = 0
    number = 0
    for i in range(1, 1_000_000):
        steps = collatz(i)
        if longestChain < steps:
            longestChain = steps
            number = i
    print(number)

def collatz(num):
    steps = 0
    while num != 4:
        if num % 2 == 0:
            num /= 2
        else:
            num = 3 * num + 1
        steps += 1
    return steps

if __name__ == '__main__':
    main()