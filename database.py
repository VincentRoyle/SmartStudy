import sqlite3


connection = sqlite3.connect("smartstudy.db")

cursor = connection.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS flashcards (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        question TEXT NOT NULL,
        answer TEXT NOT NULL,
        topic TEXT NOT NULL,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
""")

cursor.execute("""
    CREATE TABLE IF NOT EXISTS study_attempts (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        flashcard_id INTEGER NOT NULL,
        correct INTEGER NOT NULL,
        studied_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (flashcard_id) REFERENCES flashcards(id)
    )
""")

connection.commit()
connection.close()

print("Database created successfully.")