import gspread
from google.oauth2.service_account import Credentials
import random
from words import list_of_words

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('Leaderboard')

global guesses
guesses = []


class colors:
    RED = "\033[1;31m"
    BLUE = "\033[1;34m"
    CYAN = "\033[1;36m"
    GREEN = "\033[0;32m"
    RESET = "\033[0;0m"
    BOLD = "\033[;1m"
    REVERSE = "\033[;7m"


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


def read_rules():
    print(f"""\n    {colors.BOLD}RULES
    
    {colors.RED}1. Choose your difficulty{colors.RESET}
            - Easy = 9 lives
            - Medium = 7 lives
            - Hard = 5 lives

   {colors.RED}2. Take a guess at one of the letters in the word!{colors.RESET}
            - If the letter is not in the word, you lose a life
              If the letter is in the word, it will show up, wherever in the
              word it is present!

    {colors.RED}3. You WIN by guessing the full word and saving HangMan{colors.RESET}

    {colors.RED}4. You LOSE if you run out of lives and HangMan is hung{colors.RESET}

    What would you like to do?

    {colors.GREEN}1. Play Game
    {colors.CYAN}2. View the leaderboard{colors.RESET}
     """)
    choice_made = False
    while choice_made is not True:
        choice = input('Number:\n')

        try:
            if choice == "1":
                choice_made = True
                num_lives = set_difficulty()
                make_guess(num_lives)
            elif choice == "2":
                choice_made = True
                display_leaderboard()
            else:
                raise ValueError("""WHOOPS! That is not a valid option!\n
Please enter a valid option, using the number which corresponds to your selection\n""")
        except ValueError as e:
            print(f"{colors.RED}{e}{colors.RESET}")


def display_leaderboard():
    leaderboard = SHEET.worksheet("leaderboard_sorted")
    scores = leaderboard.get_all_values()
    headers = scores.pop(0)
    i = 1
    for i in range(0, 3):
        headers[i] = "{:<15}".format(headers[i])
    print(f"""\nLEADERBOARD - TOP 10\n\n-----------------------------------
{colors.BOLD}{headers[0]} {headers[1]} {headers[2]}{colors.RESET}\n""")
    for score in scores[0:10]:
        for i in range(0, 3):
            score[i] = "{:<15}".format(score[i])
       
        print(f"{score[0]} {score[1]} {colors.GREEN}{score[2]}{colors.RESET}")
    print("\n-----------------------------------")
    print(f"""What would you like to do?\n
    {colors.BLUE}1. Play Game\n
    {colors.RED}2. Read rules\n""")
    choice_made = False
    while choice_made is not True:
        choice = input('Number:\n')

        try:
            if choice == "1":
                choice_made = True
                num_lives = set_difficulty()
                make_guess(num_lives)
            elif choice == "2":
                choice_made = True
                read_rules()
            else:
                raise ValueError("""WHOOPS! That is not a valid option!\n
Please enter a valid option, using the number which corresponds to your selection\n""")
        except ValueError as e:
            print(f"{colors.RED}{e}{colors.RESET}")

def start_game():
    global guesses
    guesses = []

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

\n""")

    print(f'WELCOME TO {colors.BLUE}HANGMAN!!{colors.RESET}\n')

    print('What is your name? \n')

    global name 
    name = ""
    name_given = False
    while name_given is False:
        name = input('ENTER YOUR NAME:\n')
        name = name.upper()
        try:
            if name == "":
                raise ValueError('Please enter a name')
            if len(name) > 10:
                raise ValueError('please enter a name of 10 or less'
                                 + ' characters')
            if not name.isalnum():
                raise ValueError('Please enter a name')
            else:
                name_given = True
                print(f"\nWelcome, {colors.GREEN}{name}{colors.RESET}")
                print("""
  O
 |+-/
  |
  |
 | |
 | |
                """)
                print(f"""
