

# Input a number from the user
number = int(input("Enter a number to check if it's prime: "))

# Check if the number is less than or equal to 1
if number <= 1:
    is_prime = False
# Check if the number is 2
elif number == 2:
    is_prime = True
# Check if the number is even
elif number % 2 == 0:
    is_prime = False
else:
    is_prime = True
    # Iterate from 3 to the square root of the number, skipping even numbers
    for i in range(3, number , 2):
        if number % i == 0:
            is_prime = False
            is_prime = False

# Print the result
if is_prime:
    print(f"{number} is a prime number.")
else:
    print(f"{number} is not a prime number.")
