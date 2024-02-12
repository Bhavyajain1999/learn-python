# Take input from the user
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

# Finding HCF
a = num1
b = num2
# method 1 # while a != b:
#     if a > b:
#         a -= b
#     else:
#         b -= a
# hcf = a

# method2
while b:
        # Swap a and b, and set a to the remainder of a divided by b
        a, b = b, a % b
    # When b becomes zero, return a which is the HCF
hcf = a

# Finding LCM
lcm = (num1 * num2) // hcf

# Print the results
print("HCF of", num1, "and", num2, "is:", hcf)
print("LCM of", num1, "and", num2, "is:", lcm)

# # Code here
# x = int(input('enter 1st number'))
# y = int(input('enter 2nd number'))

# if x>y:
#   greater = x
# else:
#   greater = y

# while True:
#   if (greater % x == 0) and (greater % y == 0):
#     lcm = greater
#     break
  
#   greater = greater + 1

# print(lcm)


# # Code here
# x = int(input('enter 1st number'))
# y = int(input('enter 2nd number'))

# if x<y:
#   smaller = x
# else:
#   smaller = y

# for i in range(1,smaller+1):
#   if (x % i == 0) and (y % i == 0):
#     hcf = i

# print(hcf)