Would you like to:\n
{colors.BLUE}1. Start Game \n
{colors.RED}2. Read Rules \n
{colors.GREEN}3. View Leaderboard{colors.RESET} \n""")
                print(f'Please enter the {colors.RED}number{colors.RESET} which corresponds to your'
                      + 'selection! \n')
                choice_made = False
                while choice_made is False:
                    main_menu_choice = input('Number:\n')
                    try:
                        if main_menu_choice == "1":
                            return main_menu_choice
                            choice_made = True
                        elif main_menu_choice == "2":
                            return main_menu_choice
                            choice_made = True
                        elif main_menu_choice == "3":
                            return main_menu_choice
                            choice_made = True
                        else:
                            raise ValueError("""WHOOPS! That is not a valid option!\n
            Please enter a valid option, using the number which corresponds to your selection\n""")
                    except ValueError as e:
                        print(f"{colors.RED}{e}{colors.RESET}")
        except ValueError as e:
            print(f"\n{colors.RED}{e}.\nPlease try again.{colors.RESET}\n")


def set_difficulty():
    print(f"""  ___   _    _  _____  _____  _____ ___  ___ _____ 
 / _ \ | |  | ||  ___|/  ___||  _  ||  \/  ||  ___|
/ /_\ \| |  | || |__  \ `--. | | | || .  . || |__  
|  _  || |/\| ||  __|  `--. \| | | || |\/| ||  __| 
| | | |\  /\  /| |___ /\__/ /\ \_/ /| |  | || |___ 
\_| |_/ \/  \/ \____/ \____/  \___/ \_|  |_/\____/ 
                                                   
                                                   
Lets play! \n \nYou have 3 Levels of Difficulty:\n
    {colors.GREEN}1. Easy\n
    {colors.CYAN}2. Medium\n
    {colors.RED}3. Hard{colors.RESET}\n""")
    print('Please choose the number corresponding to your preferred level of'
          + 'difficulty \n')
    choice_made = False
    while choice_made is not True:
        difficulty = input('Difficulty:\n')
        try:
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
                raise ValueError("""WHOOPS! That is not a valid option!\n
Please enter a valid option, using the number which corresponds to your selection\n""")
        except ValueError as e:
            print(f"{colors.RED}{e}{colors.RESET}")
    return num_lives

def get_word():
    word = list_of_words[random.randint(0, len(list_of_words)-1)]
    return word


def make_guess(num_lives):
    guesses = []
    if num_lives == 5:
        difficulty = 'Hard'
        hangman_start_number = 4
    elif num_lives == 7:
        difficulty = 'Medium'
        hangman_start_number = 2
    elif num_lives == 9:
        difficulty = 'Easy'
        hangman_start_number = 0
    guess_number = 0
    word = get_word()

    print(f'\nLets do this!\n \nYour word contains {colors.GREEN}{len(word)}{colors.RESET} characters')
    word_blank = "_" * len(word)
    word_blanks_as_list = [i for i in word_blank]
    word_as_list = [i for i in word]

    game_over = False
    while not game_over and num_lives > 0:
        print(HANGMAN[hangman_start_number] + '\n')
        print(f'Your word: {word_blank} \n')

        print(f'You have {num_lives} lives! \n')
        guess_made = False
        while guess_made == False:
            if guess_number > 0:
                guess_list = " ".join(guesses)
                print(f'\nGuesses: {colors.BOLD}{guess_list}{colors.RESET} \n')
            this_guess = input('Please choose a letter to guess:\n').lower()
            try:
                if len(this_guess) > 1:
                    raise ValueError(
                    f'You can only guess 1 letter, but you guessed {len(this_guess)} characters!'
                    )
                elif this_guess == "":
                    raise ValueError(
                    f'You need to enter a guess.'
                    )
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
                    print(f"{colors.RED}{this_guess} is not in the word. You lose a life!{colors.RESET}")
                    guesses.append(this_guess)
                    num_lives -= 1
                    guess_number += 1
                    hangman_start_number += 1
                    guess_made = True
                else:
                    print(f'\n{colors.GREEN}Great Guess!{colors.BOLD} {this_guess}{colors.RESET}{colors.GREEN} is in the word!{colors.RESET}')
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
                        print(f"""\n{colors.GREEN}  /$$     /$$  /$$$$$$  /$$   /$$       /$$      /$$ /$$$$$$ /$$   /$$
