# https://www.youtube.com/watch?v=y8qLhov8QU8

from loguru import logger;

logger.info("This is the loguru_demo!!!") #Ran inside of the __main__ module, so it would show up as __main__:<module>: 5 (line 5).

def runLoggerInfo(msg:str):
   return logger.info(msg) #Ran inside of a runLoggerInfo function, so it returns as __main__:runLoggerInfo:8 

runLoggerInfo("This is inside of a function!!!")