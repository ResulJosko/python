a = {"kitap" : "book",
"bilim" : "knowledge",
"kompyuter" : "computer"}

key = input('Enter the word: ')
if key in a:
    print(key, "-", a[key])
else:
    print("The word isn't in the dictionary")