|  $$   /$$/ /$$__  $$| $$  | $$      | $$  /$ | $$|_  $$_/| $$$ | $$
 \  $$ /$$/ | $$  \ $$| $$  | $$      | $$ /$$$| $$  | $$  | $$$$| $$
  \  $$$$/  | $$  | $$| $$  | $$      | $$/$$ $$ $$  | $$  | $$ $$ $$
   \  $$/   | $$  | $$| $$  | $$      | $$$$_  $$$$  | $$  | $$  $$$$
    | $$    | $$  | $$| $$  | $$      | $$$/ \  $$$  | $$  | $$\  $$$
    | $$    |  $$$$$$/|  $$$$$$/      | $$/   \  $$ /$$$$$$| $$ \  $$
    |__/     \______/  \______/       |__/     \__/|______/|__/  \__/
                                                                     
                                                                     
                                                                     
                                
                                
                                {colors.RESET} \n \nThe word was {colors.GREEN}{word.upper()}{colors.RESET}.\n \nYou finished with {colors.GREEN}{num_lives}{colors.RESET} guesses remaining!""")
                        new_score = [name, difficulty, num_lives]
                        worksheet_to_update = SHEET.worksheet('leaderboard')
                        worksheet_to_update.append_row(new_score)
                        print('\nYour Score has been added to the leaderboard')       
                if num_lives == 0:
                    game_over = True
                    print(HANGMAN[hangman_start_number] + '\n')
                    print(f"""{colors.RED} /$$     /$$  /$$$$$$  /$$   /$$       /$$        /$$$$$$   /$$$$$$  /$$$$$$$$
|  $$   /$$/ /$$__  $$| $$  | $$      | $$       /$$__  $$ /$$__  $$| $$_____/
 \  $$ /$$/ | $$  \ $$| $$  | $$      | $$      | $$  \ $$| $$  \__/| $$      
  \  $$$$/  | $$  | $$| $$  | $$      | $$      | $$  | $$|  $$$$$$ | $$$$$   
   \  $$/   | $$  | $$| $$  | $$      | $$      | $$  | $$ \____  $$| $$__/   
    | $$    | $$  | $$| $$  | $$      | $$      | $$  | $$ /$$  \ $$| $$      
    | $$    |  $$$$$$/|  $$$$$$/      | $$$$$$$$|  $$$$$$/|  $$$$$$/| $$$$$$$$
    |__/     \______/  \______/       |________/ \______/  \______/ |________/
                                                                              
                                                                              
                                                                              \n\nUnlucky! You ran out of lives! \n\nThe correct word was {word}{colors.RESET}\n""")
            except ValueError as e:
                        print(f"\n{colors.RED}{e}.\n Please try again.{colors.RESET}\n")
    if game_over == True:       
        print(f"""Would you like to:
        {colors.RED}1. View the leaderboard
        {colors.GREEN}2. Play Again
        {colors.BLUE}3. Read Rules{colors.RESET}""")
        print('Please choose the number that corresponds to your selection')  
        choice_made = False
        while choice_made != True:
            choice = input('Number:\n')
            try:
                if choice == "1":
                    choice_made = True
                    display_leaderboard()
                elif choice == "2":
                    num_lives = set_difficulty()
                    make_guess(num_lives)
                elif choice == "3":
                    choice_made = True
                    read_rules()
                else:
                    raise ValueError("""WHOOPS! That is not a valid option!\n
Please enter a valid option, using the number which corresponds to your selection\n""")
            except ValueError as e:
                print(f"{colors.RED}{e}{colors.RESET}")
def main():

    """
    Run game functions
    """
    main_menu_choice = start_game()
    if main_menu_choice == "1":
        num_lives = set_difficulty()
        if num_lives == 5:
            difficulty = 'Hard'
            hangman_start_number = 4
        elif num_lives == 7:
            difficulty = 'Medium'
            hangman_start_number = 2
        elif num_lives == 9:
            difficulty = 'Easy'
            hangman_start_number = 0
        make_guess(num_lives)
    elif main_menu_choice == "2":
        read_rules()    
    elif main_menu_choice == "3":
        display_leaderboard()
    else:
        return


main()