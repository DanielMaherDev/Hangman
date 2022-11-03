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


def start_hangman(word, num_lives):
    word_blank = "_" * len(word)
    print(f'Your word contains {len(word)} characters')
    print(f'{word_blank}')


def make_guess(guess_number, num_lives, word):
    print(HANGMAN[guess_number])
    print(f'You have {num_lives} lives!')
    this_guess = input('Please choose a letter to guess:')
    try:
            if len(player_try) > 1:
                raise ValueError(
                    f" You can only guess 1 letter at a time, you guessed"
                    f" {len(player_try)} characters"
                )

            elif not player_try.isalpha():
                raise ValueError(
                    f" You can only guess letters, you guessed {(player_try)}"
                    f" which is not a letter"
                )

            elif len(player_try) == 1 and player_try.isalpha():
                if player_try in guesses:
                    raise ValueError(
                        f" You have already guessed {(player_try)}"
                    )

                elif player_try not in word:

                    message = f" {text_colors.RED}{(player_try)} is not in"\
                              f" the word. You lose a life.{text_colors.WHITE}"

                    guesses.append(player_try)
                    lives -= 1

                else:

                    message = f" {text_colors.GREEN}{player_try} is in the"\
                              f" word. Well done!{text_colors.WHITE}"

                    guesses.append(player_try)
                    word_template_list = list(word_template)
                    indices = [i for i, letter in enumerate(word)
                               if letter == player_try]
                    for index in indices:
                        word_template_list[index] = player_try
                        word_template = "".join(word_template_list)
                    if "_" not in word_template:
                        game_over = True

        except ValueError as e:
            print(f"{text_colors.RED}{e}.\n Please try again.\n"
                  f"{text_colors.WHITE}")
            continue
    

def main():
    """
    Run game functions
    """
    main_menu_choice = start_game()
    num_lives = set_difficulty()
    word = get_word()
    guess_number = 0
    if main_menu_choice == 1:
        start_hangman(word, num_lives)
        make_guess(guess_number, num_lives, word)
    elif main_menu_choice == 2:
        print('RULES')
    elif main_menu_choice == 3:
        print('leaderboard')
    else:
        return


main()
