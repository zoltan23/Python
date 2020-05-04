import json
from difflib import get_close_matches;

data = json.load(open('data.json'))


def getDef(word):
    word.lower()
    if word in data:
        return(data[word])
    elif len(get_close_matches(word, data.keys())) > 0:
        Yn = raw_input("Did you mean %s?" % get_close_matches(word, data.keys())[0])
        if Yn == "Y":
            return("Did you mean %s?" % get_close_matches(word, data.keys())[0])
        elif Yn == "N":
            return "Word does not exists.  Pleas check again!"
        else:
            return "Response not understood!" 
    else:
        return "Word does not exist!  Please try another word!"

user_input = raw_input("Enter a word:")

output = getDef(user_input)

for item in output:
    print(item)

