import psycopg2

# Connect to "chinook" database
connection = psycopg2.connect(database="chinook")

# Build a cursor object of the database
cursor = connection.cursor()

# Query 1 - select all records from the "Artist" table
# cursor.execute('SELECT * FROM "Artist"')

# Query 2 - select only the "Name" columns from the "Artist" table
# cursor.execute('SELECT "Name" FROM "Artist"')

# Query 3 - select only "Queen" from the "Artist" table
# cursor.execute('SELECT * FROM "Artist" WHERE "Name" = %s', ["Queen"])

# Query 4 - select only by "ArtistId" number 51 from the "Artist" table
# cursor.execute('SELECT * FROM "Artist" WHERE "ArtistId" = %s', [51])

# Query 5 - select only the albums with "ArtistId" number 51 from the "Album" 
# table
# cursor.execute('SELECT * FROM "Album" WHERE "ArtistId" = %s', [51])

# Query 6 - select all tracks where the composer is "Queen" from the "Track"
# table
# cursor.execute('SELECT * FROM "Track" WHERE "Composer" = %s', ["Queen"])

# Query 7 - select only the albums with "ArtistId" number 8 from the "Album"
# table
cursor.execute('SELECT * FROM "Album" WHERE "ArtistId" = %s', [8])

# Query 8 - select all tracks where the composer is "test" from the "Album"
# table, which will return nothing
cursor.execute('SELECT * FROM "Track" WHERE "Composer" = %s', ["test"])

# Fetch the results (multiple)
results = cursor.fetchall()

# Fetch the result (single)
# results = cursor.fetchone()

# Close the connection
connection.close()

# Print the results
for result in results:
    print(result)
