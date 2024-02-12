row = int(input('enter rows : '))

for i in range (1,row+1):
    
    for j in range (0, i):
        print("*" , end=" ")

    print()
for i in range (1,row,1):
    
    for j in range (row-i, 0, -1):
        print("*", end=" ")

    print()  
    