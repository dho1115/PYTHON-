def API_Key():
   from dotenv import load_dotenv
   from os import getenv;

   load_dotenv(dotenv_path="../PasswordPrivacy/.env");
   secret_key = getenv("stockApiKey", "unable to retrieve api key... check path.")
   return secret_key;

def link(ticker_symbol, API_Key=API_Key()):
   '''
   Returns the link.
   parameters:
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
   parameters:
   link: link as string.
   '''
   import aiohttp;
   from requests.exceptions import HTTPError
   try:
      async with aiohttp.ClientSession() as client:
         result = await client.get(link)
         if not result: raise Exception(f"Cannot get link!!! No such ticker!!!!!")
         return await result.json()
   except HTTPError as HTTP:
      print(f"HTTP error encountered!!!", HTTP);
   except RuntimeWarning as RTW:
      print("You may want to await this with an asyncio.run or something...", RTW)
   except Exception as EXC:
      print("SHIT!!! An exception occurred: ", EXC)


def filteredData(all_data, link):
   '''
   parameters:
   all_data: the all_data function.
   link: the link function (def link) with the ticker: link(ticker).

   return:
   1. The symbol.
   2. The date the data was last refrreshed in yyyy-mm-dd format.
   3. The data where the key is yyyy-mm-dd and the value is the open, high, low, close and volume.
   '''
   '''
   WARNING!!! API ONLY MAKES, LIKE 25 CALLS PER DAY OR SOME SHIT LIKE THAT. USE THE CALLS WISELY...

   AND GO GET YOUR OWN DAMN API KEY!!! I NEED TO SAVE MY GOOFY-ASS CALLS.
   '''
   import asyncio
   try:
      results = asyncio.run(all_data(link));     
      MetaData = results.get('Meta Data');
      Symbol = MetaData.get('2. Symbol');
      LastRefreshed = MetaData.get('3. Last Refreshed');
      TimeSeriesDaily = results.get('Time Series (Daily)'); #{"2025-08-29": {...}, "2025-08-28": {...}, "2025-08-27": {...}}
      closingDates = list(TimeSeriesDaily.keys());
      closingValues = list(TimeSeriesDaily.values());
      first5Dates = [closingDates[i] for i in range(5)];
      first5Values = [closingValues[i] for i in range(5)];
      first5ClosingValues = list(map(lambda x: x.get("4. close"), first5Values))

      return dict(Symbol=Symbol, LastRefreshed=LastRefreshed, data=dict(first5Dates=first5Dates, first5Values=first5Values, first5ClosingValues=first5ClosingValues));
   except Exception as EXC:
      print(EXC)
      return f"Exception in filteredData: {EXC}!!!"

def regularExpressionSearch(patternToSearch, tuple_string):
   global data;
   import re;
   date = re.search(patternToSearch, tuple_string);
   group_date = date.group(0);
   return group_date

def Chart(xAxisArray:list, yAxisArray:list, xLabel:str=None, yLabel:str=None):
   '''
   Using Numpy and Matplotlib, this function takes in values for x axis (xAxisArray) and y axis (yAxisArray) along with optional values for xLabel and yLabel and plots a chart using Matplotlib.

   Parameters:
   xAxisArray: A LIST[] of x values.
   yAxisArray: A LIST[] OF y values.
   xLabel: Text you want to display on X axis.
   yLabel: Ditto for Y axis.
   '''
   import numpy as np;
   import matplotlib.pyplot as mpp;
   try:
      xValues = np.array(xAxisArray, dtype=object)
      yValues = np.array(yAxisArray, dtype=object)
      mpp.plot(xValues, yValues);
      labelX = mpp.xlabel(xLabel) if xLabel else None;
      labelY = mpp.ylabel(yLabel) if yLabel else None;
      mpp.show();
   except Exception as EXC:
      print("There seems to be an error inside Chart Function: ", EXC);
   finally:
      mpp.close(); #closes the chart no matter what.
   



