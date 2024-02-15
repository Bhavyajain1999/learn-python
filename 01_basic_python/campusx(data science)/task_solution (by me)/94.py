class Scoop:

  __counter = 0

  def __init__(self,flavor,num_scoops=1):
    self.flavor = flavor
    self.__price = None
    self.num_scoops = num_scoops
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

  def __init__(self,max_scoops=3):
    self.__scoop_list = []
    Bowl.__counter += 1
    self.scoops_added = 0
    self.max_scoops = max_scoops

  def add_scoops(self,*new_scoops):
    for scoop in new_scoops:
      if self.scoops_added + scoop.num_scoops <= self.max_scoops:
        self.__scoop_list.append(scoop)
        self.scoops_added = self.scoops_added + scoop.num_scoops
        print(scoop.flavor,'added!')
      else:
        print('Bowl is full')
        break

  def display(self):
    total = 0
    for scoop in self.__scoop_list:
      print(scoop)
      total = total + scoop.get_price()

    print('total price',total)

  @staticmethod
  def sold():
    return Bowl.__counter
    

############################

choco = Scoop('chocolate', 1)
choco.set_price(100)
print(choco)


berry = Scoop('berry', 2)
berry.set_price(120)
print(berry)

vanilla = Scoop('vanilla') # no of scoop parameter not given, will take default value
vanilla.set_price(150)
print(vanilla)

bowl1 = Bowl() # max_scoop parameter not given, will take default value
bowl1.add_scoops(choco) # Giving one parameter
bowl1.add_scoops(berry, vanilla) # Multiple
bowl1.display()      