# Take input from the user
total_amount = float(input("Enter the total amount of the bill: "))
tip_percentage = float(input("Enter the percentage of tip (e.g., 15 for 15%): "))
num_people = int(input("Enter the number of people: "))

# Calculate tip amount
tip_amount = (tip_percentage / 100) * total_amount

# Calculate total bill including tip
total_bill = total_amount + tip_amount

# Calculate each person's share
each_person_share = total_bill / num_people

# Display the result
print("Total bill including tip:", total_bill)
print("Each person's share:", each_person_share)
