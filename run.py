import random
from words import list_of_words

guesses = []

HANGMAN = (
    """
 ------
 |    |
 |
 |
 |
 |
 |
 |
 |
----------
""",
"""
 ------
 |    |
 |    O
 |
 |
 |
 |
 |
 |
----------
""",
"""
 ------
 |    |
 |    O
 |   -+-
 | 
 |   
 |   
 |   
 |   
----------
""",
"""
 ------
 |    |
 |    O
 |  /-+-
 |   
 |   
 |   
 |   
 |   
----------
""",
"""
 ------
 |    |
 |    O
 |  /-+-/
 |   
 |   
 |   
 |   
 |   
----------
""",
"""
 ------
 |    |
 |    O
 |  /-+-/
 |    |
 |   
 |   
 |   
 |   
----------
""",
"""
 ------
 |    |
 |    O
 |  /-+-/
 |    |
 |    |
 |   | 
 |   | 
 |   
----------
""",
"""
 ------
 |    |
 |    O
 |  /-+-/
 |    |
 |    |
 |   | |
 |   | |
 |  
----------
""")


def start_game():
    """
    Initial screen upon game load
    """
    print("""

 __ __   ____  ____    ____  ___ ___   ____  ____  
|  |  | /    ||    \  /    ||   |   | /    ||    \ 
|  |  ||  o  ||  _  ||   __|| _   _ ||  o  ||  _  |
|  _  ||     ||  |  ||  |  ||  \_/  ||     ||  |  |
|  |  ||  _  ||  |  ||  |_ ||   |   ||  _  ||  |  |
|  |  ||  |  ||  |  ||     ||   |   ||  |  ||  |  |
|__|__||__|__||__|__||___,_||___|___||__|__||__|__|


    """)

    print('Welcome to HangMan!\n')
    print('What is your name?\n \n')
    name = input('ENTER YOUR NAME:')
    print(f"\n Welcome, {name}")
    print("""
    Would you like to:
    1. Start Game
    2. Read The Rules
    3. View Leaderboard? \n \n""")
    print('Please enter the number which corresponds to your selection! \n')
    main_menu_choice = int(input('Number:'))
    return main_menu_choice


def set_difficulty():
    num_lives = 7
    return num_lives


def get_word():
    word = list_of_words[random.randint(0, len(list_of_words)-1)]
    return word

def make_guess(guess_number, num_lives, word):
    print(f'Your word contains {len(word)} characters')
    word_blank = "_" * len(word)
    word_as_list = [i for i in word]
    print(word_as_list)
    game_over = False
    while not game_over and num_lives > 0:
        print(HANGMAN[guess_number] + '\n')
        print(f'Your word: {word_blank}')

        print(f'You have {num_lives} lives! \n')
        this_guess = input('Please choose a letter to guess:')
        try:
            if len(this_guess) > 1:
                raise ValueError(
                f'You can only guess 1 letter, but you guessed {len(this_guess)} characters! \n'
                )
            elif this_guess == "":
                print('Please enter a guess')                    
            elif (len(this_guess) == 1 and this_guess.isalpha() 
                  and this_guess in guesses):
                raise ValueError(
                f'"{this_guess}" has already been guessed.'
                )
            elif not this_guess.isalpha():
                raise ValueError(
                f" Only letters are valid guesses, but you guessed {this_guess}"
                )
            elif this_guess not in word:
                print(f"{this_guess} is not in the word. You lose a life!")
                guesses.append(this_guess)
                print(guess_number)
                num_lives -= 1
                guess_number += 1
            else:
                print(f'Great Guess! {this_guess} is in the word!')
                guesses.append(this_guess)
                x = 0
                #for x in word:
                 #   if this_guess == word[x]
                        
                        
        except ValueError as e:
            print(f"{e}.\n Please try again.\n")


def main():
    """
    Run game functions
    """
    main_menu_choice = start_game()
    num_lives = set_difficulty()
    word = get_word()
    guess_number = 0
    game_over = False
    if main_menu_choice == 1:
        make_guess(guess_number, num_lives, word)
    elif main_menu_choice == 2:
        print('RULES')
    elif main_menu_choice == 3:
        print('leaderboard')
    else:
        return


main()
