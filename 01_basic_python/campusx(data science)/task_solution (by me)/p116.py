# Write code here
def display(n):
    i=0
    while True:
        try:
            n+=1
            i+=1
            if i==21:
                raise StopIteration
        except StopIteration:
            break
        else:
            print(n, end =' ')
display(100)