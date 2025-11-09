class ProductDetails:
   def __init__(self, product, price, quantity):
      self.product = product;
      self._price = price;
      self._quantity = quantity;

   @property
   def potential_gross_profits(self):
      return self.price * self.quantity;
   
   @property
   def price(self):
      '''
      GETTER object that returns the price when the user does ProductDetails.price.
      '''
      if not isinstance(self._price, float): raise ValueError(f"Wrong value!!! {self._price} should be a float, but instead, {self._price} is of type {type(self._price).__name__}!!!") #validation

      self._price = max(self._price, 0) #validation to insure price is not negative.

      return self._price;
   
   @price.setter #This is the SETTER that sets the price.
   def price(self, newprice):
      '''
      SETTER object to SET the price: ProductDetails.price = new price.
      
      PARAMETERS:
      self: The class object itself.
      newprice: The new price as a type FLOAT.
      '''
      self._price = newprice;
      return newprice
   
   @property
   def quantity(self):
      '''
      GETTER for self._quantity.
      '''
      self._quantity = max(0, self._quantity); #validation to ensure quantity > 0;
      return self._quantity;
   
   @quantity.setter
   def quantity(self, newquantity):
      newquantity = max(0, newquantity);
      self._quantity = newquantity;
      return self._quantity
   
   def __repr__(self):
      return f"<class {ProductDetails} >"

myproddetails = ProductDetails("widget", 15.93, 11)
myproddetails.price = 19.75
print(myproddetails)
print(myproddetails.quantity)
myproddetails.quantity = 105;
print(myproddetails.potential_gross_profits)