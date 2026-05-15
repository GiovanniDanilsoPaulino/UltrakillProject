import mysql.connector
import credentials

database = mysql.connector.connect(
    host = "localhost",
    user = credentials.username,
    password = credentials.password
)

print(database)

mycursor = database.cursor()

mycursor.execute("DROP DATABASE IF EXISTS terminal")
mycursor.execute("CREATE DATABASE terminal")
mycursor.execute("USE terminal")

mycursor.execute("CREATE TABLE test(" \
"id INT NOT NULL, name VARCHAR(50))")

mycursor.execute("SHOW TABLES")

for x in mycursor:
    print(x)
