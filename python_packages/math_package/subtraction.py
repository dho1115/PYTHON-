from functools import reduce;

def SubtractionResult(*args):
   try:
      if len(args) < 1: raise Exception(f"You must enter some kind of number!!! Right now, you have {args}.")
      if not filter(lambda x: eval(x), args): raise TypeError("Non-Number found!!!");
      return reduce(lambda accumulator, value: accumulator-value, list(args));
   except TypeError as TE:
      return "TYPE ERROR ALERT!!! " + TE;
   except Exception as EXC:
      return EXC;