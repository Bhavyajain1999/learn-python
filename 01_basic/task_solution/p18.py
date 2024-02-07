i = 0

for i in range (1,6,1):
    j = i
    for j in range (j, 0, -1):
        print("*" , end=" ")

    print()
for i in range (1,6,1):
    j = 6-i
    for j in range (j, 0, -1):
        print("*", end=" ")

    print()  
    