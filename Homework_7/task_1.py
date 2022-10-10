import re


path = "Homework_7/text_1.txt"
path_two = "Homework_7/forbidden_words.txt"


def censorship(path):
    with open(path, "r") as f, open(path_two) as f2:
        source = f.read()
        censor = f2.read().split(" ")
    for word in censor:
        source = re.sub(word, "*" * len(word), source, flags=re.IGNORECASE)
    return source


print(censorship(path))
