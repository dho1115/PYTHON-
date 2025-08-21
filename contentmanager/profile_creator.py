from contextlib import contextmanager;
from time import sleep;

@contextmanager
def ProfileManager():
   '''
   This context manager YIELDS a class that exposes a method called 'generate'. To use this method, you just use PF.generate. 'PF' is the alias to this ProfileManager (which in turn, yields the generate method.)
   '''
   print("Any logic needed to automatically START/OPEN/EXPOSE the properties, functions, classes, etc... goes here.");
   print("Starting up Profile mangager...");
   sleep(1.5);
   print("Please wait while we get the GenerateProfile class ready...");
   sleep(3.75);
   print("FINISHED setting up GenerateProfile!!!");

   class GenerateProfile:
      def __init__(self):
         self.dictionary = {}
      
      @classmethod
      def generate(cls, _id, name, role):
         from colorama import init;
         from termcolor import colored;

         init();
         try:
            roles = dict(manager = "red", HR="yellow", janitor="red")
            coloredRole = lambda : colored(f"{role}", color=roles[role], attrs=["bold"]) # I have to put this inside a function or it will throw an error if role is staff b/c colored() IMMEDIATELY invokes/calls colored and will break when 'staff' is encountered.

            print(f"_id={_id}, name={name}, role={coloredRole() if roles.get(role) else role}")

            return (f"_id: {_id} name: {name}, role: {role}")
         except Exception as EXC:
            print("EXCEPTION!!! =>", EXC);

   yield GenerateProfile;

   print("Any logic to close this content manager would go here.")

with ProfileManager() as PF: #the PF is actually the 'alias' for ProfileManager(). The called/activated function goes below.
   PF.generate('jamie111', 'Jamie Smith', 'manager');
   PF.generate('nic333', 'Nickee Naylor', 'HR');
   PF.generate('acey355', 'Acey Riley', 'staff');
   
