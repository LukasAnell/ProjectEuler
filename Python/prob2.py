def main():
    prev1 = 1
    prev2 = 0
    curr = 1
    sum = 0
    while curr < 4_000_000:
        if curr % 2 == 0:
            sum += curr
        curr = prev1 + prev2
        prev2 = prev1
        prev1 = curr
    print(sum)


if __name__ == '__main__':
    main()