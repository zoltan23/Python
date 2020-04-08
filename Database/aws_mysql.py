import pandas as pd
import pymysql
import aws_credentials as aws



conn = pymysql.connect(aws.host, user=aws.user,port=aws.port,
                            passwd=aws.password, db=aws.dbname)

cursorObject = conn.cursor()    

cursorObject.execute("SHOW tables")

output = cursorObject.fetchall()


#Create the players table if it does not already exists
if any('players' in str_ for str_ in output) == False:
    print('no players')
    createTableQuery = "CREATE TABLE players(id int NOT NULL, LastName varchar(32), FirstName varchar(32))"
    cursorObject.execute(createTableQuery)
else: 
    print('The players table was already created')

#Seed the table
sqlQuery = "INSERT INTO players (FirstName, LastName) VALUES ('Joe', 'Burrow')"
cursorObject.execute(sqlQuery)

#Confirm the table was seeded
sqlQuery = "SELECT * FROM players"
cursorObject.execute(sqlQuery)

output = cursorObject.fetchall()
print(output)