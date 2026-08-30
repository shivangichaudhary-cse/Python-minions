import random

# Define the range dynamically
lower_bound = int(input("Enter the lower bound of the range: "))
upper_bound = int(input("Enter the upper bound of the range: "))

# Generate a random integer within the specified range
number = random.randint(lower_bound, upper_bound)

print("you got 10 guesses")

user_guesses = 10
user_guessed = 0

while user_guessed == user_guesses:
  user_guessed += 1
  user_number_guessed = int(input("So? "))
  if number == user_number_guessed :
    print("You won!!!")
    break
  else:
    print(f"You lose, it was actually {number}')
