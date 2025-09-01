from functools import wraps;

def textcolor_red(fn): # This is the DECORATOR!!!
   from colorama import init;
   from termcolor import colored;
   @wraps(fn) # Not really necessary... BUT if you ever want to unwrapp a function, you kinda, sorta need this ("kinda, sorta" because there IS another way to unwrap a function... but I forgot what it is :(:( :(.)
   def wrapper(text): #the text is what is passed into the fn below.
      init();
      return colored(f"{'*'*3}{fn(text)}{'*'*3}", 'red', attrs=['bold'])
   return wrapper #It is the WRAPPER declaration that is retured.

@textcolor_red
def sometext(text):
   return text;

print(sometext("This should be red.")) #decorated.
print(sometext.__wrapped__("This is not red. It is undecorated.")) #undecorated.

