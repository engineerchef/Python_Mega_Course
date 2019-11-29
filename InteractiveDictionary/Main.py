import json
# from difflib import SequenceMatcher
from difflib import get_close_matches

data = json.load(open("data.json"))


def main():
    word = input("Enter word: ")
    word = word.strip()
    output = translate(word)
    if type(output) == list:
        for i in output:
            print(i)
    else:
        print(output)


def translate(w: str):
    if w in data:
        return data[w]
    elif w.lower() in data:
        return data[w.lower()]
    elif w.title() in data:
        return data[w.title()]
    elif w.upper() in data:
        return data[w.upper()]
    elif len(get_close_matches(w, data.keys())) > 0:
        yn = input(
            "Did you mean '{}' instead? Enter Y if yes, or N if no. ".format(get_close_matches(w, data.keys())[0]))
        if yn == "Y" or yn == "y":
            return data[get_close_matches(w, data.keys())[0]]
        elif yn == "N" or yn == "n":
            exit()
        else:
            return "Did't understand your entry!!!"
    else:
        return "There is no word found in dictionary like '{}'".format(w)


if __name__ == '__main__':
    main()
