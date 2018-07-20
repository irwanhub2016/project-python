class Car:
  def __init__(self, colour, type, price):
    self.colour = colour
    self.type = type
    self.price = price

  def myfunc(abc):
    print("Ini mobil dengan merk " + abc.type + " dan " + " harga " + abc.price)	

p1 = Car("Red","BMW",9000)
p2 = Car("Blue","Honda", 1)
print(p1.colour)
print(p1.type)
print(p1.price)
print(p2.myfunc())
