#sum
a = int(input('please enter the number '))
counter = 1
sum = 0
while(counter <= a and sum < 300):

 
   if(counter % 5 != 0): 
    sum = sum + counter
    counter = counter + 1
   else:
     counter = counter + 1

print(sum)    

