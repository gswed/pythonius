import json
from difflib import get_close_matches

data = json.load(open("data.json"))

def getWord(w):
    w=w.lower()
    if w in data:
        return data[w]
    elif len(get_close_matches(w, data.keys()))>0:
        matches = input("Close matches found: %s , Enter X to close, or the index of the desired match: " %get_close_matches(w, data.keys()))
        if matches == "X" or matches=="x":
            return "Thank you!"
        else:
            try:
                int(matches)
                if int(matches)<len(get_close_matches(w, data.keys())):
                    return data[get_close_matches(w, data.keys())[int(matches)]]
            except ValueError:
                return "Sorry, please enter X or the desired index"
            return "Index out of bounds."
    else:
        return "The word does not exist."

word = input("Enter a word: ")
print(getWord(word))
