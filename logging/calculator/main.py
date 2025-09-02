if __name__ == "__main__":
   def main():
      import logging;
      logging.basicConfig(level=logging.ERROR, filename='ErrorLog.log')
      try:
         import functions;
         operation = input("What operation do you want to perform? ");
         numbers = input("Enter some numbers separated by a comma: ").split(",");

         return functions.__dict__[operation](numbers)
      except Exception as EXC:
         logging.error(msg="Error in main program!!!", exc_info=EXC);
         return f"Main function exception!!! - {EXC}."
   
   main();