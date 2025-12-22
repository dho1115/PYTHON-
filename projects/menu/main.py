if __name__ == "__main__":
   from restaurantmenu import currentselection;

   class Order:
      items_ordered = [];

      def __init__(self, quantity, price, taxAdded=False) -> None:
         self.quantity = quantity;
         self.taxAdded = taxAdded
         self.price = price;
         self.total = price;
      
      def __add__(self, other_value):
         tax_item_1 = 0.1 *(self.quantity * self.price); # tax
         tax_item_2 = 0.1 *(other_value.quantity * other_value.price); # tax

         item_1_total = round((self.quantity * self.total) + tax_item_1, 3) if self.taxAdded == False else round((self.quantity * self.total), 3); # I do not want to add tax again when I do addition with multiple numbers.

         item_2_total = round((other_value.quantity * other_value.price) + tax_item_2, 3) if other_value.taxAdded == False else round((other_value.quantity + other_value.price), 3);

         self.total+= (item_1_total + item_2_total); # grand total with tax

         print(dict(item_1_total=item_1_total, item_2_total=item_2_total, totalSoFar = item_1_total + item_2_total))

         return Order(1, (item_1_total + item_2_total), True) # if you return a number instead of type Order, then you cannot to addition with multiple items.

   food1 = Order(3, currentselection[0]["price"]);
   food2 = Order(5, currentselection[1]["price"]);
   food3 = Order(4, currentselection[5]["price"]);

   grand_total = food1 + food2 + food3 + food1 + food2; # I cannot multiple more than 2 food items if I returned, say, an integer instead of Order (see __add__ in Order method).
   
   print(grand_total)
   print(grand_total.total)