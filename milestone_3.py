# Task 1: Iteratively check if the input is a valid guess

# Step 1: Create a while loop and set the condition to True. 
# Setting the condition to True ensures that the code runs continuously.
# In the body of the loop, write the code required for the following steps.

# while True:
    # Step 2: Ask the user to guess a letter and assign this to a variable called guess.
    # guess = input("Enter a single letters:")

    # Step 3: Check if the guess is a single alphabetical character
    # if guess.isalpha() and len(guess) == 1:
        # Step 4: If the guess passes the checks, break out of the loop
        # break
    # else:
        # Step 5: If the guess does not pass the checks, print an error message.
#         print("Invalid letter. Please, enter a single alphabetical character.")

# print("You guessed:", guess)        

# Task 2: Check whether the guess is in the word
# Check whether the letter guessed by the user is in the secret word that was randomly chosen by the computer.
# For example, if the user guesses the letter "a" and the secret word is "apple", 
# then your code should check if "a" is in "apple".

# secre_word="apple"

# while True:
#     guess = input("Enter a single letters:")

    # Step 1: Check if the guess is in the word
    # if guess in secre_word:
        # Step 2: if the guess is in the word, print a success message
    #     print(f"Good guess! {guess} is in the word.")
    #     break
    # else:
        # Step 3: If the guess is not in the word, print an error message
#         print(f"Sorry, {guess} is not in the word. Try again.")

# print("You guessed:", guess)   

#Task 3: Create functions to run the checks
# Create 2 functions, check_guess and ask_for_input functions which contain 
# the code for those two things.abs
# The check_guess function will take the guessed letter as an argument and
# check if the letter is in the word.

secre_word= "apple"

# Step 1: Define a function called check_guess. pass in the guess as a parameter for the function.
def check_guess(guess):
    # Step 2: Convert the guess into lower case.abs
    guess = guess.lower()

    # Step 3: Check if the guess is in the word
    if guess in secre_word:
        print(f"Good guess! {guess} is in the word.")
        return True
    else:
        print(f"Sorry, {guess} is not in the word. Try again.")
        return False    

# Step 1: Define a function called ask_for_input.
def ask_for_input():
    while True:
        # Step 2: Move the code for getting a valid letter guess into this function.
      guess= input("Guess a letter: ")

    
      if guess.isalpha() and len(guess) ==1:
        # Step 3: Call the check_guess function to check if the guess is in the word. 
            if check_guess(guess):
                break
      else:
        print("Invalid letter. Please, enter a single alphabetical character.")

# Step 4: Call the ask_for_input function to test your code
ask_for_input() 