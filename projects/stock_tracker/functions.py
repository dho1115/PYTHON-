def API_Key():
   from dotenv import load_dotenv
   from os import getenv;

   load_dotenv(dotenv_path="../PasswordPrivacy/.env");
   secret_key = getenv("stockApiKey", "unable to retrieve api key... check path.")
   return secret_key;

def link(ticker_symbol, API_Key=API_Key()):
   '''
   Returns the link.
   arguments:
   ticker_symbol: ticker.
   API_Key: User's API key.
   '''
   try:      
      return f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={ticker_symbol}&apikey={API_Key}"
   except ValueError as VE:
      return VE;
   except Exception as EXC:
      return EXC;

async def all_data(link):
   '''
   Asynchronous function that accepts a link and then returns all of the data in json() format.
   '''
   import aiohttp;
   from requests.exceptions import HTTPError
   try:
      async with aiohttp.ClientSession() as client:
         result = await client.get(link)
         return await result.json()
   except HTTPError as HTTP:
      print(f"HTTP error encountered!!!", HTTP);
   except RuntimeWarning as RTW:
      print("You may want to await this with an asyncio.run or something...", RTW)

def filteredData(all_data, link):
   import asyncio;
   '''
   Returns:
   1. The symbol.
   2. The date the data was last refrreshed in yyyy-mm-dd format.
   3. The data where the key is yyyy-mm-dd and the value is the open, high, low, close and volume.

   Arguments:
   all_data: the all_data function.
   link: the url from alpha vantage.
   '''
   try:
      results = asyncio.run(all_data(link));     
      MetaData = results.get('Meta Data');
      Symbol = MetaData.get('2. Symbol');
      LastRefreshed = MetaData.get('3. Last Refreshed');
      TimeSeriesDaily = results.get('Time Series (Daily)');
      TimeSeriesDaily_list = list(TimeSeriesDaily.items());
      data = [{f'{TimeSeriesDaily_list[0]}': TimeSeriesDaily_list[1]} for i in range(5)];

      return dict(Symbol=Symbol, LastRefreshed=LastRefreshed, data=data);
   except Exception as EXC:
      print(EXC)
      return f"Exception in filteredData: {EXC}!!!"

tickerSymbol = input("Enter Ticker Symbol: ");

print(filteredData(all_data, link(tickerSymbol)))

