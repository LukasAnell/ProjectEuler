def main():
    prev1 = 1
    prev2 = 0
    curr = 1
    i = 1
    while len(str(curr)) < 1_000:
        i += 1
        curr = prev1 + prev2
        prev2 = prev1
        prev1 = curr
    print(i)


if __name__ == '__main__':
    main()