if __name__ == "__main__":
   '''
   WARNING!!!
   The api I use, https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=MSFT&apikey=go-get-your-own-damn-api-stop-using-mine-I-need-to-save-my-call-limit!!!

   ONLY ALLOWS LIKE, 25 'F*CKIN' API CALLS A DAY OR SOME STUPID SH*T LIKE THAT (D*MN A...........E CHEAPOS)!!!!!

   So (ahem)... anyway, it goes to say that, if you go get your own api-key (you don't have to, but if you don't you get ONE MEASLY FREE DEMO. That's it... or something like that), just be careful.

   This is why I hide my api-key inside a dot-env (that and it's good practice).
   '''
   try:
      from functions import all_data, filteredData, link, regularExpressionSearch

      ticker = input("Enter a Ticker Symbol: ")

      filteredResult = (filteredData(all_data, link(ticker))['data'])

      print(filteredResult)     

   except Exception as EXC:
      print("EXCEPTION: ", EXC)





      