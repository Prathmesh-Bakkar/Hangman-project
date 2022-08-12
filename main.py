import random
print("Welcome to HANGMAN!\n")
print("How this game works:\n\n1. You will be given a name of one of your friends with first and last letters.\n2. You have to guess the name by filling out one letter at a time in the blank spaces.\n3. You have 6 lives, for each wrong guess, one life will be reduced.\n")
print('''
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/  
''')



stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

word_list = ["Prathmesh", "Adesh", "Swapnil", "Sneha", "Shruti", "Vipul", "Aniket"]
chosen_word = random.choice(word_list).lower()

display = []
display = ["_"]*len(chosen_word)   
display[0] = chosen_word[0]
display[-1] = chosen_word[-1]
print(f"Here's the name of one of your friend with first and last letters {display[0]} and {display[-1]}\n")
print(display)

n = 1
lives = 6
guesses = []

while display.count("_") > 0 and lives > 0:

    guess = input("\nGuess a letter: ").lower()
    

    i = 0
    for letters in chosen_word:
        if guess == letters:
            display[i] = guess
        i += 1
    
    if guess in guesses:
        print(f"You already guessed {guess}, try another letter.")
    elif guess not in chosen_word:
        print(f"Wrong guess. lives remaining : {lives-1}. Guess again!\n")
        print(stages[n])
        n += 1
        lives -= 1
    guesses += guess
    print(display)
    print("\n")

if display.count("_") == 0:
    print("You win!")
else:
    print("You are out of lives.You lose!")





    


