#reverse a given integer
a = int(input('please enter the number '))
n = 0
reversed_number = 0
while(a != 0):
    n = a%10
    reversed_number = reversed_number*10 + n
    a = a//10

print(reversed_number)    

