def main():
    maxPalindrome = 0
    for i in range(1000, 100, -1):
        for j in range(1000, 100, -1):
            numString = str(i * j)
            if len(numString) % 2 == 1:
                continue
            firstHalf = numString[:len(numString) // 2]
            secondHalfRev = numString[len(numString) // 2:]
            secondHalfRev = secondHalfRev[::-1]
            if firstHalf == secondHalfRev:
                maxPalindrome = max(maxPalindrome, i * j)
    print(maxPalindrome)

if __name__ == '__main__':
    main()