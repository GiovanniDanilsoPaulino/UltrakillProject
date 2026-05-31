from sqlite3 import OperationalError

import sys
for path in sys.path:
    print(path)

import mysql.connector
import credentials

#connects to database
connection = mysql.connector.connect(
    host = "localhost",
    user = credentials.username,
    password = credentials.password
)

print(connection)

mycursor = connection.cursor()

def executeSqlScripts(filename):
    """Execute SQL scripts from a specified file."""
    with open(filename, 'r') as fd:
        sql_commands = fd.read().split(';')

    for command in sql_commands:
        try:
            mycursor.execute(command)
        except OperationalError as msg:
            print("Command skipped: ", msg)

#Creates terminal database
executeSqlScripts('../db/terminal.sql')

#Creates and fills enemies table
executeSqlScripts('../db/enemies.sql')
executeSqlScripts('../db/enemies_data.sql')

#Test that prints all enemies information
#mycursor.execute(select_enemies)
#for x in mycursor:
#    print(x)

#Returns all the enemies as a dictionary
def returnEnemies() :
    mycursor.execute("SELECT * FROM terminal.Enemies")
    dictionary = {}
    for enemy in mycursor:
        dictionary[enemy[0]] = enemy
    return dictionary

#Selects all enemies where type contains enemy_type
def selectType(enemy_type) :
    mycursor.execute("SELECT * FROM terminal.Enemies " \
    "WHERE type LIKE '%" + enemy_type + "%';")

#Selects all enemies where data contains enemy_data
def selectData(enemy_data) :
    mycursor.execute("SELECT * FROM terminal.Enemies " \
    "WHERE data LIKE '%" + enemy_data + "%';")

#Selects all enemies where strategy contains enemy_strategy
def selectStrategy(enemy_strategy) :
    mycursor.execute("SELECT * FROM terminal.Enemies " \
    "WHERE strategy LIKE '%" + enemy_strategy + "%';")

#Tests for selectType, selectData, and selectStrategy
selectType("supreme")
for x in mycursor:
    print(x[0])

selectData("hell")
for x in mycursor:
    print(x[0])

selectStrategy("black hole")
for x in mycursor:
    print(x[0])

executeSqlScripts('../db/guns.sql')
executeSqlScripts('../db/weapons.sql')

executeSqlScripts('../db/guns_data.sql')
executeSqlScripts('../db/weapons_data.sql')

#Test for printing all weapons data
#mycursor.execute("SELECT * FROM weapons")
#for x in mycursor:
#    print(x)
#Test for printing all guns data
#mycursor.execute("SELECT * FROM guns")
#for x in mycursor:
#    print(x)