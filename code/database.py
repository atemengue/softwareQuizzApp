import sqlite3

CREATE_TABLE_GAME = """
CREATE TABLE IF NOT EXISTS game (
   idGame INTEGER PRIMARY KEY AUTOINCREMENT,
   score INTEGER,
   date TIMESTAMP,
   userIdUser INTEGER
);
"""

CREATE_TABLE_LECTURE = """
CREATE TABLE IF NOT EXISTS lectures (
    idLecture INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT,
    description TEXT,
    date TIMESTAMP
);
"""

CREATE_TABLE_QUESTION = """
CREATE TABLE IF NOT EXISTS questions (
    idGame INTEGER PRIMARY KEY AUTOINCREMENT,
    description TEXT
    date TIMESTAMP
);
"""

CREATE_TABLE_RESPONSE = """
CREATE TABLE IF NOT EXISTS responses (
    idQuestion INTEGER PRIMARY KEY AUTOINCREMENT,
    description TEXT,
    state INT,
    date TIMESTAMP
);
"""

CREATE_TABLE_USER = """
CREATE TABLE IF NOT EXISTS users (
    idUser INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    date TIMESTAMP
);
"""
if __name__ == "__main__":
    database = sqlite3.connect("quizz.db")
    cursor = database.cursor()
    cursor.execute(CREATE_TABLE_GAME)
    cursor.execute(CREATE_TABLE_LECTURE)
    cursor.execute(CREATE_TABLE_QUESTION)
    cursor.execute(CREATE_TABLE_RESPONSE)
    cursor.execute(CREATE_TABLE_USER)