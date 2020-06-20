'''
 1. Create connection to the database
 2. Create database in MySQL (use the "CREATE DATABASE" statement)
 3. Check if a database exist by listing all databases in your system (use the "SHOW DATABASES" statement)
 4. Or access the database when making the connection (adding "database="mydatabase"")
 5. Create a table in MySQL (use the "CREATE TABLE" statement)
 6. Check if a table exist by listing all tables in database (use the "SHOW TABLES" statement)
 7. Insert unique number for each record by defining a PRIMARY KEY (use the "INT AUTO_INCREMENT PRIMARY KEY" statement).
    If the table already exist, use "ALTER TABLE" keyword.
 8. Fill a table in MySQL (use the "INSERT INTO" statement)
 9. Insert multiple rows into a table (use the "executemany()" method - a list of tuples, containing data to insert)
10. Insert one row, and return ID
11. Select from a table in MySQL (use the "SELECT" statement)
12. Select only some of the columns in a table (use the "SELECT" statement followed by the column name(s))
13. Select only one row (use the "fetchone() method - will return the first row)
14. Filter the selection when selecting records from a table (use the "WHERE" statement)
15. Select the records that starts, includes, or ends with given letter or phrase (use the "%" to represent wildcard
    character)
16. Use escape query values to escape values provided by users in order to prevent SQL injections (use the placeholder
    "%s" method)
17. Sort the result in acsending or descending order ("ORDER BY" keyword sorts the result ascending by default. "DESC"
    keyword sorts the result in descending)
18. Delete records from an existing table (use the "DELETE FROM" statement)
19. Escape the values of any query in delete statement to prevent SQL injection (use the "%s" to escape values)
20. Delete the existing table (use the "DROP TABLE" statement)
21. Delete the table only if exist to avoid an error (use the "IF EXIST" keyword)
22. Update existing records in a table (use the "UPDATE" statement)
23. Escape the values of any query in update statement to prevent SQL injection (use the "%s" to escape values)
24. Limit the number of records returned from the query (use the "LIMIT" statement)
25. Return number of records starting from another position (use the "OFFSET" statement)
26. Join users and products to see the name of the users favorite product
27. Select all users and their favorite product
28. Select all products, and the user(s) who have them as their favorite

Created on Jun 19, 2020

@author: olegg
'''

''' MySQL Connector must be installed and ready to use
Package                Version
---------------------- -------
mysql-connector-python 8.0.20
'''
import mysql.connector

''' Create connection to the database. Use username and password from MySQL database '''
mydb = mysql.connector.connect(
  host="localhost",
  user="login",
  password="password",
  database="mydatabase"         #connecting to database
)

#print(mydb)

mycursor = mydb.cursor()

''' Create a database in MySQL '''
'''
mycursor.execute("CREATE DATABASE mydatabase")
'''

''' Check if a database exist by listing all dtabases in system '''
'''
mycursor.execute("SHOW DATABASES")
for x in mycursor:
    print(x)
'''

''' Create a table in MySQL '''
'''
mycursor.execute("CREATE TABLE customers (name VARCHAR(255), address VARCHAR(255))")
'''

''' Check if table exist by listing all tables in your database '''
'''
mycursor.execute("SHOW TABLES")
for x in mycursor:
    print(x)
'''

''' Create a column with a unique key for each record '''
'''
mycursor.execute("CREATE TABLE customers (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), address VARCHAR(255))")
'''

''' If the table already exists, use the ALTER TABLE keyword '''
'''
mycursor.execute("ALTER TABLE customers ADD COLUMN id INT AUTO_INCREMENT PRIMARY KEY")
'''

''' Fill a table in MySQL. Insert a record in the "customers" table '''
'''
sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
val = ("John", "Highway 21")
mycursor.execute(sql, val)
mydb.commit()               # This requires to make changes, otherwise no changes made to the table
print(mycursor.rowcount, "record inserted.")
'''

''' Insert multiple rows into "customers" table '''
'''
sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
val = [
  ('Peter', 'Lowstreet 4'),
  ('Amy', 'Apple st 652'),
  ('Hannah', 'Mountain 21'),
  ('Michael', 'Valley 345'),
  ('Sandy', 'Ocean blvd 2'),
  ('Betty', 'Green Grass 1'),
  ('Richard', 'Sky st 331'),
  ('Susan', 'One way 98'),
  ('Vicky', 'Yellow Garden 2'),
  ('Ben', 'Park Lane 38'),
  ('William', 'Central st 954'),
  ('Chuck', 'Main Road 989'),
  ('Viola', 'Sideway 1633')
]
mycursor.executemany(sql, val)
mydb.commit()               # This requires to make changes, otherwise no changes made to the table
print(mycursor.rowcount, "was inserted.")
'''

''' Inserted one row and return the ID '''
'''
sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
val = ("Michelle", "Blue Village")
mycursor.execute(sql, val)
mydb.commit()
print("1 record inserted, ID:", mycursor.lastrowid)
'''

''' Select all records from the "customers" table and display the result '''
'''
mycursor.execute("SELECT * FROM customers")
myresult = mycursor.fetchall()      # fetchall() method, which fetches all rows from the last executed statement
for x in myresult:
  print(x)
'''

''' Select only the name and address columns '''
'''
mycursor.execute("SELECT name, address FROM customers")
myresult = mycursor.fetchall()
for x in myresult:
  print(x)
'''

''' Return the first row of the result '''
'''
mycursor.execute("SELECT * FROM customers")
myresult = mycursor.fetchone()          # fetch only one row, the first row
print(myresult)
'''

