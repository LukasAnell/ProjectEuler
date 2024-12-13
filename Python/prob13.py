def main():
    file = open("input13.txt", "r")
    lines = [int(line.strip()) for line in file]
    print(str(sum(lines))[:10])

if __name__ == '__main__':
    main()
