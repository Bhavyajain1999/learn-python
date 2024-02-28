class rectangle:
    def  __init__(self,l,b):
        self.length = l
        self.breadth = b

    @classmethod
    def property(cls,len,bre):
        return cls(len,bre)
    
    
    def area(self):
        return self.length*self.breadth
    
    def is_square(self):
        return True if self.length == self.breadth else False
    


r = rectangle.property(4,5)
print(r.area())
print(r.is_square())