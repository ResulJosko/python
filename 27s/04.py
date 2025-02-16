def replace_vowels(text):
    vowels = "AEIOUYaeiouy"
    for vowel in vowels:
        text = text.replace(vowel, "*")
    return text

text = input("Bir setir girizin: ")
print("Calyshlan setir: ", replace_vowels(text))