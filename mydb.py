import mysql.connector

# Connect to MySQL Server
dataBase = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='Govardhan123@'
)

# Create a cursor object
cursorObject = dataBase.cursor()

# Check if database exists before creating
cursorObject.execute("CREATE DATABASE IF NOT EXISTS elderco")

print('Database created successfully!')

# Close the connection
dataBase.close()
