import string


def caesar_eng(some_line: str, step: int) -> str:
    alphabet = string.ascii_letters
    coded_line = ""
    for letter in some_line:
        if letter in alphabet:
            coded_index = (alphabet.find(letter) + step) % len(alphabet)
            coded_line += alphabet[coded_index]
        else:
            coded_line += letter
    return coded_line


path = "Homework_7/for_cipher.txt"
with open(path, "r") as f:
    step = 1
    for line in f:
        print(caesar_eng(line, step), end="")
        step += 1
    print()
