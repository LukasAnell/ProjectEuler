def main():
    file = open("input13.txt", "r")
    print(str(sum([int(line.strip()) for line in file]))[:10])

if __name__ == '__main__':
    main()
