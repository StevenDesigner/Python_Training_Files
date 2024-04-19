# Take input for names
name1 = input("Enter the first name: ").lower()
name2 = input("Enter the second name: ").lower()

# Combine the names
combined_name = name1 + name2

# Count occurrences of letters representing "true"
count_true = combined_name.count("t") + combined_name.count("r") + combined_name.count("u") + combined_name.count("e")

# Count occurrences of letters representing "love"
count_love = combined_name.count("l") + combined_name.count("o") + combined_name.count("v") + combined_name.count("e")

# Calculate love percentage
love_percentage = int(str(count_true) + str(count_love))

# Display the result
print(f"The love percentage between {name1.capitalize()} and {name2.capitalize()} is {love_percentage}%.")

# Compare the love percentage and print message accordingly
if love_percentage > 80:
    print("Best pair!")
elif love_percentage > 60:
    print("You fight often.")
else:
    print("You're like coke and mentos.")
