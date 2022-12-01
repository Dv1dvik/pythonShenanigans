import random
from art import logo

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10,10]

# draw
def draw():
    drawing = []
    drawing.append(random.choice(cards))
    # changing 11 to 1 if conditions are met
    if sum(player_hand) + sum(drawing) > 21 and drawing[0] == 11:
        drawing = [1]
    elif sum(computer_hand) + sum(drawing) > 21 and drawing[0] == 11:
        drawing = [1]
    return sum(drawing)

# start draw
def starting_draw():
    starting_hand = []
    starting_hand.append(draw())
    starting_hand.append(draw())
    return starting_hand

# calculating if player loses or wins
def calculating():
    global computer_hand
    is_calculating = True
    while is_calculating:
        if sum(player_hand) > 21:
            return "You lose"
            is_calculating = False
        elif sum(computer_hand) < 17:
            computer_hand.append(draw())
            print("Computer draws a card.")
            print(computer_hand)
        elif sum(computer_hand) > 21:
                return "You win!"
                is_calculating = False
        elif sum(player_hand) == sum(computer_hand):
            return "It is a draw!"
            is_calculating = False
        elif sum(player_hand) < sum(computer_hand):
            return "You lose!"
            is_calculating = False
        elif sum(player_hand) > sum(computer_hand):
            return "You win!"
            is_calculating = False

starting_round = True
playing = True
infinite_loop = True
# looping the game
while infinite_loop:
    print(logo)
    player_hand = []
    computer_hand = []
    # looping the game
    while playing:
        # starting round
        if starting_round == True:
            # player hand
            player_hand = starting_draw()
            print(f"Your hand is {player_hand}")
            # computer hand
            computer_hand = starting_draw()
            print(f"Computer has in hand {computer_hand[0]} and 1 hidden card.")
            starting_round = False

        stand_or_hit = input("Do you want to stand 'y' or hit 'n'? ").lower()
        if stand_or_hit == "y":
            print(f"Your hand is {player_hand}.\nComputer's hand is {computer_hand}\n{calculating()}")
            playing = False
        # drawing a card
        else:
            player_hand.append(draw())
            print(f"Your hand is {player_hand}")
            print(f"Computer has in hand {computer_hand[0]} and 1 hidden card.")
            if sum(player_hand) > 21:
                print(f"Computer's hand is{computer_hand}.")
                print("You lose!")
                playing = False

    starting_round = True
    playing = True
    should_loop = input("Do you want to play again 'y' or not 'n'? ").lower()
    if should_loop == "n":
        infinite_loop = False