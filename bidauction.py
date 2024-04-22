import os
def get_highest_bidder(bids):
    highest_bid = 0
    highest_bidder = None
    
    for bidder, bid_amount in bids.items():
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            highest_bidder = bidder
    
    return highest_bidder, highest_bid

# Initialize an empty dictionary to store bids
bids = {}

# Prompt users to enter their bids
while True:
    os.system('cls')
    bidder_name = input("Enter your name (or type 'done' to finish): ")
    if bidder_name.lower() == 'done':
        break
    
    bid_amount = float(input("Enter your bid amount: "))
    
    bids[bidder_name] = bid_amount

# Find the highest bidder
winner, highest_bid = get_highest_bidder(bids)

# Display the winner and the winning bid amount
print("The winner is:", winner)
print("The winning bid amount is:", highest_bid)
