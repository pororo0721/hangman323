# Task 1: Create the class

import random

# Step 1: Create a class called Hangman
class Hangman:
    # Step 2: Inside the class, create an __init__ method to initialise the attributes of the calss
    def __init__(self,word_list, num_lives=5):
        self.word_list=word_list
        self.num_lives=num_lives
        self.list_of_guesses=[]

        # The word to be guessed, picked randomly from the word_list
        self.word= random.choice(word_list)

        #  Initialize word_guessed with '_' for each letter
        self.word_guessed= ['_' for _ in self.word]

        #  Calculate the number of unique letters in the word
        self.num_letters = len(set(self.word))

word_list=["apple","banana","orange"]
hangman_game=Hangman(word_list)
print(f"Randomly choosen word: {hangman_game.word}") 
print(f"Word to be guessed: {hangman_game.word_guessed}")  
print(f"Number of lives: {hangman_game.num_lives}")  
print(f"Number of unique letters: {hangman_game.num_letters}")
print(f"List of guesses: {hangman_game.list_of_guesses}")   