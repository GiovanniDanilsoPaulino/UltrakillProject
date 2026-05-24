from sqlite3 import OperationalError

import mysql.connector
import credentials

#connects to database
database = mysql.connector.connect(
    host = "localhost",
    user = credentials.username,
    password = credentials.password
)

print(database)

mycursor = database.cursor()

def execute_sql_scripts(filename):
    """Execute SQL scripts from a specified file."""
    with open(filename, 'r') as fd:
        sql_commands = fd.read().split(';')

    for command in sql_commands:
        try:
            mycursor.execute(command)
        except OperationalError as msg:
            print("Command skipped: ", msg)

#Creates terminal database
execute_sql_scripts('terminal.sql')

#Creates and fills enemies table
execute_sql_scripts('enemies.sql')
execute_sql_scripts('enemies_data.sql')

#Test that prints all enemies information
#mycursor.execute(select_enemies)
#for x in mycursor:
#    print(x)

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