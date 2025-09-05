# https://www.youtube.com/watch?v=y8qLhov8QU8

from loguru import logger;

if __name__ == "__main__":
   try:
      logger.remove() # removes any defaults (by default, logger does not log traceback).
      logger.add('MyLogs.log', level="TRACE", format="LOG TIME: {time} | {level} | message: {message} | extra information: {extra}") # level = TRACE is lowest level.

      logger.info("This is the loguru_demo!!!") #Ran inside of the __main__ module, so it would show up as __main__:<module>: 5 (line 5).

      def runLoggerInfo(msg:str):
         return logger.info(msg) #Ran inside of a runLoggerInfo function, so it returns as __main__:runLoggerInfo:8 

      runLoggerInfo("This is inside of a function!!!")

      print("Hello"%3) # Should raise an exception that will show up in MyLogs.log.

   except Exception as EXC:
      logger.error(f"ERROR!!! => {EXC} - {EXC.args}");