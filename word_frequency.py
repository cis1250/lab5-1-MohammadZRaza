#!/usr/bin/env python3
"""
Word Frequency Program
----------------------
This program prompts the user to enter a valid sentence and then calculates
the frequency of each word in that sentence. It demonstrates modular programming
by dividing the logic into multiple reusable functions.
"""

import re  # Import regular expressions module for sentence validation

# ---------------------------------------------------------------
# Function: is_sentence()
# Purpose:  Check whether the input text qualifies as a valid sentence
# ---------------------------------------------------------------
def is_sentence(text):
    """
    Check if the provided text qualifies as a valid sentence.
    A valid sentence must:
    - Start with a capital letter
    - End with one of the following punctuation marks: '.', '!', or '?'
    - Contain at least one word (non-whitespace characters)
    """
    # Check that text is a non-empty string
    if not isinstance(text, str) or not text.strip():
        return False

    # Check that the first character is uppercase
    if not text[0].isupper():
        return False

    # Ensure the sentence ends with a period, exclamation mark, or question mark
    if not re.search(r'[.!?]$', text):
        return False

    # Check that the text includes at least one word
    if not re.search(r'\w+', text):
        return False

    return True  # All conditions met → valid sentence


# ---------------------------------------------------------------
# Function: get_sentence()
# Purpose:  Prompt the user for a sentence and validate it
# ---------------------------------------------------------------
def get_sentence():
    """
    Prompt the user to enter a valid sentence and ensure it meets
    the sentence criteria using is_sentence().
    Returns:
        str: A valid sentence entered by the user.
    """
    # Ask the user for input
    user_sentence = input("Enter a sentence: ")

    # Continue asking until the input meets the sentence criteria
    while not is_sentence(user_sentence):
        print("This does not meet the criteria for a sentence.")
        user_sentence = input("Enter a sentence: ")

    # Return the valid sentence once obtained
    return user_sentence


# ---------------------------------------------------------------
# Function: calculate_frequencies()
# Purpose:  Count how many times each word appears in the sentence
# ---------------------------------------------------------------
def calculate_frequencies(sentence):
    """
    Calculate the frequency of each unique word in the provided sentence.
    Steps:
    1. Split the sentence into individual words.
    2. Clean punctuation and convert words to lowercase.
    3. Store unique words and their corresponding counts.
    
    Args:
        sentence (str): The validated sentence from the user.
    Returns:
        tuple: Two lists - (words, frequencies)
    """
    # Split sentence into words based on spaces
    sentence_list = sentence.split()

    # Initialize empty lists to store unique words and their frequencies
    words = []
    frequencies = []

    # Loop through each word in the sentence
    for w in sentence_list:
        # Remove punctuation and convert to lowercase for consistency
        w = w.strip(".,!?").lower()

        # If the word already exists in the list, increment its count
        if w in words:
            index = words.index(w)
            frequencies[index] += 1
        else:
            # If it's a new word, add it to the list with a count of 1
            words.append(w)
            frequencies.append(1)

    # Return both lists for further processing
    return words, frequencies


# ---------------------------------------------------------------
# Function: print_frequencies()
# Purpose:  Display each word along with its frequency count
# ---------------------------------------------------------------
def print_frequencies(words, frequencies):
    """
    Print the list of words and their corresponding frequencies
    in a clean and readable format.
    
    Args:
        words (list): List of unique words.
        frequencies (list): List of their corresponding frequency counts.
    """
    print("\nWord Frequencies:")
    print("-----------------")
    # Loop through each word-frequency pair and print them
    for i in range(len(words)):
        print(f"{words[i]}: {frequencies[i]}")


# ---------------------------------------------------------------
# Function: main()
# Purpose:  Coordinate the program's overall flow
# ---------------------------------------------------------------
def main():
    """
    Main function that coordinates the overall workflow of the program:
    1. Get a valid sentence from the user.
    2. Calculate word frequencies.
    3. Display the results.
    """
    # Step 1: Prompt and validate user input
    sentence = get_sentence()

    # Step 2: Process the sentence to calculate word frequencies
    words, frequencies = calculate_frequencies(sentence)

    # Step 3: Print the results in a clear format
    print_frequencies(words, frequencies)


# ---------------------------------------------------------------
# Entry point of the program
# ---------------------------------------------------------------
if __name__ == "__main__":
    # Run the main function only if the script is executed directly
    main()


