from threading import Thread, Event;
from time import sleep;
from random import randint;
from contextlib import contextmanager;

game_over = False;
correctNumber = randint(1, 50);

def contestant_model(name, correctNumber):
   '''
   The function to be used as the "target" for the Thread.
   PARAMETERS:
   name: The contestant's name as a 'str'.
   correctNumber: The correct guess as an 'int'.
   '''
   global game_over;

   guess = randint(1, 50);

   while not game_over:
      guess = randint(1, 50);
      game_over = (guess == correctNumber);
      sleep(1.5)
      print(f"{name}'s guess is {guess}... correct number is {correctNumber}\n");
   
   if (guess == correctNumber):
      print(f" *** CORRECT GUESS!!! *** {name} guessed {guess}. {name} wins!!! ");

      return f"*** CORRECT GUESS!!! *** {name} wins!!!"
   else:
      return f"LOSER!!!!!"

@contextmanager
def contest(contestant_props, correctNumber):
   '''
   This function declaration (context manager) handles not only taking in the contestant props and turning those props into a Thread, but it also STARTS the thread (something I keep forgetting to do and then I wonder why the thread is not... STARTING!!!).

   Note how each individual threads inside allThreads is a DAEMON THREAD!!!

   PARAMETERS:
   contestant_props: a dict that contains the following properties: name & correctNumber.
   correctNumber: the number the guess must equal for the contest to end (it also ends when I terminate the main thread by hitting ENTER on main.py).
   '''
   global contestant_model;
   try:
      '''
      Note below inside allThreads, how I set each of the Thread values inside allThreads to daemon=True. I want to do this because I want these threads to be DAEMON THREADS. 

      What are Daemon Threads? These are threads that terminate when the main thread (in this case, main.py is the main thread) terminates or stops.

      When will main.py stop? In this case, I added a stopThread = input(...) inside main.py.

      As long as I do not hit "Enter" for stopThread, main.py (the main thread) will still continue (because it has not been terminated b/c the input() value has not been entered yet).
      '''
      allThreads = [Thread(target=contestant_model, daemon=True, args=properties) for properties in contestant_props];

      yield [thread.start() for thread in allThreads];

      print("Threads have started...")
   except TypeError as TE:
      print(f"Error!!! arrayOfContestants argument must be an array that has. You have a type {type(contestant_props)}!!! - {TE}.");

      yield f"Error!!! arrayOfContestants argument must be an array. You have a type {type(contestant_props)} - {TE}!!!"
   
   except Exception as EXC:
      print(EXC);
      yield EXC;


