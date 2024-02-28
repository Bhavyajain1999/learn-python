# Write code here
class InvalidAge(Exception):
    def display(self):
        print("Sorry!! Age cannot be below 18. Please come after that")
class InvalidName(Exception):
    def display(self):
        print("Please enter a valid name...")
try:
    name = input("Enter your name: ")
    if len(name) == 0 or len(name.split()) < 2:
        raise InvalidName

    age = int(input("Enter your age: "))
    if age < 18:
        raise InvalidAge
except InvalidName as i:
    i.display()
except InvalidAge as a:
    a.display()
else:
    print("Your vote is accepted successfully")
finally:
    print("Thank You")