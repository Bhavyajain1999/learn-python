# Write code here
import random

class ValueTooLarge(Exception):
    def display(self):
        print("Input value is too large")

class ValueTooSmall(Exception):
    def display(self):
        print("Input value is too small")
    
class GuessError(Exception):
    def display(self):
        print("Guess the number between 1 and 100")

num = random.randint(1, 100)
while 1:
    try:
        guess = int(input("Enter a number:"))

        if guess < 1:
            raise GuessError

        if guess == num:
            print("Great You succeeded...")
            break
        if guess < num:
            raise ValueTooSmall
        if guess > num:
            raise ValueTooLarge
    except ValueTooSmall as s:
        s.display()
    except ValueTooLarge as l:
        l.display()
    except GuessError as g:
        g.display()
