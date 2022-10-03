def rec_prime(num, divider=None):
    divider = divider or num - 1
    if divider == 1:
        return True
    if num % divider == 0:
        return False
    return rec_prime(num, divider - 1)


number = int(input("Set a number: "))
print(f"Is {number} a prime number?")
print(rec_prime(number, divider=None))
