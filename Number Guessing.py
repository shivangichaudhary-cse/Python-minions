
"""
Simple number guessing game with input validation, helpful feedback, and
an automatically computed reasonable number of guesses based on the range.
"""
import math
import random

def get_int(prompt: str) -> int:
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Please enter a valid integer.")

def play_game():
    while True:
        lower = get_int("Enter the lower bound of the range: ")
        upper = get_int("Enter the upper bound of the range: ")
        if lower > upper:
            print("Lower bound must be less than or equal to upper bound. Please try again.")
            continue

        range_size = upper - lower + 1
        # Compute a reasonable number of guesses (binary-search based)
        suggested = 1 if range_size <= 1 else math.ceil(math.log2(range_size)) + 1
        max_guesses = max(1, suggested)

        print(f"You have {max_guesses} guesses to find the number between {lower} and {upper}.")

        secret = random.randint(lower, upper)
        attempts = 0

        while attempts < max_guesses:
            attempts += 1
            guess = get_int(f"Guess #{attempts}: ")

            if guess == secret:
                print(f"Correct! You found the number in {attempts} guess{'es' if attempts > 1 else ''}.")
                break
            elif guess < secret:
                print("Too low.")
            else:
                print("Too high.")

            remaining = max_guesses - attempts
            if remaining:
                print(f"{remaining} guess{'es' if remaining > 1 else ''} remaining.")
        else:
            print(f"Sorry — you ran out of guesses. The number was {secret}.")

        again = input("Play again? (y/n): ").strip().lower()
        if again not in ("y", "yes"):
            print("Thanks for playing!")
            break

if __name__ == "__main__":
    play_game()
