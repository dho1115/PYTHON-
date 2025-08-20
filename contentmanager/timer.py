from contextlib import contextmanager; #There is also an asynccontextmanager.
from time import time; #for timing purposes.

@contextmanager
def elapsedTime(fn):
   '''
   This is the generator that also acts as the decorator. The yield is where the function goes. 

   This decorator generator will display the elapsed time it takes for the function to finish running.

   next() is called behind the scenes.
   '''
   start = time();
   yield f"{'='*7} YIELD RESULT {'='*7}\n {fn()}\n{'='*29}"; #Run function here (in this case, someFunction).
   end = time();
   print(f"finished in {end-start} seconds.")

def someFunction():
   '''
   This goes inside the decorator.
   '''
   numbers = []
   for i in range(37000575):
      if (i%3525 == 0 and i%97 == 5): numbers = [*numbers, i];
   return f"There are {len(numbers)} numbers between 0 and 37,000,575 that are divisible by 3525 and gives a remainder of 5 when divided by 97, such as {numbers[0]}. For a complete list, please pay me $37,000,575.00"

with elapsedTime(someFunction) as yieldresult:
   print(yieldresult)