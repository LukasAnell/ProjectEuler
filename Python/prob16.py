def main():
    num = str(2**1000)
    sumDigits = sum(int(num[i]) for i in range(len(num)))
    print(sumDigits)

if __name__ == '__main__':
    main()