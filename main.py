# Welcome to Hangman game - can you guess the name of the movie? (Only movie titles)
import random
import hangman_functions

# Printing introduction

# Creating movie pool
mov_pool = ["Dune", "Pulp Fiction", "The Godfather", "The Lord Of the Rings", "The Shawshank Redemption", "Fight Club",
            "Star Wars", "The Matrix", "Goodfellas", "The Silence of the Lambs", "Back to the Future", "Memento",
            "WALL-E", "Oldboy", "Reservoir Dogs", "Requiem for a Dream", "A Clockwork Orange", "Blade Runner", "Fargo",
            "Trainspotting", "The Big Lebowski", "The Hitchhiker's Guide to the Galaxy", "Pan's Labyrinth", "Seven",
            "Die Hard", "Ghostbusters", "Blazing Saddles", "Vertigo", "Raging Bull", "Taxi Driver", "Titanic", "Alien",
            "The Shining", "Apocalypse Now", "Gone With the Wind", "Forrest Gump", "Citizen Kane", "The Green Mile"
            ]

# Choosing random word form the list
chosen_word = random.choice(mov_pool).lower()
# print(chosen_word)

# Generating display for the player, to track guesses
display = []
for letter in chosen_word:
    if letter == " ":
        display += letter
    elif letter == "'":
        display += letter
    elif letter == "-":
        display += letter
    else:
        display += "_"

# Player lives
player_lives = 6
# Asking the player for the letter
game_on = True
while game_on:
    guess = input("Choose your letter: ").lower()
    letter_i = -1
    for letter in chosen_word:
        letter_i += 1
        if letter == guess:
            display[letter_i] = letter
    print(hangman_functions.stages[player_lives])
    print(''.join(display))

    if guess not in chosen_word:
        player_lives -= 1
        print(hangman_functions.stages[player_lives])
        if player_lives == 0:
            print("You lose!")
            print(f"Right movie was: {chosen_word.capitalize()} !")
            game_on = False

    elif list(chosen_word) == display:
        game_on = False
        print("You Win!!!")
        print(f"Movie was: {chosen_word.capitalize()} !")
