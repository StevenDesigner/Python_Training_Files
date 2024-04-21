# Define the range
start = 1
end = 30  # Adjust the end value as needed

# Loop through the range
for num in range(start, end + 1):
    # Check if the number is divisible by both 3 and 5
    if num % 3 == 0 and num % 5 == 0:
        print("FizzBuzz")
    # Check if the number is divisible by 3
    elif num % 3 == 0:
        print("Fizz")
    # Check if the number is divisible by 5
    elif num % 5 == 0:
        print("Buzz")
    # If none of the above conditions are met, just print the number itself
    else:
        print(num)
