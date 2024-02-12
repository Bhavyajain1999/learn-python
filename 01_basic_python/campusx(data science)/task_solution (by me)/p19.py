rows = 3

# Outer loop for number of rows
for i in range(0, rows):
    # Inner loop for spaces
    for j in range(0, rows - i - 1):
        print(" ", end="")
    
    # Inner loop for printing stars
    for k in range(0, 2*i + 1):
        print("*", end="")
    
    # Move to the next line after each row is printed
    print()


#     rows = 6
# for i in range(1,rows+1):
#   print(' '*rows,end='')
#   print('* '*i)
#   rows = rows - 1
