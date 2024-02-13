# You are given a list of integers. You are asked to make a list by running through elements of the list by adding all elements greater and itself.


L = [2,4,6,10,1]
result = []

for i in L:
    sum = 0
    for j in L:
        if i <= j:
            sum = sum + j
    result.append(sum)    

print(result)