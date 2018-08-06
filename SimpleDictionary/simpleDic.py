import json
from difflib import get_close_matches

data = json.load(open("data.json"))

def getWord(w):
    w=w.lower()
    if w in data:
        return data[w]
    elif len(get_close_matches(w, data.keys()))>0:
        matches = get_close_matches(w, data.keys())
        response = input("Close matches found: %s , Enter X to close, or the index of the desired match: " %get_close_matches(w, data.keys()))
        if response == "X" or response=="x":
            return "Thank you!"
        else:
            try:
                index = int(response)
                if index<len(matches):
                    return data[matches[index]]
            except ValueError:
                return "Sorry, please enter X or the desired index"
            return "Index out of bounds."
    else:
        return "The word does not exist."

word = input("Enter a word: ")
output = getWord(word)
if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)
