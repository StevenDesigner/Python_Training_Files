def is_prime(num):
    # Check if the number is less than 2
    if num < 2:
        return False
    
    # Check for factors from 2 to the square root of the number
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    
    return True

# Test the function
num = int(input("Enter a number to check if it's prime: "))
if is_prime(num):
    print(num, "is a prime number")
else:
    print(num, "is not a prime number")
