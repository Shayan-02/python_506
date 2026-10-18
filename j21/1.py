import sqlite3

connection = sqlite3.connect("./my-db.db")
cursor = connection.cursor()

sql = """
INSERT INTO product VALUES (5,'[value-2]','[value-3]','[value-4]')
"""

cursor.execute(sql)
connection.commit()
connection.close()
