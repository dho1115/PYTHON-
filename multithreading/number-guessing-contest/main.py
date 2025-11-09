if __name__ == "__main__":
   from functions import contestant_model, game_over, correctNumber, contest;

   contestant_props = [("Jamie", correctNumber), ("Rylie", correctNumber), ("Andie", correctNumber)];

   with contest(contestant_props, correctNumber) as c:
      print(c);
      
   stopThread = input("Press Enter to Stop...."); # I created the stopThread on this main thread (main.py is the 'main thread') so I can terminate this program (terminate the threads) if the "contestant" threads (the threads in allThreads) take to damn long to guess. NOTE: In order for the threads in allThreads to terminate when I hit "Enter", they must all be DAEMON threads.
