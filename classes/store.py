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




      
