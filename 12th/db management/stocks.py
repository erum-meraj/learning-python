#Creating database Stock and table Stocks and inserting 4 records
import mysql.connector
db_connection = mysql.connector.connect(host="localhost",user="root",passwd="sql@123")
db_cursor = db_connection.cursor()
db_cursor.execute("CREATE DATABASE Stocks")
db_cursor.execute('use Stocks')
db_cursor.execute("CREATE TABLE Stock1 (Itemno Integer PRIMARY KEY, Item VARCHAR(15), dcode Integer, qty Integer, Unitprice Integer, Stockdate date);")
db_cursor.execute("INSERT INTO Stock1 VALUES(3,'2',3,4,5,'2020-07-02')")
#db_cursor.execute("INSERT INTO movies (Itemno,Item,dcode, qty, Unitprice, Stockdate) VALUES(                      )")

db_cursor.execute("select * from Stock1")
rows=db_cursor.fetchall()
for i in rows:
     print("The data is",i)
db_connection.close()

