'''
*** (SOMEWHAT)IMPORTANT!!!! ***
requests is BLOCKING. What does that mean?
Let's say I have three requests:
request1 = request('http//api1.json') #Takes 5 seconds.
request2 = request('http//api1.json') #Takes 5 seconds.
request3 = request('http//api1.json') #Takes 5 seconds.

To run all three requests would take (about) 15 seconds b/c the next request will not even start till the other request is finished because request() is SYNCHRONOUS (it runs in order).

If you want asynchrounous (async/await), consider using .gather() or asyncio.TaskGroup. With asynchronous programming...

The same three requests would take (about) 5 seconds.
'''
import requests;

#Utilizing the following API: https://jsonplaceholder.typicode.com/.

def endpoint(endpoint):
   try:
      if endpoint not in ['users', 'posts', 'albums', 'todos']: raise Exception(f"Your endpoint of {endpoint} is is not in the list of ['users', 'posts', 'albums', 'todos']!!!");
   
      return requests.get(f"https://jsonplaceholder.typicode.com/{endpoint}").json()
   except Exception:
      return f"Error!!! {Exception}."

print(endpoint('users'))