from hotelsdatabase import HotelsDatabase, hotelsByCity;

if __name__ == "__main__":
   def main(db):
      from termcolor import colored;
      from colorama import init;
      init()
      selectCity = input(f"Select a city from these list of choices, {list(db.keys())} to return the available hotels. ")
      try:
         if db.get(selectCity):
            color = "red"
            for i in list(db.get(selectCity).values()):
               color = "green" if color == "red" else "red";
               print(colored(f"{i}", color=color, attrs=['bold']));
            return;
         raise ValueError(f"Sorry, but your choice of {selectCity} is not in the list of {list(db.keys())}.")
      except ValueError as VE:
         return f"{VE}.";
      except Exception as EXC:
         return f"Another exception occurred... {EXC}."
   
   print(main(hotelsByCity(HotelsDatabase)));


