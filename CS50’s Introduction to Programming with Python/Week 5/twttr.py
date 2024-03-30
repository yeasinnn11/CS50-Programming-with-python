def main():
    prompt = input('Input: ')
    print(shorten(prompt))

def shorten(word):
    for vowel in ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']:
        word = word.replace(vowel, '')
    return word


if __name__ == "__main__":
    main()
