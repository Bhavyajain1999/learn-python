# Taking input for the number of terms in the series
n = int(input("Enter the number of terms in the series: "))

# Initializing variables
series_sum = 0
current_term = 2

# Calculating the sum of the series
for i in range(1, n + 1):
    series_sum += current_term
    print(current_term, end="")
    if i != n:
        print(" + ", end="")
    current_term = current_term * 10 + 2

# Printing the sum
print(" =", series_sum)
