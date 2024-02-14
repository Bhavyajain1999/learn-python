class rectangle:
     def __init__(self,a,b) :
      self.a = a
      self.b = b
     
     def perimeter(self) :
      return  2*(self.a + self.b)
     
     def area(self) :
        return self.a * self.b
     
     def display(self):
        print('length', self.a)
        print('breadth',self.b)
        print('perimeter',self.perimeter())
        print('area', self.area())
   

obj = rectangle(4,5)
obj.display()

