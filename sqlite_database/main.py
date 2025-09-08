from sqlite_db_demo import post_post_delete_data, fetch_data;

if __name__ == "__main__":
   with post_post_delete_data() as db:
      db.execute(
         '''
         CREATE TABLE IF NOT EXISTS products (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name VARCHAR(39) NOT NULL,
            price FLOAT NOT NULL,
            quantity INTEGER DEFAULT 0
         )
         '''
      );

      # listofproducts = [
      #    ('chocolate sprinkles bar', '1.15', 35),
      #    ('watermelon chunks', '7.35', 19),
      #    ('healthy almonds', '3.99', 7),
      #    ('iced tea bottles (black)', '3.99', 57),
      #    ('raisin boxes', '0.99', 0)
      # ];

      # db.executemany("INSERT INTO products (name, price, quantity) VALUES (?, ?, ?)", listofproducts); #Will comment this out b/c I do not want to insert the same products again.

      db.execute(
         '''
         SELECT 
         name, 
         price, 
         quantity,
         CASE
            WHEN quantity < 1 THEN 'OUT OF STOCK.'
            WHEN quantity < 15 THEN 'LOW.'
            ELSE 'IN STOCK.'
         END as STATUS
         FROM products;
         '''
      );

      result = db.fetchall();

      for i in result:
         print(f"name: {i[0]}\nprice: {i[1]}\nquantity: {i[2]}\nstatus: {i[3]}\n=========\n");