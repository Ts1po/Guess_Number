import random


def guess_the_number():
    ran_num = random.randint(1, 50)
    max_attempts = 3
    attempts = 0

    while attempts < max_attempts:
        guess = int(input("Guess the number between 1 to 50: "))
        if guess < ran_num:
            print("Low, try again")
        elif guess < ran_num:
            print("High, try again")
        else:
            print("You guessed")
            break
        attempts += 1

    if attempts == max_attempts:
        print("You are out of attempts", ran_num)

    play_again = input("Do you want to play again? (yes/no): ")
    if play_again.lower() == "y":
        guess_the_number()


guess_the_number()
