class Food:
   categories = ['meat', 'vegetable', 'fruit', 'beverage', 'other']
   def __init__(self, name, category, price):
      try:
         if category not in Food.categories: raise Exception(f"Sorry, but your choice of {name} is NOT in the categories of {Food.categories}")
         self.name = name;
         self.category = category;
         self.price = price;
      except Exception as exc:
         print(exc)

   def __repr__(self):
      return f"<New Food Item: {self.name} {self.category} {self.price} >"

class Store():
   def __init__(self, *foods):
      nonFood = list(filter(lambda x: not isinstance(x, Food), foods)); #filters out values that are not type Food.
      try:
         if len(nonFood):
            self.inventory = []
            raise TypeError(f"{nonFood} are not instances of Food!!! They are all {[type(x) for x in nonFood]}.") #Throws error if any item is not type Food.
         else:
            self.foods = foods;
            self.inventory = [*self.foods];
      except TypeError as TE:
         print(TE)
   
   def __repr__(self):
      return f"<Store inventory {self.inventory}>"

   def addItem(self, foods:list): # Method to add new food.
      try:
         for i in foods:
            if not isinstance(i, Food):
               raise Exception(f"{i} is {type(i)} and NOT type Food.")
            else:
               self.inventory.append(i)
         return self.inventory;
      except Exception as EXC:
         print(f"AN ERROR OCCURRED => {EXC}!!!!!")
         return f"EXCEPTION WARNING!!! {Exception}."
   
   def __len__(self): # Without this, I cannot do len(Store Instance). len calls this function.
      return len(self.inventory) # It does not make sense, but I can add 23 to the return and len(Store Instance) would be the result of len(self.inventory) + 23.

MyStore = Store(Food('Bologna', 'meat', 1.99), Food('sardines', 'other', 7.99), Food('lemonade', 'beverage', 5.99), Food('avocado', 'vegetable', 1.99), Food('water', 'beverage', 0.99));

MyStore.addItem([Food('bacon', 'meat', 7.45), Food('pineapples', 'fruit', 5.99), Food('rasberries', 'fruit', 3.99)])

print(len(MyStore))





      


      




      
