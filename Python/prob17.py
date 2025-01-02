from num2words import num2words


def main():
    sumLetters = 0
    for i in range(1, 1001):
        numWord: str = num2words(i)
        withoutDash = numWord.split('-')
        for word in withoutDash:
            sumLetters += len(word.replace(' ',''))
            print(word.replace(' ', ''))
    print(sumLetters)

if __name__ == '__main__':
    main()