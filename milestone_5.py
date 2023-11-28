# Task 1: Code the logic of the game
import random

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
    
        guess =guess.lower()

        
        if guess in self.word:
            print(f"Good guess! {guess} is in the word.")
            
            # Replace the corresponding "_" in the word_guessed with the guess
            for i, letter in enumerate(self.word):
                if letter == guess:
                    self.word_guessed[i] = guess
                    self.num_letters -=1
            return True        
        else:
            # Reduce 'num_lives' by1
            self.num_lives -=1
            # Print a message saying "Sorry, {letter} is not in the word"
            print(f"Sorry, {guess} is not in the word")
            # Print another message saying "You have {num_lives} lives left"
            print(f"You have {self.num_lives} lives left.")
            return False

    def ask_for_input(self):
       while True:
            guess= input("Guess a letter:")

            if not guess.isalpha() or len(guess) !=1:
                print("Invalid letter. Please, enter a single alphabetical character.")
            
            elif guess in self.list_of_guesses:
                print("You already tried that letter!")

            else:
                if self.check_guess(guess):   
                    break

                self.list_of_guesses.append(guess)

# Step 1: Create a function called play_game that takes word_list as a parameter
def play_game(word_list):
    num_lives=5
    game=Hangman(word_list,num_lives)

    while True:
        if game.num_lives ==0:
            print("You lost!")
            break
        elif game.num_letters>0:
            game.ask_for_input()
        else:
            print("Congratulations. You won the game!")
            break



if __name__ == "__main__":
    word_list=["apple","banana","orange"]
    play_game(word_list)