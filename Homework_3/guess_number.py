from random import randint

number = randint(1, 100)
attempt = 10
game_over = False


def continue_play():
    print("Do you want to play again?")
    return input("y/n ")


while not game_over:
    while attempt > 0:
        print(f"You have {attempt} attempts")
        guesed_number = int(input("Try to guese a number from 1 too 100: "))
        attempt -= 1
        if guesed_number == number:
            print("You won!")
            break
        elif attempt == 0:
            print("You lose!")
            break
        elif guesed_number > number:
            print("Too big, try smaller one")
        elif guesed_number < number:
            print("Too small, try bigger one")
    if continue_play() == "n":
        game_over = True
    else:
        attempt = 10
