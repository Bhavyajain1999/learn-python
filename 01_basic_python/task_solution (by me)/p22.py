# Taking input for x and the number of terms (n)
x = float(input("Enter the value of x: "))


# Initialize the result
result = 0

# Computing the expression up to the nth term
for i in range(1, 8):
    result += 1/2 * ((x-1)/x) ** (i)
    print(result)



# Printing the result
print("Result:", result)
