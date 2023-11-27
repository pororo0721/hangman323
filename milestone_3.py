# Task 1: Iteratively check if the input is a valid guess

# Step 1: Create a while loop and set the condition to True. 
# Setting the condition to True ensures that the code runs continuously.
# In the body of the loop, write the code required for the following steps.

while True:
    # Step 2: Ask the user to guess a letter and assign this to a variable called guess.
    guess = input("Enter a single letters:")

    # Step 3: Check if the guess is a single alphabetical character
    if guess.isalpha() and len(guess) == 1:
        # Step 4: If the guess passes the checks, break out of the loop
        break
    else:
        # Step 5: If the guess does not pass the checks, print an error message.
        print("Invalid letter. Please, enter a single alphabetical character.")

print("You guessed:", guess)        