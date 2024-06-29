-- SQL CREATE TABLE ---
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
    idQuestion INTEGER PRIMARY KEY AUTOINCREMENT,
    description TEXT,
    explanation TEXT,
    lectureIdLecture INTEGER,
    date TIMESTAMP,
    FOREIGN KEY (lectureIdLecture) REFERENCES lectures(idLecture)
);

CREATE TABLE IF NOT EXISTS responses (
    idResponse INTEGER PRIMARY KEY AUTOINCREMENT,
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

-- SQL SCRIPTS USERS ---
INSERT INTO users (name, date)
VALUES("regis", DATE('now'));


-- SQL SCRIPT ADD LECTURE
INSERT INTO lectures (title, description, date)
VALUES
("Fundamentals of Software Engineering", "This is Software Engineering Course Lecturer", DATE('now')),
("Software Algorithms", "This is software Algorithms Lecturer", DATE('now')),
("Software Testing", "This is software testing Lecture", DATE('now'))

-- SQL SCRIPT ADD QUESTIONS
-- Question 1:
INSERT INTO questions (description, lectureIdLecture, date)
VALUES("What is the main goal of software testing?", 1, DATE('now'));


-- Question 2:
INSERT INTO questions (description, lectureIdLecture, date)
VALUES("What type of testing involves testing individual components of the software in isolation?", 1, DATE('now'));

-- Question 3:
INSERT INTO questions (description, lectureIdLecture, date)
VALUES("Which testing technique involves running the system under a controlled environment to ensure it meets specified requirements?", 1, DATE('now

-- SQL SCRIPT ADD MANY RESPONSES OF ONE QUESTION
INSERT INTO responses (description, state, questionIdQuestion, date)
VALUES
("To ensure the software performs as expected and to identify defects.", 1, 1, DATE('NOW')),
("To write the software code", 0, 1, DATE('NOW')),
("To design the Software architecture", 0, 1, DATE('now'));

-- SELECT RESPONSES
SELECT * FROM responses;

-- SELECT QUESTIONS
SELECT * FROM questions;

-- SELECT RESPONSES AND QUESTIONS (THIS IS JOINTURE)
SELECT
     responses.idResponse as idResponse,
     responses.description as description,
     responses.state as state,
     questions.idQuestion as idQuestion,
     questions.description as titleQuestion,
FROM responses
INNER JOIN questions ON responses.questionIdQuestion = questions.idQuestion

--- SELECT ALL QUESTIONS
SELECT  *
FROM  questions;

-- SELECT ALL RESPONSES OF ONE QUESTION (THIS IS JOINTURE)
SELECT
     responses.idResponse as idResponse,
     responses.description as description,
     responses.state as state,
     questions.idQuestion as idQuestion,
     questions.description as titleQuestion
FROM responses
INNER JOIN questions ON responses.questionIdQuestion = questions.idQuestion
WHERE idQuestion = 2


--- SELECT ID PLAYER
SELECT
    idUser
FROM users
WHERE name = 'regis'

-- SELECT ONE QUESTION
SELECT
     responses.idResponse as idResponse,
     responses.description as description,
     responses.state as state,
     questions.idQuestion as idQuestion,
     questions.description as titleQuestion
FROM responses
INNER JOIN questions ON responses.questionIdQuestion = questions.idQuestion
WHERE idQuestion = 3
