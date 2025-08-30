from functools import reduce;

def MultiplyResult(*args):
   try:
      if len(args) < 1: raise Exception(f"You MUST have at least 1 argument for args. Right now, you have {args}!!!!!")
      return reduce(lambda accumulator, value: accumulator*value, list(args), 1);
   except TypeError as TE:
      return TE;
   except Exception as EXC:
      return EXC;

      