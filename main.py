import random
import art

answer = random.randint(1, 100)
game_continue = True


def compare(guess):
    if guess == answer:
        print(f"You got it! The answer was {answer}")
        return False
    elif guess > answer:
        return "Too high"
    elif guess < answer:
        return "Too low"


def attempt(attempt_number):
    for i in range(attempt_number):
        i = attempt_number - i
        print(f"You have {i} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))
        print(compare(guess))
        if guess == answer:
            return False
        elif i > 1:
            print("Guess again.")
    print("You ran out of the number of guesses. You lose!\n")
    return False


while game_continue:
    print(art.logo)
    print("Guess a number between 1 and 100")
    choice = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    if choice == 'easy':
        attempt(10)
    else:
        attempt(5)
    continue_yn = input("Type 'yes' to play again, 'no' to quit: ")
    if continue_yn == 'yes':
        game_continue = True
    else:
        game_continue = False
        print("Good bye!")
        