''' Select record(s) where the address is "Park Lane 38" '''
'''
sql = "SELECT * FROM customers WHERE address ='Park Lane 38'"
mycursor.execute(sql)
myresult = mycursor.fetchall()
for x in myresult:
  print(x)
'''

''' Select records where the address contains the word "way" '''
'''
sql = "SELECT * FROM customers WHERE address LIKE '%way%'"      # "%" represents wildcard characters
mycursor.execute(sql)
myresult = mycursor.fetchall()
for x in myresult:
  print(x)
'''

''' Escape query values provided by users using "%s" '''
'''
sql = "SELECT * FROM customers WHERE address = %s"
adr = ("Yellow Garden 2", )
mycursor.execute(sql, adr)
myresult = mycursor.fetchall()
for x in myresult:
  print(x)
'''

''' Sort the result alphabetically by name '''
'''
sql = "SELECT * FROM customers ORDER BY name"
mycursor.execute(sql)
myresult = mycursor.fetchall()
for x in myresult:
  print(x)
'''

''' Sort the result reverse alphabetically by name '''
'''
sql = "SELECT * FROM customers ORDER BY name DESC"
mycursor.execute(sql)
myresult = mycursor.fetchall()
for x in myresult:
  print(x)
'''

''' Delete any record where the address is "Mountain 21" '''
'''
sql = "DELETE FROM customers WHERE address = 'Mountain 21'"     # If omit "WHERE" clause, all records will be deleted
mycursor.execute(sql)
mydb.commit()           # This requires to make changes, otherwise no changes made to the table
print(mycursor.rowcount, "record(s) deleted")
'''

''' Escape values by using placeholder "%s" method '''
'''
sql = "DELETE FROM customers WHERE address = %s"
adr = ("Yellow Garden 2", )
mycursor.execute(sql, adr)
mydb.commit()
print(mycursor.rowcount, "record(s) deleted")
'''

''' Delete the table "customers" '''
'''
sql = "DROP TABLE customers"
mycursor.execute(sql)
'''

''' Delete the table "customers" if it exist '''
'''
sql = "DROP TABLE IF EXISTS customers"
mycursor.execute(sql)
'''

''' Overwrite the address column from "Valley 345" to "Canyoun 123" '''
'''
sql = "UPDATE customers SET address = 'Canyon 123' WHERE address = 'Valley 345'"    # If omit "WHERE" clause, all records will be updated
mycursor.execute(sql)
mydb.commit()
print(mycursor.rowcount, "record(s) affected")
'''

''' Escape values by using the placeholder "%s" method '''
'''
sql = "UPDATE customers SET address = %s WHERE address = %s"
val = ("Valley 345", "Canyon 123")
mycursor.execute(sql, val)
mydb.commit()
print(mycursor.rowcount, "record(s) affected")
'''

''' Select the 5 first records in the "customers" table '''
'''
mycursor.execute("SELECT * FROM customers LIMIT 5")
myresult = mycursor.fetchall()
for x in myresult:
  print(x)
'''

''' Start from position 3 and return 5 records '''
'''
mycursor.execute("SELECT * FROM customers LIMIT 5 OFFSET 2")
myresult = mycursor.fetchall()
for x in myresult:
  print(x)
'''

''' Create a "users" and a "products" tables '''
'''
mycursor.execute("CREATE TABLE users (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), fav DECIMAL(3,0))")
mycursor.execute("CREATE TABLE products (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255))")
'''

''' Insert rows in "users" table '''
'''
sql = "INSERT INTO users (name, fav) VALUES (%s, %s)"
val = [
  ('John', '154'),
  ('Peter', '154'),
  ('Amy', '155'),
  ('Hannah', '0'),
  ('Michael', '0')
]
mycursor.executemany(sql, val)
mydb.commit()               # This requires to make changes, otherwise no changes made to the table
print(mycursor.rowcount, "was inserted.")
'''

''' Insert rows in "products" table '''
'''
sql = "INSERT INTO products (id, name) VALUES (%s, %s)"
val = [
  ('154', 'Chocolate Heaven'),
  ('155', 'Tasty Lemons'),
  ('156', 'Vanilla Dreams')
]
mycursor.executemany(sql, val)
mydb.commit()               # This requires to make changes, otherwise no changes made to the table
print(mycursor.rowcount, "was inserted.")
'''

''' Join "users" and "products" to see the name of the users favorite product '''

sql = "SELECT \
  users.name AS user, \
  products.name AS favorite \
  FROM users \
  INNER JOIN products ON users.fav = products.id"   # combined by using users' fav field and products' id field
mycursor.execute(sql)
myresult = mycursor.fetchall()
for x in myresult:
    print(x)
print('')


''' Show all users even if they do not have a favorite product by using "LEFT JOIN" statement '''

sql = "SELECT \
  users.name AS user, \
  products.name AS favorite \
  FROM users \
  LEFT JOIN products ON users.fav = products.id"    # combined by using users' fav field and products' id field
mycursor.execute(sql)
myresult = mycursor.fetchall()
for x in myresult:
    print(x)
print('')


''' Return all products, and the users who have them as their favorite, even if no user have them as their favorite, use the "RIGHT JOIN" statement '''

sql = "SELECT \
  users.name AS user, \
  products.name AS favorite \
  FROM users \
  RIGHT JOIN products ON users.fav = products.id"   # combined by using users' fav field and products' id field
mycursor.execute(sql)
myresult = mycursor.fetchall()
for x in myresult:
    print(x)
print('')


'''
sql = "DROP TABLE IF EXISTS users"
mycursor.execute(sql)

sql = "DROP TABLE IF EXISTS products"
mycursor.execute(sql)

mycursor.execute("SHOW TABLES")
for x in mycursor:
    print(x)
'''
