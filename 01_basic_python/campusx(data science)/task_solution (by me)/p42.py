num1 = [23,45,67,78,89,34,67]
num2 = [34,89,55,56,39,67,67]
result = []

for i in num1:
    if i in num2:
        if i not in result:
            result.append(i)
result.sort()
print(result)