import sqlite3

#connect to database
conn = sqlite3.connect('movies.db')

#create a cursor
c = conn.cursor()

#creating a table
c.execute("""CREATE TABLE movies (
        name text,
        actor text,
        actress text,
        director text,
        year_of_release integer
    )""")

#moviedata list
movies_data =   [
                ('War','Hritik','Priya','Arunkapoor',2019),
                ('War 2','Hritik','Priya','Arunkapoor',2021),
                ('Maanadu','Simbu','Kalyani','Venkat',2021),
                ('Karnan','Dhanush','Rajashi','Mari Selvaraj',2019),
                ]

#insert a table
c.executemany("INSERT INTO movies VALUES(?,?,?,?,?)",movies_data)

#reterive table data
c.execute("SELECT * FROM movies")
query1 = c.fetchall()

#SELECT statement to query all rows from the Movies table,
for i in query1:
    print(i)
print("----------------------------------------------------------")

#use a query with parameter like actor name to select movies based on the actor's name.
c.execute("SELECT * FROM movies WHERE actor LIKE 'Hr%' ")
query2 = c.fetchall()

for i in query2:
    print(i)
print("----------------------------------------------------------")

#commit our command
conn.commit()

#close our conncetion
conn.close()



