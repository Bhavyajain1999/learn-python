# Write code here

class Vehicle:

  def __init__(self,type,capacity):
    self.type = type
    self.capacity = capacity

  def fare(self):
    return 100*self.capacity

class Bus(Vehicle):

  def fare(self):
    base_fare = super().fare()
    bus_fare = base_fare + 0.1*base_fare
    return bus_fare

bus = Bus('school bus',50)
print(bus.fare())