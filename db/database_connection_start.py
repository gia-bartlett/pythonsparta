import pyodbc
import pandas as pd

class database_connect:  # create class to initialise the connection

    def __init__(self, server, database, username, password):
        self.server = server
        self.database = database
        self.username = username
        self.password = password

    def establish_connection(self):  # establish the connection
        cnxn = ('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+self.server+';DATABASE='+self.database+';UID='+self.username+';PWD='+self.password)
        # add try block for common connection timeout error
        try:
            with pyodbc.connect(cnxn, timeout=5) as connection:
                print("Connection did not time out")
        except:
            print("Connection Timed Out")
        else:
            return connection

    def create_cursor(self, connection):  # create a cursor
        return connection.cursor()


    def fetch_results(self, sql_command, connection, user_input):
        cursor = self.create_cursor(connection)
        query_result = cursor.execute(sql_command) #(SELECT * FROM PRODUCTS)
        try:
            if user_input == 1:
                self.fetch_one(query_result)
            elif user_input == 2:
                self.fetch_many(query_result)
            elif user_input == 3:
                self.fetch_all(query_result)
            #elif user_input == 4:
                #self.avg(query_result)
            else:
                raise ValueError

        except ValueError:
            print("This is incorrect user_input")

    def fetch_one(self, query):
        rows = query.fetchone()
        return (rows.ProductName)

    def fetch_many(self, query):
        rows = query.fetchmany(30)
        for row in rows:
            return ("Product Name: "+row.ProductName, "Costs: ", row.UnitPrice)

    def fetch_all(self, query):
        rows = query.fetchall()
        all_data = rows
        for row in rows:
            #all_data[row] = rows[row]
            print("ProductID: ", row.ProductID, "Product Name: "+row.ProductName, "Supplier: ", row.SupplierID, "CategoryID: ", row.CategoryID, "Quantity: ",row.QuantityPerUnit, "Costs: ", row.UnitPrice, "In Stock: ", row.UnitsInStock, "On Order: ", row.UnitsOnOrder, "Reorder: ", row.ReorderLevel, "Discontinued: ", row.Discontinued)
        return all_data

    def avg(self, field, connection):
        cnxn = self.establish_connection()
        query_result = pd.read_sql('SELECT AVG(' + field + ') AS Average FROM Products', cnxn)
        print(f"Average of {field} is {query_result}")     # print and return in case you want to use it down the line
        return pd.DataFrame(query_result[1])
    # query result = rows


