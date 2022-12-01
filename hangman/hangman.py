import random
from hangman_art import stages, logo
from hangman_words import word_list


end_of_game = False


#choose a random word
chosen_word = random.choice(word_list)
word_length = len(chosen_word)


#Set 'lives' to equal 6.
lives = 6

print(logo)

#Hide word in "_"
display = []
for _ in range(word_length):
    display += "_"

while not end_of_game:      #gameloop
    guess = input("Guess a letter: ").lower()

    if guess in display:
        print(f"You have alredy guessed {guess}")

    #Cheking if letter is in the chosen_word and it's position
    for position in range(word_length):
        letter = chosen_word[position]
       # print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
        if letter == guess:
            display[position] = letter


    #Then reduce 'lives' by 1.
    #If lives goes down to 0 then the game should stop and it should print "You lose."
    if guess not in chosen_word:
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose.")

    #Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")

    #Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("You win.")

    print(stages[lives])