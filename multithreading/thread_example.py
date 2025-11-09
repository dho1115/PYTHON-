if __name__ == "__main__":
   from threading import Thread, Event;
   from time import sleep;
   try:
      counter = 0;
      stop_countdown = Event(); # the Event class to stop the thread. NOTE: ctrl-c does not work since create_thread (see the variable below) does NOT run on the main thread. It is running on its own thread. Here, I am creating an instance of the Event() class, which is stop_countdown.
      def autostop(create_thread): 
         stop_countdown.set(); #function that will prematurely stop countup_thread if I hit enter.
         create_thread.join();

      def countup_thread():
         global stop_countdown, counter

         while not stop_countdown.is_set():
            counter+=1;
            print(f"counter is now at... {counter}.");
            sleep(1.5);

            if counter >= 15:
               print(f"...okay. We're at {counter} now. That's enough!!!!!")
               stop_countdown.set(); # I am calling the .set() method inside my stop_countdown Event instance which stops the thread prematurely.
         
         print(f"Stop signal received. stop_countdown is now: {stop_countdown.is_set()}.");
      
      create_thread = Thread(target=countup_thread);
      create_thread.start(); # starting my thread.
      inputresult = input("Hit Enter to stop this countdown prematurely.\n");
      (inputresult == '') and autostop(create_thread);
      print("Prematurely stopped countdown.")

      

   except Exception as EXC:
      print("EXCEPTION OCCURRED: ", EXC);