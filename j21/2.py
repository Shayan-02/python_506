import mysql.connector

# Connect to server
cnx = mysql.connector.connect(
    host="127.0.0.1", port=3306, user="root", password="", database="dbshoptest"
)

# Get a cursor
cur = cnx.cursor()


sql = "INSERT INTO user VALUES (1,'[value-2]','[value-3]','[value-4]')"


# Execute a query
cur.execute(sql)

# Fetch one result
row = cur.fetchone()
print("Current date is:  {}".format(row[0]))

# Close connection
cnx.close()
