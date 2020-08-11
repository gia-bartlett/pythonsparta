from database_connection_start import database_connect

server = "databases2.spartaglobal.academy"
database = "Northwind"
username = "SA"
password = "Passw0rd2018"


#user_input = int(input("Please enter the number for the operation you want to execute: "
                    #"\n 1. Fetch one row \n 2. Fetch many rows \n 3. Fetch ALL rows \n"))




connection = database.establish_connection()
print(connection)

database.fetch_results('SELECT * FROM Products', connection, user_input)
average_unitp = database.avg('UnitPrice', connection)
