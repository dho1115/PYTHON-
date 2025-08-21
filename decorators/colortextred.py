from functools import wraps;

def textcolor_red(fn):
   from colorama import init;
   from termcolor import colored;
   @wraps(fn)
   def wrapper(text): #the text is what is passed into the fn below.
      init();
      return colored(f"{'*'*3}{fn(text)}{'*'*3}", 'red', attrs=['bold'])
   return wrapper #It is the WRAPPER declaration that is retured.

@textcolor_red
def sometext(text):
   return text;

print(sometext("This should be red.")) #decorated.
print(sometext.__wrapped__("This is not red. It is undecorated.")) #undecorated.

