if __name__ == "__main__":
   from functions import contestant_model, game_over, correctNumber, contest;

   contestant_props = [("Jamie", correctNumber), ("Rylie", correctNumber), ("Andie", correctNumber)];

   with contest(contestant_props, correctNumber) as c:
      print(c);
      print("\n")
