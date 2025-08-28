if __name__ == "__main__":
   try:
      from functions import all_data, filteredData, link

      ticker = input("Enter a Ticker Symbol: ")

      filteredResult = filteredData(all_data, link(ticker));

      print(filteredResult)
   except Exception as EXC:
      print("EXCEPTION: ", EXC)



      