# Task 1: Create the class

import random

# Step 1: Create a class called Hangman
# class Hangman:
    # Step 2: Inside the class, create an __init__ method to initialise the attributes of the calss
    # def __init__(self,word_list, num_lives=5):
    #     self.word_list=word_list
    #     self.num_lives=num_lives
    #     self.list_of_guesses=[]

        # The word to be guessed, picked randomly from the word_list
        # self.word= random.choice(word_list)

        #  Initialize word_guessed with '_' for each letter
        # self.word_guessed= ['_' for _ in self.word]

        #  Calculate the number of unique letters in the word
        # self.num_letters = len(set(self.word))

# word_list=["apple","banana","orange"]
# hangman_game=Hangman(word_list)
# print(f"Randomly choosen word: {hangman_game.word}") 
# print(f"Word to be guessed: {hangman_game.word_guessed}")  
# print(f"Number of lives: {hangman_game.num_lives}")  
# print(f"Number of unique letters: {hangman_game.num_letters}")
# print(f"List of guesses: {hangman_game.list_of_guesses}")   

# Task 2 : Create methods for running the checks

# class Hangman:
#     def __init__(self,word_list, num_lives=5):
#         self.word_list=word_list
#         self.num_lives=num_lives
#         self.list_of_guesses=[]

        # The word to be guessed, picked randomly from the word_list
        # self.word= random.choice(word_list)

        # Initialize word_guessed with '_' for each letter
        # self.word_guessed= ['_' for _ in self.word]

        # Calculate the number of unique letters in the word
        # self.num_letters = len(set(self.word))

    # def check_guess(self,guess):
        #Step 1: Convert the guessed letter to lower case
        # guess =guess.lower()

        # if guess in self.word:
        #     print(f"Good guess! {guess} is in the word.")
        #     return True
        # else:
        #     return False

    # def ask_for_input(self):
    #    while True:
            # Step 2: Ask the user to guess a letter and assign this to a variable called guess
            # guess= input("Guess a letter:")

            # Step2: Check if the guess is NOT a single alphabetical character 
            # if not guess.isalpha() or len(guess) !=1:
            #     print("Invalid letter. Please, enter a single alphabetical character.")
            
            # Step 2: Check if the guess is already in the list_of_guesses
            # elif guess in self.list_of_guesses:
            #     print("You already tried that letter!")

            # else:
                #  Step 2: Call the check_guess method
                # if self.check_guess(guess):   
                #     break

                # self.list_of_guesses.append(guess)

# word_list=["apple","banana","orange"]
# hangman_game=Hangman(word_list)
# hangman_game.ask_for_input()

# Task 3: Define what happens if the letter is in the word

class Hangman:
    def __init__(self,word_list, num_lives=5):
        self.word_list=word_list
        self.num_lives=num_lives
        self.list_of_guesses=[]

        # The word to be guessed, picked randomly from the word_list
        self.word= random.choice(word_list)

        # Initialize word_guessed with '_' for each letter
        self.word_guessed= ['_' for _ in self.word]

        # Calculate the number of unique letters in the word
        self.num_letters = len(set(self.word))

    def check_guess(self,guess):
        #Step 1: Convert the guessed letter to lower case
        guess =guess.lower()

        # Step 2: Check if the guess is in the word
        if guess in self.word:
            print(f"Good guess! {guess} is in the word.")
            
            # Step 
            for i, letter in enumerate(self.word):
                if letter == guess:
                    self.word_guessed[i] = guess
                    
            self.num_letters -=1
            return True        
        else:
            return False

    def ask_for_input(self):
       while True:
            # Step 2: Ask the user to guess a letter and assign this to a variable called guess
            guess= input("Guess a letter:")

            # Step2: Check if the guess is NOT a single alphabetical character 
            if not guess.isalpha() or len(guess) !=1:
                print("Invalid letter. Please, enter a single alphabetical character.")
            
            # Step 2: Check if the guess is already in the list_of_guesses
            elif guess in self.list_of_guesses:
                print("You already tried that letter!")

            else:
                #  Step 2: Call the check_guess method
                if self.check_guess(guess):   
                    break

                self.list_of_guesses.append(guess)

word_list=["apple","banana","orange"]
hangman_game=Hangman(word_list)
hangman_game.ask_for_input()