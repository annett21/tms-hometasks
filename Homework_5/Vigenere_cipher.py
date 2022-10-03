import string

alphabet = string.ascii_uppercase

message = input("Enter a message for encryption: ").upper()
key = input("Enter a key for encryption: ").upper()

encoded_symbols = []


for index in range(len(message)):
    alphabet_index = alphabet.index(message[index])
    key_index = alphabet.index(key[index % len(key)])
    symbol = alphabet[(alphabet_index + key_index) % len(alphabet)]
    encoded_symbols.append(symbol)

print("".join(encoded_symbols))
