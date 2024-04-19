import random

print("Welcome to the Coin Toss Game!")
choice = input("Choose heads or tails: ").capitalize()

# Check if the user's choice is valid
if choice != "Heads" and choice != "Tails":
    print("Invalid choice! Please choose heads or tails.")
else:
    # Generate a random number (0 or 1) representing heads or tails
    result = random.randint(0, 1)
    
    # Convert the result to heads or tails
    if result == 0:
        outcome = "Heads"
    else:
        outcome = "Tails"
    
    # Display the coin toss result
    print("Coin toss result:", outcome)
    
    # Check if the user's choice matches the coin toss result
    if outcome == choice:
        print("Congratulations! You win!")
    else:
        print("Sorry, you lose. Better luck next time!")
