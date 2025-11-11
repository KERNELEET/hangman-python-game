import random
import colorama
from colorama import init, Back, Fore, Style
# Initialize Colorama
colorama.init()
print(Fore.BLACK + Back.YELLOW + " " )
def startmenu():
print('''

__________ ▄▄▄▄▄▄
| HELP ME! | | █
¯¯¯¯¯¯¯¯¯¯ ° █ ▒▒▒▒▒▒▒▒
█▄██▄█ \O/ █ ▒▒▌▒▒▐▒▒▌▒
█▄█▄█▄█▄█▐█┼██▌█▄█▄█▄█▄█ | █ ▒▀▄▒▌▄▀▒
███┼█████▐████▌█████┼███ / \ █ ██
░░░░░░█████████▐████▌█████████░░░░░░████████████░░░░░░░░░░░░░██░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
''')
def header():
print( '''

▄█ █▄ ▄██████ ███▄▄▄ ▄████▄ ▄▄▄███▄▄▄ ▄██████ ███▄▄▄
███ ███ ███ ███ ███▀▀██▄ ███ ███ ▄██▀▀███▀▀██▄ ███ ███ ███▀▀██▄
███ ███ ███ ███ ███ ███ ███ █▀ ███ ███ ███ ███ ███ ███ ███
▄███▄▄███▄▄ ███ ███ ███ ███ ▄███ ███ ███ ███ ███ ███ ███ ███
▀▀███▀▀███▀ ▀█████████ ███ ███ ▀▀███ ███▄ ███ ███ ███ ▀█████████ ███ ███
███ ███ ███ ███ ███ ███ ███ ███ ███ ███ ███ ███ ███ ███ ███
███ ███ ███ ███ ███ ███ ███ ███ ███ ███ ███ ███ ███ ███ ███
███ █▀ ███ █▀ ▀█ █▀ ██████▀ ▀█ ███ █▀ ███ █▀ ▀█ █▀
''')
print(" WELCOME TO HANGMAN!!! ")
print(" ===================== ")
def turn0():
print('''


▒▒▒▒▒▒▒▒
█▄██▄█ ▒▒▌▒▒▐▒▒▌▒
█▄█▄█▄█▄█▐█┼██▌█▄█▄█▄█▄█ ▒▀▄▒▌▄▀▒
███┼█████▐████▌█████┼███ ██
░░░░░░█████████▐████▌█████████░░░░░░████████████░░░░░░░░░░░░░██░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
''')
def turn1():
print('''

█
█ ▒▒▒▒▒▒▒▒
█▄██▄█ █ ▒▒▌▒▒▐▒▒▌▒
█▄█▄█▄█▄█▐█┼██▌█▄█▄█▄█▄█ █ ▒▀▄▒▌▄▀▒
███┼█████▐████▌█████┼███ █ ██
░░░░░░█████████▐████▌█████████░░░░░░████████████░░░░░░░░░░░░░██░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
''')
def turn2():
print('''
▄▄▄▄▄▄
█
█ ▒▒▒▒▒▒▒▒
█▄██▄█ █ ▒▒▌▒▒▐▒▒▌▒
█▄█▄█▄█▄█▐█┼██▌█▄█▄█▄█▄█ █ ▒▀▄▒▌▄▀▒
███┼█████▐████▌█████┼███ █ ██
░░░░░░█████████▐████▌█████████░░░░░░████████████░░░░░░░░░░░░░██░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
''')
def turn3():
print('''
▄▄▄▄▄▄
| █
█ ▒▒▒▒▒▒▒▒
█▄██▄█ █ ▒▒▌▒▒▐▒▒▌▒
█▄█▄█▄█▄█▐█┼██▌█▄█▄█▄█▄█ █ ▒▀▄▒▌▄▀▒
███┼█████▐████▌█████┼███ █ ██
░░░░░░█████████▐████▌█████████░░░░░░████████████░░░░░░░░░░░░░██░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
''')
def turn4():
print('''
▄▄▄▄▄▄
| █
O █ ▒▒▒▒▒▒▒▒
█▄██▄█ █ ▒▒▌▒▒▐▒▒▌▒
█▄█▄█▄█▄█▐█┼██▌█▄█▄█▄█▄█ █ ▒▀▄▒▌▄▀▒
███┼█████▐████▌█████┼███ █ ██
░░░░░░█████████▐████▌█████████░░░░░░████████████░░░░░░░░░░░░░██░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
''')
def turn5():
print( '''
▄▄▄▄▄▄
| █
O █ ▒▒▒▒▒▒▒▒
█▄██▄█ | █ ▒▒▌▒▒▐▒▒▌▒
█▄█▄█▄█▄█▐█┼██▌█▄█▄█▄█▄█ █ ▒▀▄▒▌▄▀▒
███┼█████▐████▌█████┼███ █ ██
░░░░░░█████████▐████▌█████████░░░░░░████████████░░░░░░░░░░░░░██░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
''')
def turn6():
print('''
▄▄▄▄▄▄
| █
O █ ▒▒▒▒▒▒▒▒
█▄██▄█ /| █ ▒▒▌▒▒▐▒▒▌▒
█▄█▄█▄█▄█▐█┼██▌█▄█▄█▄█▄█ █ ▒▀▄▒▌▄▀▒
███┼█████▐████▌█████┼███ █ ██
░░░░░░█████████▐████▌█████████░░░░░░████████████░░░░░░░░░░░░░██░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
''')
def turn7():
print( '''
▄▄▄▄▄▄
| █
O █ ▒▒▒▒▒▒▒▒
█▄██▄█ /|\ █ ▒▒▌▒▒▐▒▒▌▒
█▄█▄█▄█▄█▐█┼██▌█▄█▄█▄█▄█ █ ▒▀▄▒▌▄▀▒
███┼█████▐████▌█████┼███ █ ██
░░░░░░█████████▐████▌█████████░░░░░░████████████░░░░░░░░░░░░░██░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
''')
def turn8():
print('''
▄▄▄▄▄▄
| █
O █ ▒▒▒▒▒▒▒▒
█▄██▄█ /|\ █ ▒▒▌▒▒▐▒▒▌▒
█▄█▄█▄█▄█▐█┼██▌█▄█▄█▄█▄█ / █ ▒▀▄▒▌▄▀▒
███┼█████▐████▌█████┼███ █ ██
░░░░░░█████████▐████▌█████████░░░░░░████████████░░░░░░░░░░░░░██░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
''')
def turn9():
print('''
_______________ ▄▄▄▄▄▄
| OUCH MY NECK! | | █
¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯\ O █ ▒▒▒▒▒▒▒▒
█▄██▄█ /|\ █ ▒▒▌▒▒▐▒▒▌▒
█▄█▄█▄█▄█▐█┼██▌█▄█▄█▄█▄█ / \ █ ▒▀▄▒▌▄▀▒
███┼█████▐████▌█████┼███ █ ██
░░░░░░█████████▐████▌█████████░░░░░░████████████░░░░░░░░░░░░░██░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
''')
def hangman():
# Wordlist consists of the words that the user will have to guess
wordlist = ['ahmed', 'python', 'programming', 'snake', 'oreo']
word = random.choice(wordlist)
# We use the random function to get a random word from the wordlist

