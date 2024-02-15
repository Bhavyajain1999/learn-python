class car:

    __counter = 0 # class ka variable static variable

    def __init__(self):
        car.__counter +=1

    def get_counter():
        return car.__counter



bmw = car()
tata = car()
nano = car()
hyundarri = car()

print(car.get_counter())