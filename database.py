import mysql.connector
import credentials
import data

#connects to database
database = mysql.connector.connect(
    host = "localhost",
    user = credentials.username,
    password = credentials.password
)

print(database)

mycursor = database.cursor()

#Creates terminal database
mycursor.execute("DROP DATABASE IF EXISTS terminal")
mycursor.execute("CREATE DATABASE terminal")
mycursor.execute("USE terminal")

#Creates Enemies table
create_enemies = "CREATE TABLE Enemies(" \
"name VARCHAR(50)," \
"type VARCHAR(50)," \
"data TEXT," \
"strategy TEXT)"

#Inserts all of the enemies information into the Enemies table
insert_enemies = "INSERT INTO Enemies(name, type, data, strategy)" \
"VALUES" \
"('Filth', 'Lesser Husk', '" + data.husk_data + "', '" + data.husk_strategy + "')," \
"('Stray', 'Lesser Husk', '" + data.stray_data + "', '" + data.stray_strategy + "')," \
"('Schism', 'Greater Husk', '" + data.schism_data + "', '" + data.schism_strategy + "')," \
"('Soldier', 'Greater Husk', '" + data.soldier_data + "', '" + data.soldier_strategy + "')," \
"('The Corpse of King Minos', 'Supreme Husk', '" + data.minos_data + "', '" + data.minos_strategy + "')," \
"('Stalker', 'Lesser Husk', '" + data.stalker_data + "', '" + data.stalker_strategy + "')," \
"('Insurrectionist', 'Supreme Husk', '" + data.insurrectionist_data + "', '" + data.insurrectionist_strategy + "')," \
"('Ferryman', 'Supreme Husk', '" + data.ferryman_data + "', '" + data.ferryman_strategy + "')," \
"('Mirror Reaper', 'Supreme Husk', '" + data.reaper_data + "', '" + data.reaper_strategy + "')," \
"('Swordsmachine', 'Greater Machine', '" + data.swordsmachine_data + "', '" + data.swordsmachine_strategy + "')," \
"('Drone', 'Lesser Machine', '" + data.drone_data + "', '" + data.drone_strategy + "')," \
"('Streetcleaner', 'Lesser Machine', '" + data.streetcleaner_data + "', '" + data.streetcleaner_strategy + "')," \
"('V2', 'Supreme Machine', '" + data.v20_data + "', '" + data.v20_strategy + "')," \
"('Mindflayer', 'Greater Machine', '" + data.mindflayer_data + "', '" + data.mindflayer_strategy + "')," \
"('V2 \\(2nd\\)', 'Supreme Machine', '" + data.v21_data + "', '" + data.v21_strategy + "')," \
"('Sentry', 'Greater Machine', '" + data.sentry_data + "', '" + data.sentry_strategy + "')," \
"('Gutterman', 'Greater Machine', '" + data.gutterman_data + "', '" + data.gutterman_strategy + "')," \
"('Guttertank', 'Greater Machine', '" + data.guttertank_data + "', '" + data.guttertank_strategy + "')," \
"('Earthmover', 'Supreme Machine', '" + data.earthmover_data + "', '" + data.earthmover_strategy + "')," \
"('Malicious Face', 'Lesser Demon', '" + data.face_data + "', '" + data.face_strategy + "')," \
"('Cerberus', 'Lesser Demon', '" + data.cerberus_data + "', '" + data.cerberus_strategy + "')," \
"('Hideous Mass', 'Greater Demon', '" + data.mass_data + "', '" + data.mass_strategy + "')," \
"('Idol', 'Lesser Demon', '" + data.idol_data + "', '" + data.idol_strategy + "')," \
"('Leviathan', 'Supreme Demon', '" + data.leviathan_data + "', '" + data.leviathan_strategy + "')," \
"('Mannequin', 'Lesser Demon', '" + data.mannequin_data + "', '" + data.mannequin_strategy + "')," \
"('Minotaur', 'Supreme Demon', '" + data.minotaur_data + "', '" + data.minotaur_strategy + "')," \
"('Deathcatcher', 'Lesser Demon', '" + data.deathcatcher_data + "', '" + data.deathcatcher_strategy + "')," \
"('Geryon', 'Supreme Demon', '" + data.geryon_data + "', '" + data.geryon_strategy + "')," \
"('Gabriel, Judge of Hell', 'Supreme Angel', '" + data.judge_data + "', '" + data.judge_strategy + "')," \
"('Virtue', 'Lesser Angel', '" + data.virtue_data + "', '" + data.virtue_strategy + "')," \
"('Gabriel, Apostate of Hate', 'Supreme Angel', '" + data.apostate_data + "', '" + data.apostate_strategy + "')," \
"('Providence', 'Lesser Angel', '" + data.providence_data + "', '" + data.providence_strategy + "')," \
"('Power', 'Greater Angel', '" + data.power_data + "', '" + data.power_strategy + "')"

select_enemies = "SELECT *" \
"FROM terminal.enemies"

for x in mycursor:
    print(x)

mycursor.execute(create_enemies)
mycursor.execute(insert_enemies)

#Test that prints all enemies information
mycursor.execute(select_enemies)
for x in mycursor:
    print(x)

#def selectType(string type) :
#    a = type