class Scoop:

  __counter = 0

  def __init__(self,flavor):
    self.flavor = flavor
    self.__price = None
    Scoop.__counter += 1


  def get_price(self):
    return self.__price

  def set_price(self,price):
    self.__price = price

  def __str__(self):
    return "Flavor - {} and Price - {}".format(self.flavor,self.__price)

  @staticmethod
  def sold():
    return Scoop.__counter


class Bowl:

  __counter = 0

  def __init__(self):
    self.__scoop_list = []
    Bowl.__counter += 1

  def add_scoops(self,*new_scoops):
    for scoop in new_scoops:
      self.__scoop_list.append(scoop)

  def display(self):
    total = 0
    for scoop in self.__scoop_list:
      print(scoop)
      total = total + scoop.get_price()

    print('total price',total)

  @staticmethod
  def sold():
    return Bowl.__counter
  


choco = Scoop('chocolate')
choco.set_price(100)

berry = Scoop('berry')
berry.set_price(120)

vanilla = Scoop('vanilla')
vanilla.set_price(150)

bowl = Bowl()

bowl.add_scoops(choco) # Giving one parameter
bowl.add_scoops(berry, vanilla) # Multiple
# add_scoops should handle both scenerios

bowl.display()

print(Scoop.sold())
print(Bowl.sold())