def textcolor_red(fn):
   from colorama import init;
   from termcolor import colored;
   def wrapper(text):
      init();
      return colored(f"{'*'*3}{fn(text)}{'*'*3}", 'red', attrs=['bold'])
   return wrapper

@textcolor_red
def sometext(text):
   return text;

print(sometext("This should be red."))

