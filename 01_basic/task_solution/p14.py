i = int(input('please enter the range'))

for num in range(1, i,1):
    temp = num
    armstrong = 0
    while(temp != 0):
        digit = temp%10
        armstrong = digit ** 3 + armstrong
        temp = temp //10

    if(num == armstrong):
        print(num, end=" ")
print()        