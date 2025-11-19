if __name__ == "__main__":
   from restaurantmenu import currentselection;

   class Order:
      def __init__(self, name, price, quantity):
         self.name = name;
         self.price = price;
         self.quantity = quantity;

      def __repr__(self):
         return str(dict(name = self.name, price=self.price, quantity=self.quantity));
      
      def __add__(self, other):
         selfTotal = self.price*self.quantity;
         otherTotal = other.price*other.quantity;
         tip = 0.1*(selfTotal + otherTotal);
         tax = 0.115 * (selfTotal + otherTotal + tip);

         return dict(
            cart=[dict(name=self.name, price=self.price, quantity=self.quantity, total=selfTotal), dict(name=other.name, price=other.price, quantity=other.quantity, total=otherTotal), dict(subtotal=selfTotal + otherTotal, tip=tip, tax=round(tax, 2), total=round(selfTotal + otherTotal + tip + tax, 2))]
         )
   
   order1 = Order(**currentselection[4], quantity=3);
   order2 = Order(**currentselection[3], quantity=5);

   total = order1 + order2

   print(total)