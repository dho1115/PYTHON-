from contextlib import contextmanager;
from time import sleep;

@contextmanager
def FileManager(filename, mode="r"): #automatically opens and closes file.
   '''
   BASIC FILE MANAGER.
   Automatically opens and closes file.
   NOTE: Yes... I know this already exists with the with open(file) as f, but... whatever.....
   NOTE II: Notice how,you (technically, kind of ) cannot do this with a regular function that "returns" a file because file.close would have to go below the return, which it cannot do. I mean... unless you don't want to return a file.

   NOTE III: @contextmanager accepts a generator which calls next() "in the backend" for you. That is why, if you notice in the code below... I am not calling next().
   '''
   modes = {"a+": "appending and reading", "a": "appending", "w+": "writing and reading", "w": "writing", "r": "reading"} #file mapping to be used in the print statement (below).
   file = open(filename, mode);
   print(f"successfully opened {filename} for {modes.get(mode)}!!!");

   yield file; # yields the file variable containing open(filename, mode)

   sleep(1.75); #pauses 1.75 seconds.
   print(f"About to close {filename}!!!");
   file.close(); #AUTMATICALLY closes file.

with FileManager("./file.txt", "a+") as f:
   # appendfile = f.write(" - just added this crap!!!") # uncomment this line to append.
   sleep(1.35);
   f.seek(0);
   readfile=f.read();
   print(readfile)


