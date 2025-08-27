from random import choice;
from time import sleep;

def RandomGibberishGenerator(ListOfWords:list):
   SentenceSoFar = "";
   try:
      if not isinstance(ListOfWords, list): raise TypeError(f"Your entry of {ListOfWords} is NOT a list!!! It is of {type(ListOfWords)}!!!")
      while "stop" not in SentenceSoFar:
         SentenceSoFar += choice(ListOfWords)
         if "stop" in SentenceSoFar: raise StopIteration(f"STOP is in SentenceSoFar, so I have to STOP. Sorry....")
         yield SentenceSoFar
         SentenceSoFar+=" ";
         sleep(0.75)
   except TypeError as TE:
      return TE
   except Exception as EXC:
      return f"Some other exception occurred... {EXC}!!!";
   except StopIteration as SI:
      return SI

MyGibberishGenerator = RandomGibberishGenerator(['marshmellows', 'rain', 'stop', 'antique', 'table', 'vacation', 'red', 'brown', 'coyote', 'house', 'coding', 'somewhere']);

print(next(MyGibberishGenerator));
print(next(MyGibberishGenerator));
print(next(MyGibberishGenerator));
print(next(MyGibberishGenerator));
print(next(MyGibberishGenerator));
print(next(MyGibberishGenerator));
print(next(MyGibberishGenerator));
print(next(MyGibberishGenerator));
print(next(MyGibberishGenerator));
print(next(MyGibberishGenerator));
print(next(MyGibberishGenerator));
print(next(MyGibberishGenerator));
print(next(MyGibberishGenerator));
print(next(MyGibberishGenerator));
print(next(MyGibberishGenerator));
print(next(MyGibberishGenerator));
print(next(MyGibberishGenerator));
print(next(MyGibberishGenerator));
print(next(MyGibberishGenerator));
print(next(MyGibberishGenerator));