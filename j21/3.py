import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="dbshoptest",
)

mycursor = mydb.cursor()

sql = "INSERT INTO user VALUES (%s, %s, %s, %s)"
val = (5, "Highway 21", "john@example.com", "1234567890")
mycursor.execute(sql, val)

mydb.commit()

print(mycursor.rowcount, "record inserted.")
