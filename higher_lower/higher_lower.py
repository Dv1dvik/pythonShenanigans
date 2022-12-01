import random
from art import logo
from art import vs
from game_data import data


# score
score = 0

# creating a
a = random.choice(data)

game_is_running = True
while game_is_running:
    # creating b
    b = random.choice(data)
    while b == a:
        b =random.choice(data)

    # Just prints the info
    print(logo)
    print(f"Compare A: {a['name']}, a {a['description']}, from {a['country']}.")
    print(vs)
    print(f"Compare B: {b['name']}, a {b['description']}, from {b['country']}.")

    # comparing which one is higher
    winner = ""
    if a['follower_count'] > b['follower_count']:
        winner = a
        winner_check = "A"
    else:
        winner = b
        winner_check = "B"

    # # for testing purposes
    # print(f"This is just for testing. A is {a['follower_count']}")
    # print(f"This is just for testing. B is {b['follower_count']}")
    # print(winner)

    # input
    guess = input("Who has more followers? Type 'A' or 'B': ")

    # is the guess == winner?
    if winner_check == guess:
        score += 1
        print(f"That is correct! Your score is {score}")
        a = winner

    else:
        print(f"That is incorrect! Your reached score of {score}!")
        game_is_running = False