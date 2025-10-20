def get_user_input():
    """
    Prompt the user to enter a positive integer and validate the input.
    Returns:
        int: The number of terms for the Fibonacci sequence.
    """
    while True:
        # Ask the user to input the number of Fibonacci terms they want
        user_input = input("Enter the number of terms for the Fibonacci sequence: ")

        # Check if the input is a positive integer
        if user_input.isdigit() and int(user_input) > 0:
            return int(user_input)  # Valid input: convert to integer and return
        else:
            # Display an error message and prompt again for invalid input
            print("Error: Please enter a positive integer.\n")


def generate_fibonacci(n):
    """
    Generate the Fibonacci sequence up to n terms.

    Args:
        n (int): Number of terms to generate.

    Returns:
        list: A list containing the Fibonacci sequence.
    """
    # Initialize an empty list to store the sequence
    sequence = []
    # Start with the first two Fibonacci numbers: 0 and 1
    a, b = 0, 1

    # Generate the sequence using a for loop
    for _ in range(n):
        sequence.append(a)  # Add the current number to the sequence
        a, b = b, a + b     # Update the values for the next iteration

    return sequence  # Return the complete sequence as a list


def print_fibonacci(sequence):
    """
    Print the Fibonacci sequence in a readable format.

    Args:
        sequence (list): The Fibonacci sequence to print.
    """
    # Print a header to indicate the start of the sequence output
    print("\nFibonacci sequence:")

    # Convert all numbers to strings and join them with commas for neat display
    print(", ".join(str(num) for num in sequence))

    # Add a blank line for better readability before the next loop iteration
    print()


def main():
    """
    Main function that controls the overall program flow.
    """
    while True:
        # Step 1: Get the number of Fibonacci terms from the user
        num_terms = get_user_input()

        # Step 2: Generate the Fibonacci sequence using the user's input
        fib_sequence = generate_fibonacci(num_terms)

        # Step 3: Display the generated Fibonacci sequence
        print_fibonacci(fib_sequence)

        # Step 4: Ask the user if they want to generate another sequence
        again = input("Do you want to generate another sequence? (yes/no): ").strip().lower()

        # If the user types anything other than "yes", end the program
        if again != "yes":
            print("Goodbye!")  # Friendly exit message
            break


# Run the program only if this file is executed directly
# This prevents the main function from running if the file is imported elsewhere
if __name__ == "__main__":
    main()
