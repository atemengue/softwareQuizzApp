CREATE TABLE IF NOT EXISTS game (
   idGame INTEGER PRIMARY KEY AUTOINCREMENT,
   score INTEGER,
   userIdUser INTEGER,
   date TIMESTAMP,
   FOREIGN KEY (userIdUser) REFERENCES users(idUser)
);

CREATE TABLE IF NOT EXISTS lectures (
    idLecture INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT,
    description TEXT,
    date TIMESTAMP
);

CREATE TABLE IF NOT EXISTS questions (
    idGame INTEGER PRIMARY KEY AUTOINCREMENT,
    description TEXT,
    lectureIdLecture INTEGER,
    date TIMESTAMP,
    FOREIGN KEY (lectureIdLecture) REFERENCES lectures(idLecture)
);

CREATE TABLE IF NOT EXISTS responses (
    idQuestion INTEGER PRIMARY KEY AUTOINCREMENT,
    description TEXT,
    state INT,
    questionIdQuestion INTEGER,
    date TIMESTAMP,
    FOREIGN KEY (questionIdQuestion) REFERENCES questions(idQuestion)
);

CREATE TABLE IF NOT EXISTS users (
    idUser INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    date TIMESTAMP
);