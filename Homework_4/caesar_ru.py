def caesar_ru(some_line: str, step: int) -> str:
    alphabet = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
    coded_line = ""
    for letter in some_line.lower():
        if letter in alphabet:
            coded_line += alphabet[
                (alphabet.find(letter) + step) % len(alphabet)
            ]
        else:
            coded_line += letter
    return coded_line


some_line = input("Какую фразу зашифруем? ")
step = int(input("Set a step: "))

print("Зашифрованная строка:", caesar_ru(some_line, step))
