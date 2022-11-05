import random
from words import list_of_words

guesses = []

HANGMAN = (
        """
 |
 |
----------
""",
    """
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
    name = ""
    name = input('ENTER YOUR NAME:')
    while name == "":
        print('Please enter a name')
        name = input('ENTER YOUR NAME:')

    if name != "":
        print(f"\n Welcome, {name}")
        print("""
        Would you like to:
        1. Start Game
        2. Read The Rules
        3. View Leaderboard? \n \n""")
        print('Please enter the number which corresponds to your selection! \n')
        main_menu_choice = input('Number:')
        choice_made = False
        while choice_made != True:
                if main_menu_choice == "1":
                    return main_menu_choice
                    choice_made = True
                else:
                    print('Invalid option, please enter the numer which corresponds to one of the available options')
                    main_menu_choice = input('Number:')


def set_difficulty():
    print("""You have 3 Levels of Difficulty:
    1. Easy
    2. Medium
    3. Hard""")
    print('Please choose the number corresponding to your preferred level of difficulty')
    difficulty = input('Difficulty:')
    choice_made = False
    while choice_made != True:
        if difficulty == "1":
            choice_made = True
            num_lives = 9
        elif difficulty == "2":
            num_lives = 7
            choice_made = True
        elif difficulty == "3":
            num_lives = 5
            choice_made = True
        else:
            print('Invalid option, please enter the numer which corresponds to one of the available options')
            difficulty = input('Number:')
    return num_lives

def get_word():
    word = list_of_words[random.randint(0, len(list_of_words)-1)]
    return word


def make_guess(guess_number, num_lives, word, hangman_start_number):
    print(f'Your word contains {len(word)} characters')
    word_blank = "_" * len(word)
    word_blanks_as_list = [i for i in word_blank]
    word_as_list = [i for i in word]

    print(word_blank)
    game_over = False
    while not game_over and num_lives > 0:
        print(HANGMAN[hangman_start_number] + '\n')
        print(f'Your word: {word_blank}')

        print(f'You have {num_lives} lives! \n')
        guess_made = False
        while guess_made == False:
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
                    hangman_start_number += 1
                    guess_made = True
                else:
                    print(f'Great Guess! {this_guess} is in the word!')
                    guesses.append(this_guess)
                    guess_made = True
                    x = 0
                    while x < len(word):
                        if this_guess == word_as_list[x]:
                            word_blanks_as_list[x] = this_guess
                        x = x+1
                    word_blank = "".join(word_blanks_as_list)
                    if word_blank == word:
                        game_over = True
                        print(f"YOU WIN! The word was {word}. \nYou finished with {num_lives} guesses remaining!")
                            
                            
            except ValueError as e:
                print(f"{e}.\n Please try again.\n")
        if num_lives == 0:
            print(f'Unlucky. You ran out of lives! The correct word was {word}')


def main():
    """
    Run game functions
    """
    main_menu_choice = start_game()
    num_lives = set_difficulty()
    word = get_word()
    guess_number = 0
    if num_lives == 5:
        hangman_start_number = 4
    elif num_lives == 7:
        hangman_start_number = 2
    elif num_lives == 9:
        hangman_start_number = 0
    if main_menu_choice == "1":
        make_guess(guess_number, num_lives, word, hangman_start_number)
    elif main_menu_choice == "2":
        print('RULES')
    elif main_menu_choice == "3":
        print('leaderboard')
    else:
        return


main()
