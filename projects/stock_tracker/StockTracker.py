if __name__ == "__main__":
   '''
   WARNING!!!
   The api I use, https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=MSFT&apikey=go-get-your-own-damn-api-stop-using-mine-I-need-to-save-my-call-limit!!!

   ONLY ALLOWS LIKE, 25 'F*CKIN' API CALLS A DAY OR SOME STUPID SH*T LIKE THAT (D*MN A...........E CHEAPOS)!!!!!

   So (ahem)... anyway, it goes to say that, if you go get your own api-key (you don't have to, but if you don't you get ONE MEASLY FREE DEMO. That's it... or something like that), just be careful.

   This is why I hide my api-key inside a dot-env (that and it's good practice).
   '''
   try:
      from functions import all_data, filteredData, link, Chart

      ticker = input("Enter a Ticker Symbol: ")

      filteredResult = (filteredData(all_data, link(ticker))['data'])
      
      closingDates = filteredResult.get('first5Dates');
      closingValues = [float(x)*1 for x in filteredResult.get('first5ClosingValues')]; # The elements (values) inside filteredResult are STRINGED NUMBERS. You must convert them into ACTUAL NUMBERS or the resulting graph will look weeeeeerd... and remember to use your (approximately) 25 Alphvantage API calls wisely!!!!! Thank you for your cooperation.

      print(Chart(closingDates, closingValues, f"{ticker} - CLOSING DATES", f"{ticker} - CLOSING PRICE")) # See the resulting chart drawn by this function inside the comments part of this commit: d1b1f60 (https://github.com/dho1115/PYTHON-/commit/d1b1f603d9650356e7a09b484d45facdc8a9b82d).

   except Exception as EXC:
      print("EXCEPTION: ", EXC);





      