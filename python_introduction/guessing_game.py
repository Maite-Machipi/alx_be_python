
import random

print("🎯 Welcome to the Guessing Game!")
print("I'm thinking of a number between 1 and 10...\n")

# Game loop
play_again = "yes"

while play_again.lower() == "yes":
    
    # Generate secret number
    secret_number = random.randint(1, 10)
    guess_count = 0  # Count number of guesses

    while True:
        try:
            guess = int(input("Enter your guess: "))
        except ValueError:
            print("Please enter a valid number!")
            continue

        guess_count += 1  # Increment counter

        # Match-case for comparison
        match guess:
            case _ if guess == secret_number:
                print(f"🎉 Congratulations, you guessed it in {guess_count} tries!\n")
                break
            case _ if guess > secret_number:
                print("⬆️ Oops, your guess is a bit high. Try again!")
            case _ if guess < secret_number:
                print("⬇️ Nope, your guess is a bit low. Give it another shot!")

    # Ask to play again
    play_again = input("Do you want to play again? (yes/no): ")
    print()

print("Thanks for playing! Goodbye 👋")
