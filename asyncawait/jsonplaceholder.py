import aiohttp;
import asyncio;

url = 'https://jsonplaceholder.typicode.com/users';

async def fetch(client, url=url):
   async with client.get(url) as response:
      assert response.status == 200
      return await response.text()
   
async def main():
   async with aiohttp.ClientSession() as client:
      '''      
      This client acts ALMOST like request, except that it is faster b/c it is NON-BLOCKING (requests are BLOCKING in that you have to WAIT for the request() to finish before moving on).

      The client (as client) has a .get() method (along with other CRUD methods) that we pass into the await fetch below. 

      Since we want to get information, we invoke client.get(url) inside the fetch function.
      '''
      return await fetch(client)

getresult = asyncio.run(main());
print(getresult)
