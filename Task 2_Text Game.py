import random

def number_guessing_game():
    # Generate a random number between 1 and 100
    sec = random.randint(1, 100)
    
    # Set the number of attempts
    max_attempts = 7
    attempts = 0
    
    print("Welcome to the Number Guessing Game!")
    print("I've selected a random number between 1 and 100.")
    print(f"You have {max_attempts} attempts to guess it.")
    
    while attempts < max_attempts:
        try:
            # Ask the player for their guess
            guess = int(input("Enter your guess: "))
            
            if guess < 1 or guess > 100:
                print("Please enter a number between 1 and 100.")
                continue
            
            attempts += 1
            
            if guess < sec:
                print("Too low! Try again.")
            elif guess > sec:
                print("Too high! Try again.")
            else:
                print(f"Congratulations! You guessed the number {sec} in {attempts} attempts.")
                break
                
        except ValueError:
            print("Invalid input. Please enter a valid number.")
    
    if attempts >= max_attempts:
        print(f"Sorry, you've run out of attempts. The secret number was {secret_number}.")

if __name__ == "__main__":
    number_guessing_game()
