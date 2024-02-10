menu = input("""
Hi! how can I help you.
1. Enter 1 for CM TO FEET
2. Enter 2 for KM TO MILES
3. Enter 3 for USD TO INR
4. Enter 4 for exit
""")

if menu == '1':
  CM = int((input('please enter VALUE IN CM')))
  print('value in feet is ', CM*0.0328084)
elif menu == '2':
  KM = int((input('please enter VALUE IN KM')))
  print('value in miles is ', KM*0.6213712 )
elif menu == '3':
  USD = int((input('please enter VALUE IN USD')))  
  print('value in INR is ', USD*75)
else:
  print('exit')