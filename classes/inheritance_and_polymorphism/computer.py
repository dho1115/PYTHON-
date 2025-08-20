class Computer:
   def __init__(self, ram=None, screensize=None, batteryLife=None, price=None):
      self.ram = 5 if not ram else ram;
      self.screensize = 15.6 if not screensize else screensize;
      self.batteryLife = "11 hours" if not batteryLife else batteryLife;
      self.price = 101.00 if not price else price

   def screenimage(self):
      return "Opening screenshot of our most BASIC computer!!!\n*** YOU CANNOT EDIT THIS***\n\t\t*** SORRY!!! ***.";

   def __repr__(self): #polymorphism in action.
      return f"<__main__.Computer object with ram of {self.ram} screensize is {self.screensize} & battery life of {self.batteryLife}>"

class CustomComputer(Computer): #This is called inheritance
   '''
   This newly designed Custom Computer INHERITS from the above Computer (basic computer).
   
   Both have a sreenimage, but NOTICE how, when you call screen image (see below)... different message shows up. This is POLYMORPHISM: The same function/method, inside of different classes yields different results.

   When we overrive __repr__, which is a common method inside of Python classes, we are using polymorphism.
   '''
   def __init__(self, ram, screensize, batteryLife, price, customMessage="WELCOME!!!"):
      super().__init__(ram, screensize, batteryLife, price)
      self.customMessage = customMessage;

   def screenimage(self):
      return self.customMessage

BasicComputer = Computer();
MyCustomComputer = CustomComputer(35, 25, "395 hours", 703.99, "HERE IS MY CUSTOM, AWESOME MESSAGE (THANKS TO POLYMORPHISM!!!)");

print("Basic Computer Screen Image:", BasicComputer.screenimage());
print("Custom Comuter Screen Image:", MyCustomComputer.screenimage());
