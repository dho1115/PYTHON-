import requests;

#Utilizing the following API: https://jsonplaceholder.typicode.com/.

def endpoint(endpoint):
   try:
      if endpoint not in ['users', 'posts', 'albums', 'todos']: raise Exception(f"Your endpoint of {endpoint} is is not in the list of ['users', 'posts', 'albums', 'todos']!!!");
   
      return requests.get(f"https://jsonplaceholder.typicode.com/{endpoint}").json()
   except Exception:
      return f"Error!!! {Exception}."

print(endpoint('users'))