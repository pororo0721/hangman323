# Task 1: Define the list of possible words

# favorite_fruits=['Apple','Banana','Orange','Mango','Strawberry']

# word_list= favorite_fruits

# print(word_list)

# Task 2: Choose a random word from the list

# import random


# favorite_fruits=['Apple','Banana','Orange','Mango','Strawberry']

# word_list= favorite_fruits

# random_word = random.choice(word_list)

# word = random_word
# print(word)

# Task 3: Ask the user for an input

geuss = input("Enter a single letters:")

# Task 4: Check that the input is a single character

if len(geuss) == 1 and geuass.isalpha():
    print("Good guess!")

else:
    print("Opps! That is not a valid input.")
