import pyodbc


#

# these are needed to establish a connection with the server
server = "databases2.spartaglobal.academy"
database = "Northwind"
username = "SA"
password = "Passw0rd2018"

# establishing connection: specifying the OBDC server
# cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=localhost;DATABASE=testdb;UID=me;PWD=pass')
# we paste in our server, database, username and password
cnxn = ('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+password)



# connection timing out is a common error so we put in an try block to catch it.
try:
    with pyodbc.connect(cnxn, timeout=5) as connection:
        print("Connection did not time out")
except:
    print("Connection Timed Out")
else:
    # acquire a cursor from a connection
    # execute the code through the cursor
    # fetch
    cursor = connection.cursor()
    print(connection)
    print(cursor)

query_result = cursor.execute('SELECT * FROM Products')
print("Printing query_result object: ", query_result)

# .fetchone() --> output 1 row - remember cursor maintains state
# if you want to get back to the start you need a new cursor or to run execute command again.

rows = query_result.fetchone()
print(type(rows))
print(rows[1]) # second column of rows starts a 0th index
print(rows.ProductName)

print("Executing FetchMany: ", query_result.fetchmany(30))  # returns in a list

rows = query_result.fetchmany(30)
for row in rows:
    print(row)
# looping through the rows and printing each row

rows = query_result.fetchall()

for row in rows:
    print("ProductName: ".ProductName, )
