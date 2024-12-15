import random

random_number = random.randint(1, 100)
valid_input = list(range(101))
random_number = str(random_number)
remaining_guesses = 15

difficulty_chosen = False

def divider():
    print("______________________________________________________________________________________________")
    print()

def start():
    global difficulty
    global difficulty_chosen

    if difficulty_chosen == False:
        print("Choose a difficulty:")
        print("1. Easy (Unlimited Guesses)")
        print(f"2. Hard (Limit of {remaining_guesses} guesses)")
        divider()
        difficulty = input("Enter a 1 or 2: ")
        pass
    else:
        pass

def unlimited_guesses():
    while True:
        divider()
        guess = input("I'm thinking of a number between 1 and 100, what is it?: ")
        if not guess.isnumeric():
            print("ERROR")
            print("Invalid Input, try again")
            input("Press any key to continue...")
            continue
        else:
            if guess == random_number:
                print("Correct!")
                print("Congratulation! You Win!")
                print("\n")
                input("Press any key to exit...")
                break
            elif guess != random_number:
                print("Incorrect, try again")
                input("Press any key to continue...")
                continue

def limited_guesses():
    while True:
        global remaining_guesses
        global random_number

        if remaining_guesses == 0:
            print("GAME OVER!")
            print("You've run out of guesses!")
            print(f"The correct answer was: {random_number}")
            break
        else:
            divider()

            guess = input("I'm thinking of a number between 1 and 100, what is it?: ")

            if not guess.isnumeric():
                print("ERROR")
                print("Invalid Input, try again")
                input("Press any key to continue...")
                continue
            else:
                guess = int(guess)
                random_number = int(random_number)

                if guess == random_number:
                    print("Correct!")
                    print("Congratulation! You Win!")
                    print("\n")
                    input("Press any key to exit...")
                    break
                elif guess != random_number:
                    remaining_guesses -= 1
                    print(f"Incorrect, you have {remaining_guesses} more attempts")
                    input("Press any key to continue...")
                    continue

while True:
    divider()
    start()
    if difficulty == "1":
        difficulty_chosen = True
        unlimited_guesses()
        break
    elif difficulty == "2":
        difficulty_chosen = True
        limited_guesses()
        break
    elif not difficulty.isnumeric():
        print("ERROR")
        print("Invalid input, try again")
        print()
        input("Press any key to continue...")
        continue
    else:
        pass
