import sqlite3

# Create SQLite database and table
conn = sqlite3.connect('blood_bank.db')
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS donors (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        blood_type TEXT NOT NULL
    );
''')

conn.commit()
conn.close()

print("Database and table created successfully!")
