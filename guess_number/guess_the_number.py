import random
from art import logo

# calculaton
def calculation():
        global guess
        # Let player make guess
        guess = int(input("What is your guess? "))
        # compairing guess with number
        if guess == number:
            return f"You got it! The number was {guess}."
        elif guess < number:
            return "Too low."
        elif guess > number:
            return "Too high."


# Starting
print(logo)
print("Welcome, this is Guess the Number game.\nI'll think a random number between 1 and 100.\nYour goal is to guess this number.")
# random number
number = random.randint(1,100)
print(number)

# Number of guesses
difficulty = input("For starters, do you want this to be 'easy or 'hard'? ")
num_of_tries = 0
if difficulty == "hard":
    num_of_tries += 5
elif difficulty == "easy":
    num_of_tries += 10
else:
    print("Wrong input!")

#running the game
while num_of_tries > 0:
    # Letting player know how many attempts they have left
    print(f"You have {num_of_tries} attempts to guess the number.")
    print(calculation())
    num_of_tries -= 1
    # Ending the loop
    if num_of_tries == 0:
        print("You are out of guesses, you lose!")
    elif guess == number:
         num_of_tries = 0