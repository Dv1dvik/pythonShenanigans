import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇

shapes = [rock, paper, scissors]

#player controls
player = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

if player < 0 or player > 2:
    print("You dared input invalid number. That means you lose!")

else:
    player_shape = shapes[player]

    #computer controls
    computer = random.randint(0,2)
    computer_shape = shapes[computer]

    #UI
    print(player_shape)
    print("Computer chose:")
    print(computer_shape)

    #win - lose - draw
    if player == computer:
        print("It is draw!")

    if player == 0 and computer == 1:
        print("You lose!")
    elif player == 0 and computer == 2:
        print("You win!")

    if player == 1 and computer == 2:
        print("You lose!")
    elif player == 1 and computer == 0:
        print("You win!")

    if player == 2 and computer == 0:
        print("You lose!")
    elif player == 2 and computer == 1:
        print("You win!")
