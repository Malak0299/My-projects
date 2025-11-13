# - SQL Setup -

import sqlite3
connection = sqlite3.connect('butik_trans.db')
cursor = connection.cursor()

#------------------------------
#-Create, Read, Update, Delete-
#------------------------------
# Create: Opretter nye data
# Read: Henter data
# Update: Ænder data
# Delete: Sletter data


# - 1. Opret tabeller med deres atrributter -
com1 = """CREATE TABLE IF NOT EXISTS
butik(butik_id INTEGER PRIMARY KEY, location TEXT)"""

cursor.execute(com1)

com2 = """CREATE TABLE IF NOT EXISTS
indkøb(indkøb_id INTEGER PRIMARY KEY, butik_id INTEGER, total FLOAT,
FOREIGN KEY(butik_id) REFERENCES butik(butik_id))"""

cursor.execute(com2)

# - 2. Indsæt rækker i tabellerne -
cursor.execute("INSERT INTO butik VALUES(5, 'Kolding')")
cursor.execute("INSERT INTO butik VALUES(7, 'Middelfart')")
cursor.execute("INSERT INTO butik VALUES(10, 'Odense')")

cursor.execute("INSERT INTO indkøb(indkøb_id, butik_id, total) VALUES(1, 7, 1029.95)")
cursor.execute("INSERT INTO indkøb(indkøb_id, butik_id, total) VALUES(2, 10, 599.90)")

cursor.execute("SELECT * FROM indkøb")
results = cursor.fetchall()
print(results)

# - 3. Udvælg fra tabellerne -

# - 4. Opdater i tabellerne
cursor.execute("UPDATE indkøb SET total = 2000.00 WHERE indkøb_id = 1")
cursor.execute("SELECT * FROM indkøb")
results2 = cursor.fetchall()
print(results2)


# - 5. Slet i tabellerne
cursor.execute("DELETE FROM butik WHERE butik_id = 7")
cursor.execute("SELECT * FROM butik")
results3 = cursor.fetchall()
print(results3)


#-------------------------
#--------Opgave-----------
#-------------------------

com3 = """CREATE TABLE IF NOT EXISTS
medlemskab(medlemskab_id TEXT PRIMARY KEY, pris_id FLOAT)"""
cursor.execute(com3)

cursor.execute("INSERT INTO medlemskab VALUES('Senior', 600)")
cursor.execute("INSERT INTO medlemskab VALUES('Junior', 300)")
cursor.execute("INSERT INTO medlemskab VALUES('Passiv', 50)")


#-------------------------------------------------------------

com4 = """CREATE TABLE IF NOT EXISTS
location(postnummer INTEGER PRIMARY KEY, by TEXT)"""
cursor.execute(com3)

cursor.execute("INSERT INTO location VALUES(6000, 'Kolding')")
cursor.execute("INSERT INTO location VALUES(7000, 'Fredercia')")
cursor.execute("INSERT INTO location VALUES(5500, 'Middelfart')")
cursor.execute("INSERT INTO location VALUES(6070, 'Christiansfeld')")

#-------------------------------------------------------------

com4 = """CREATE TABLE IF NOT EXISTS
navn(fornavn TEXT PRIMARY KEY, efternavn TEXT)"""
cursor.execute(com4)

cursor.execute("INSERT INTO navn VALUES('Søren', 'Sten')")
cursor.execute("INSERT INTO navn VALUES('Karen', 'Kost')")
cursor.execute("INSERT INTO navn VALUES('Benny', 'Bullseye')")
cursor.execute("INSERT INTO navn VALUES('Hanne', 'Hus')")