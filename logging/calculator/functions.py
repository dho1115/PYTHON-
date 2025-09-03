def input_validation(*args):
   import logging;
   logging.basicConfig(level=logging.ERROR, filename="ErrorLog.log");
   try:
      def isNum(x):
         try:
            getFloat = float(x);
            return getFloat;
         except ValueError as VE:
            logging.error(VE)
            return VE;
         except TypeError as TE:
            logging.error(TE);
            return TE;
         except Exception as EXC:
            logging.error(EXC);
            return EXC;
   
      valuesAreNumbers = list(map(lambda x: isNum(x), args[0][0]));
      return valuesAreNumbers;
   except Exception as EXC:
      logging.error(f"Error inside input_validation function: {EXC}.")
      return f"Error inside input_validation function: {EXC}."

def addition(*args):
   import logging;
   logging.basicConfig(level=logging.ERROR, filename="ErrorLog.log");
   try:
      numbers = input_validation(args)
      result = sum(numbers);
      return result;
   except Exception as EXC:
      logging.error(msg=f"FROM: {__name__}. ERROR: ADDITION ERROR!!! {dict(file=__name__, EXC=EXC)}.", exc_info=EXC);
      return f"addition EXCEPTION!!! {EXC}.";

def subtraction(*args):
   import logging;
   from functools import reduce
   logging.basicConfig(level=logging.ERROR, filename="ErrorLog.log");
   try:
      numbers = input_validation(args);
      result = reduce(lambda accumulator, value: accumulator-value, numbers);
      return result;
   except Exception as EXC:
      logging.error(f"FROM: {__name__}. ERROR: subtraction EXCEPTION!!! {dict(File=__name__, EXC=EXC)}.", exc_info={dict(file=__name__, exception=EXC)});
      return f"subtraction EXCEPTION - {EXC}!!!"
   
def multiplication(*args):
   import logging;
   from functools import reduce
   logging.basicConfig(level=logging.ERROR, filename="ErrorLog.log");
   try:
      numbers = input_validation(args);
      result = reduce(lambda accumulator, value: accumulator*value, numbers);
      return result;
   except Exception as EXC:
      logging.error(f"From: {__name__} ERROR: multiplication EXCEPTION!!! {EXC}.");
      return f"multiplication EXCEPTION - {EXC}!!!"
      