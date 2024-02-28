# Write code here
from abc import ABC,abstractmethod

class Polygon(ABC):

  @abstractmethod
  def get_data():
    pass

  @abstractmethod
  def area():
    pass

class Rectangle(Polygon):

  def get_data(self,l,b):
    self.l = l
    self.b = b

  def area(self):
    return self.l*self.b

class Triangle(Polygon):

  def get_data(self,b,h):
    self.b = b
    self.h = h

  def area(self):
    return 0.5 * self.b*self.h

rect = Rectangle()
rect.get_data(4,5)
print(rect.area())

tri = Triangle()
tri.get_data(4,5)
tri.area()