turns = 10
guessmade = ''
valid = set('abcdefghijklmnopqrstuvwxyz')

while len(word) > 0 and turns > 0:
main_word = ''
for letter in word:
if letter in guessmade:
main_word += letter
else:
main_word += "_ "

# Move the check for winning here
if main_word == word:
print(main_word)
print("You Won!")
break

print("Guess The Word", main_word)
guess = input("Enter a letter: ").lower()

if guess in valid:
guessmade += guess
else:
print("Invalid input. Please enter a valid letter.")
continue

if guess not in word:
turns = turns - 1

if turns == 9:
turn0()
if turns == 8:
turn1()
if turns == 7:
turn2()
if turns == 6:
turn3()
if turns == 5:
turn4()
if turns == 4:
turn5()
if turns == 3:
turn6()
if turns == 2:
turn7()
if turns == 1:
turn8()
if turns == 0:
turn9()

# Game start
while True:
header()
startmenu()
print("1. Play Hangman \t \t 2. How To Play \t \t 3. Exit")
print("--------------------------------------------------------------------------------")
press = int(input("Select an option: "))
if press == 1:
hangman()
elif press == 2:
print("\nHOW TO PLAY HANGMAN:")
print("1. You will be presented with a word where some letters are missing.")
print("2. You have 10 turns to guess the correct letters and complete the word.")
print("3. Enter a lowercase letter when prompted. Invalid inputs will be rejected.")
print("4. If your guess is correct, the letter will be revealed in the word.")
print("5. If your guess is incorrect, the hangman will start to appear.")
print("6. Win the game by correctly guessing all the letters before running out of turns.")
print("7. Lose the game if you run out of turns without completing the word.")
print("8. The hangman ASCII art will progress with each incorrect guess.")
print("9. Return to the main menu at any time by pressing Ctrl+C or interrupting the program.")
print("10. Have fun playing Hangman!\n")
elif press == 3:
print("Goodbye")
break