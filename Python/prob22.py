def main():
    file = open("input22.txt", "r")
    line = [line for line in file][0]
    nameList = sorted(line.replace("\"", "").replace(",", " ").split(" "))
    sum = 0
    for i in range(len(nameList)):
        name = nameList[i]
        sum += alphabeticalValueSum(name) * (i + 1)
    print(sum)

def alphabeticalValueSum(name):
    return sum(ord(char.lower()) - 96 for char in name if char.isalpha())

if __name__ == '__main__':
    print(alphabeticalValueSum("COLIN"))
    main()
