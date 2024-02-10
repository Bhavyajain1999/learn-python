n = int(input('enter the value of n till you want to print the series'))

for i in range (0,n+1,1):
    if (i==0):
        print(1, end=" + ")
    else:
       if(i==n):
           print(f"x^{i}/{i}", end="")
       else:   
            print(f"x^{i}/{i}", end=" + ") 
