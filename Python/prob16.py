def main():
    num = str(2**1000)
    sum = 0
    for i in range(len(num)):
        sum += int(num[i])
    print(sum)

if __name__ == '__main__':
    main()