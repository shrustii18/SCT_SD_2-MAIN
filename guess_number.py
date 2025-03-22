import random
def guess_the_number():
    """Generates a random number and challenges the user to guess it."""
    # Set the range for the random number
    lower_bound = 1
    upper_bound = 100  # You can change this to a different range
    secret_number = random.randint(lower_bound, upper_bound)

    # Set the number of attempts the user has
    max_attempts = 7 # You can change this
    attempts_left = max_attempts

    print(f"I'm thinking of a number between {lower_bound} and {upper_bound}.")

    while attempts_left > 0:
        try:
            guess = int(input(f"You have {attempts_left} attempts remaining.  Take a guess: "))
        except ValueError:
            print("Invalid input. Please enter a whole number.")
            continue  # Go back to the beginning of the loop

        if guess < secret_number:
            print("Too low!")
            attempts_left -= 1
        elif guess > secret_number:
            print("Too high!")
            attempts_left -= 1
        else:
            print(f"Congratulations! You guessed the number {secret_number} in {max_attempts - attempts_left + 1} attempts.")
            return  # Exit the function if the user guesses correctly

    # If the loop finishes without a correct guess
    print(f"You ran out of attempts. The number I was thinking of was {secret_number}.")

# Start the game
guess_the_number()