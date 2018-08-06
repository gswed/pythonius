import json

data = json.load(open("data.json"))

def getWord(w):
    w=w.lower()
    if w in data:
        return data[w]
    else:
        return "The word does not exist."

word = input("Enter a word: ")
print(getWord(word))
