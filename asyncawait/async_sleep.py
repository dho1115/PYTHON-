import asyncio, aiohttp;
from time import time;

async def RunAsyncioSleep():
   '''
   In this function, we are AWAITING asyncio.sleep, so here, it is NOT going to give us a coroutine. It will actually give us the result.

   Because of this, it is BLOCKING!!! Task 1 will run first and during the 3.5 seconds it takes Task 1 to run, NO OTHER TASKS WILL RUN UNTIL THE 3.5 SECONDS (roughly) are up. Then, Task 2 will run for (about) 1 second and no other task will run and finally, Task 3!

   This is similar to if you run the sleep method in Time.
   '''
   Task1 = await asyncio.sleep(3.5, "Task 1 takes about 3.5 seconds....");
   Task2 = await asyncio.sleep(1.0, "Task 2 takes about 1.0 second....");
   Task3 = await asyncio.sleep(2.5, "Task 3 takes about 2.5 seconds....");

   return f"TASK 1: {Task1} - TASK 2: {Task2} - TASK 3: {Task3}."

start = time();
RunTask = asyncio.run(RunAsyncioSleep());
end = time();

print(f"Finished running {RunTask}. Elapsed time is {round(end - start, 5)} seconds.")