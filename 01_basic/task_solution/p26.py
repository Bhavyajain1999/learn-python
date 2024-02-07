# Take input from the user
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

# Finding HCF
a = num1
b = num2
while a != b:
    if a > b:
        a -= b
    else:
        b -= a
hcf = a

# Finding LCM
lcm = (num1 * num2) // hcf

# Print the results
print("HCF of", num1, "and", num2, "is:", hcf)
print("LCM of", num1, "and", num2, "is:", lcm)
