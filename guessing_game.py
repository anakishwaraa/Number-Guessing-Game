import random

def number_guessing_game():
    """
    A simple number guessing game where the player guesses a number between 1 and 100.
    The computer gives hints if the guess is too high or too low.
    """
    # Generate a random number between 1 and 100
    secret_number = random.randint(1, 100)
    attempts = 0
    max_attempts = 10  # Limit the number of attempts for challenge

    print("Welcome to the Number Guessing Game!")
    print("I've picked a number between 1 and 100. Can you guess it?")
    print(f"You have {max_attempts} attempts. Good luck!")

    while attempts < max_attempts:
        try:
            # Get user input
            guess = int(input("Enter your guess: "))
            attempts += 1

            if guess < secret_number:
                print("Too low! Try a higher number.")
            elif guess > secret_number:
                print("Too high! Try a lower number.")
            else:
                print(f"Congratulations! You guessed the number in {attempts} attempts.")
                return  # Exit the function on correct guess

        except ValueError:
            print("Invalid input. Please enter a valid integer.")

    # If they run out of attempts
    print(f"Sorry, you've used all {max_attempts} attempts. The secret number was {secret_number}.")

# Run the game if the script is executed directly
if __name__ == "__main__":
    number_guessing_game()
