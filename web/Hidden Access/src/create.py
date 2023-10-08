import sqlite3

connection = sqlite3.connect("user_data.db")
cursor = connection.cursor()


cursor.execute("INSERT INTO users VALUES ('Hacker', 'password')")

connection.commit()
