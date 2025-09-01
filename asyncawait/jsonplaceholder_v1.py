'''
NOTE: Wanna see something a little more cooler with APIs and async/await? Go to:
the projects folder:
projects > stock_tracker > StockTracker.py. By the time you see this comment, StockTracker.py may be renamed to main.py.
'''
import aiohttp;
from aiohttp import ClientSession;
import asyncio;
from requests.exceptions import HTTPError;
from time import time;

url = 'https://jsonplaceholder.typicode.com/users';

async def fetch(client, url=url):
   async with client.get(url) as response:
      try:
         if response.status != 200: raise HTTPError(f"HTTP status code error!!! {response.status}.")
         return await response.json()
      except HTTPError as http:
         return f"{http}."
      
   
async def main():
   async with aiohttp.ClientSession() as client:
      '''      
      This client acts ALMOST like request, except that it is faster b/c it is NON-BLOCKING (requests are BLOCKING in that you have to WAIT for the request() to finish before moving on).

      The client (as client) has a .get() method (along with other CRUD methods) that we pass into the await fetch below. 

      Since we want to get information, we invoke client.get(url) inside the fetch function.
      '''
      return await fetch(client, url)

start = time();
get_result_for_main = asyncio.run(main());
end = time();

print(f"gatherCouroutine takes {end-start} seconds and there is the result:\n{get_result_for_main}")
