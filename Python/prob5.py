def main():
    i = 0
    while True:
        i += 20
        divisible = True
        for j in range(2, 21):
            if i % j != 0:
                divisible = False
                break
        if divisible:
            break
    print(i)

if __name__ == '__main__':
    main()