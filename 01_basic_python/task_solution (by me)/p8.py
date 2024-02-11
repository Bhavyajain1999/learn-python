#sum
a = int(input('please enter the number '))
counter = 1
sum = 0
while(counter <= a and sum < 300):

 
   if(counter % 5 == 0): 
    counter = counter + 1
   else:
      sum = sum + counter
      if sum>300:
        sum = sum - counter
        break
      counter = counter + 1

    


print(sum)    

