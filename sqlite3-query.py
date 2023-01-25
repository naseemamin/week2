import sqlite3
from faker import Faker

#generate names for sample.db
fake = Faker()
names = [fake.name().split() for i in range(100)]
names = [name for name in names if len(name) == 2]
print(names)

connection = sqlite3.connect("sample.db")

insert_query = 'INSERT INTO people(name, surname) VALUES(?, ?)'
cursor = connection.cursor()
for name in names:
    cursor.execute(insert_query, name)
connection.commit()

select_query = 'SELECT * from people LIMIT 10'
for i in cursor.execute(select_query):
    print(i)
    
query = 'SELECT name, surname FROM people WHERE name="James" ORDER BY name DESC'
for result in cursor.execute(query):
    print(result)

query_splitname = 'SELECT name, surname FROM people LIMIT 10'
for result in cursor.execute(query_splitname):
    print(f"First Name: {result[0]}, Last Name: {result[1]}")

#% is a like a wildcard, useful for searching / filtering data.
query_percent = 'SELECT name, surname FROM people WHERE name LIKE "%es___%"'
print("querying using percent symbol: ")
for result in cursor.execute(query_percent):
    print(f"First Name: {result[0]}, Last Name: {result[1]}")
