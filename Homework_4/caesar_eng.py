import string


def caesar_eng(some_line: str, step: int) -> str:
    alphabet = string.ascii_lowercase
    coded_line = ""
    for letter in some_line.lower():
        if letter in alphabet:
            coded_line += alphabet[
                (alphabet.find(letter) + step) % len(alphabet)
            ]
        else:
            coded_line += letter
    return coded_line


some_line = input("Write something: ")
step = int(input("Set a step: "))

print("Coded line:", caesar_eng(some_line, step))
