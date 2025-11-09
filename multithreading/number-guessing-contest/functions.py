from threading import Thread
from time import sleep;
from random import randint;
from contextlib import contextmanager;

game_over = False;
correctNumber = randint(1, 10);

def contestant_model(name, correctNumber):
   global game_over;

   guess = randint(1, 10);

   while not game_over:
      guess = randint(1, 10);
      game_over = (guess == correctNumber);
      sleep(1.5)
      print(f"{name}'s guess is {guess}... correct number is {correctNumber}\n");
   
   if (guess == correctNumber):
      print(f" *** CORRECT GUESS!!! *** {name} guessed {guess}. {name} wins!!! ");

      return f"*** CORRECT GUESS!!! *** {name} wins!!!"
   else:
      return f"LOSER!!!!!"

createthread = Thread(target=contestant_model, daemon=False, args=("Jamie", correctNumber))

@contextmanager
def contest(arrayOfContestants, correctNumber):
   global contestant_model;
   global stop_game;
   try:
      allThreads = [Thread(target=contestant_model, args=properties) for properties in arrayOfContestants];
      yield [thread.start() for thread in allThreads];

   except TypeError as TE:
      print(f"Error!!! arrayOfContestants argument must be an array that has. You have a type {type(arrayOfContestants)}!!! - {TE}.");

      yield f"Error!!! arrayOfContestants argument must be an array. You have a type {type(arrayOfContestants)} - {TE}!!!"
   
   except Exception as EXC:
      print(EXC);
      yield EXC;


