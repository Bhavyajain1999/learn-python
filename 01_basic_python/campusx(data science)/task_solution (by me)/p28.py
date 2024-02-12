s1 = input('enter first string')
s2 = input('enter second string')

middle_index = len(s1) // 2

# Insert the second string at the middle index of the first string
result_string = s1[:middle_index] + s2 + s1[middle_index:]

# Print the result
print(result_string)



