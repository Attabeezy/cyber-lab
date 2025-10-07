import random

def play_game():
    # Generate the random answer for the new game
    answer = random.randint(1, 10)
    print("I'm thinking of a number between 1 and 10.")
    
    # Loop for guessing
    while True:
        try:
            # PROMPT FOR GUESS *INSIDE* THE LOOP
            # Convert the input string to an integer
            guess = int(input("Enter your guess: "))
            
            if guess == answer:
                print(f"Yes!!! Your prediction is right. The number was {answer}!")
                break # Exit the inner guessing loop
            elif guess < answer:
                print("Too low! Try again.")
            else: # guess > answer
                print("Too high! Try again.")
                
        except ValueError:
            # Handles non-number input (e.g., if the user types "hello")
            print("Invalid input. Please enter a whole number.")

# Main game loop for playing multiple times
while True:
    play_game() # Start a new round of the game
    
    # Ask if the user wants to play again
    state = input("Do you want to try again? [y/n]: ").strip().lower()
    
    if state == "n":
        print("Thanks for playing! Goodbye.")
        break
    elif state != "y":
        print("Invalid choice. Starting a new game anyway!")
