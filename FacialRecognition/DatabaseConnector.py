import mysql.connector

cnx = mysql.connector.connect(user='root', password='1111',
                              host='localhost',
                              database='attendance')
mycursor = cnx.cursor()

sql = "INSERT INTO students (first_name, last_name) VALUES (%s, %s)"
val = ("John", "Highway")
mycursor.execute(sql, val)

cnx.commit()

print(mycursor.rowcount, "record inserted.")