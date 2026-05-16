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

create_enemies = "CREATE TABLE Enemies(" \
"name VARCHAR(50)," \
"type VARCHAR(50)," \
"data TEXT," \
"strategy TEXT)"

insert_enemies = "INSERT INTO Enemies(name, type, data, strategy)" \
"VALUES" \
"('Filth', 'Lesser Husk', 'fill data later', 'fill strategy later')," \
"('Stray', 'Lesser Husk', 'fill data later', 'fill strategy later')," \
"('Schism', 'Greater Husk', 'fill data later', 'fill stategy later')"

select_enemies = "SELECT *" \
"FROM terminal.enemies"

for x in mycursor:
    print(x)

mycursor.execute(create_enemies)
mycursor.execute(insert_enemies)
mycursor.execute(select_enemies)

for x in mycursor:
    print(x)


