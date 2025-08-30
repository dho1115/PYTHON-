from functools import reduce;

def MultiplyResult(*args):
   return reduce(lambda accumulator, value: accumulator*value, list(*args), 1);