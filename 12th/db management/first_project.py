
import mysql.connector as sql
con = sql.connect(host = 'localhost', user = 'root', password = 'erummeraj', database = 'python_db')
cur = con.cursor()
#cur.execute("INSERT INTO python_db.student(Rollno, name, age, city) VALUES(4, 'd', 15, 'mumbai')")

'''ctr = 1;
while ctr != 0:
    roll = int(input("Enter roll no. :    "))
    age = int(input("Enter age:    "))
    n = input("Enter name:   ")
    city = input("Enter city:   ")
    query = "insert into student(Rollno, name, age, city) values({}, '{}', '{}', '{}' ) ".format(roll, n , age, city)
    cur.execute(query)
    con.commit()
    print("done")
    ctr = int(input("Enter 1 to insert another record or enter 0:   "))
'''
cur.execute("show databases")
con.commit()
con.close;
