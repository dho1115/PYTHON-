# NOTE: While colored does have a "blinking" attribute, that feature is not supported in windows... which is why I created this!!!!!

text = input("Input some text here!!!");

def flashingSign(text:str):
   from colorama import init;
   from termcolor import colored;
   from time import sleep;

   init(); # MANDATORY for windows users. Otherwise, the termcolor does NOT work!!! Not sure if you need this for Mac.

   redText = colored(text, color="red", attrs=["bold"]); #colors the text red.
   greenText = colored(text, color="yellow", attrs=["bold"]); #green.

   for i in range(5):
      ''' The Loop. '''
      print(redText, end="\r"); # The \r moves the cursor BACK to the beginning of the text.
      sleep(0.533); # Shows the text for 0.533 seconds...
      print(" "*len(text), end="\r"); # "Blacks out" the colored text by replacing it with enough " " to cover the text (hence, the len(text)).
      sleep(0.533);
      print(greenText, end="\r");
      sleep(0.533);
      print(" "*len(text), end="\r")
      sleep(0.533)
   
   return "FINISHED!!!"

print(flashingSign(text)); #Output.
   