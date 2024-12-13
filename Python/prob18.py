def main():
    file = open("input18.txt", "r")
    numList = [[int(num) for num in line.split()] for line in file]
    for r in reversed(range(len(numList) - 1)):
        row = numList[r]
        for c in range(len(row)):
            row[c] += max(int(numList[r + 1][c]), int(numList[r + 1][c + 1]))
    print(numList[0][0])
if __name__ == '__main__':
    main()