import random
from words import list_of_words


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


#def start_hangman(word, num_lives):



def main():
    """
    Run game functions
    """
    main_menu_choice = start_game()
    set_difficulty()
    if main_menu_choice == 1:
        print('start game')
 #       start_hangman(word, num_lives)
    elif main_menu_choice == 2:
        print('RULES')
    elif main_menu_choice == 3:
        print('leaderboard')
    else:
        return

main()

