import psycopg2

# Connect to "chinook" database
connection = psycopg2.connect(database="chinook")

# Build a cursor object of the database
cursor = connection.cursor()

# Query 1 - select all records from the "Artist" table
cursor.execute('SELECT * FROM "Artist"')

# Fetch the results (multiple)
results = cursor.fetchall()

# Fetch the result (single)
# results = cursor.fetchone()

# Close the connection
connection.close()

# Print the results
for result in results:
    print(result)
