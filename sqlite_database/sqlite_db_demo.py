if __name__ == "__main__":
   '''
   This is a sqlite3 demo. I will also use contextmanager (imported from contextlib. See below) to handle closing and other "garbage collection"/cleanup.

   I will demonstrate writing (POST) and getting (FETCH) data.

   NOTE: SQLITE 3 comes with Python.
   '''
   from contextlib import contextmanager;
   import sqlite3;

   @contextmanager
   def post_post_delete_data():
      sql_connection = sqlite3.connect("products.db"); # establish a connection.
      cursor = sql_connection.cursor();
      yield cursor; #returns the cursor to POST, PUT or DELETE data.
      sql_connection.commit(); # commits the data to sqlite3 after writing.
      sql_connection.close(); # closes the database connection to prevent side-effects, memory loss, etc....

   @contextmanager
   def fetch_data():
      sql_connection = sqlite3.connect("products.db");
      cursor = sql_connection.cursor();
      yield cursor;
      sql_connection.close(); # Not totally mandatory to close() when fetching, but good practice still.


