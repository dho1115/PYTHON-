from functools import reduce;

def SubtractionResult(*args):
   return reduce(lambda accumulator, value: accumulator-value, list(*args), 0);