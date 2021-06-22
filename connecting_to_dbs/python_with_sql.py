import sqlalchemy
from pprint import pprint
import pandas as pd

server = 'localhost,1433'
database = 'Northwind'
user = 'SA'
password = 'Passw0rd2018'
driver = 'SQL+Server'  # ODBC+Driver+17+for+

engine = sqlalchemy.create_engine(f"mssql+pyodbc://{user}:{password}"
                                   f"@{server}/{database}?driver={driver}")

# Open connection

connection = engine.connect()
query = "SELECT name FROM sys.tables;"
print(query)
# Once connection is open we can start to query

# result = engine.execute("SELECT * FROM Products;")
# print(result)  # <sqlalchemy.engine.cursor.LegacyCursorResult object at
# 0x03E58C40>
#
# first_row = result.fetchone()  # Just prints the first row
# print(first_row)
#
# for entry in result:  # loop for printing all results
#     print(entry)
#
# for entry in result:
#     as_dictionary = dict(entry)
#     print(as_dictionary)

# all_rows = result.fetchall()  # Fetch all results, not using loop
# print(list(result.keys()))  # Product keys too
# pprint(all_rows)  # Prints it nicely

# If fetchall is used after fetchone, fetchone will print independently of
# fetch all

# Giacomo's way
# query = 'SELECT * FROM Orders o JOIN [Order Details] od ON od.OrderID =
# o.OrderID'

# products = pd.read_sql(query, connection, index_col='ProductID')
# print(products)
