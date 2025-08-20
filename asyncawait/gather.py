import asyncio, aiohttp;
from time import time;

async def RunAsyncioSleep():
   '''
   Notice how much FASTER this function is, compared to the RunAsyncioSleep function that was in async_sleep.py.

   Also note that the 3 tasks here actually take LONGER (Task 1 here takes about 5 seconds wheras Task 1 inside async_sleep.py > RunAsyncioSleep takes only 3.5 seconds...
   
   And yet, THIS function is faster by almost 2.1 seconds!!!

   WHY???

   Because here, we DO NOT await asyncio.sleep. Instead, we put the "unawaited" version of asyncio.sleep (the coroutine version of asyncio.sleep) inside .gather() and THEN await it. .gather() runs these asynchrounously (non-blocking).
   '''
   Task1 = asyncio.sleep(5.0, "Task 1 takes about 5.0 seconds to complete.");
   Task2 = asyncio.sleep(3.5, "Task 2 takes about 3.5 seconds to complete.");
   Task3 = asyncio.sleep(1.5, "Task 1 takes about 1.5 seconds to complete.");

   gatherTasks = await asyncio.gather(Task1, Task2, Task3);

   return gatherTasks;

start = time();
TaskRunner = asyncio.run(RunAsyncioSleep());
end = time();

print(f"{TaskRunner} finished running all tasks. Elapsed time is {round(end - start, 5)} seconds.")

