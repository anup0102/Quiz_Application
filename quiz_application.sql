create database quiz_application;

CREATE TABLE users (
    uid INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    name varchar(50),
    age INT,
    score INT
    quizid int,
    foreign key (quizid) references quiz(qid)
);

CREATE TABLE quiz(
    qid INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    topic varchar(50),
    difficulty int,
);

CREATE TABLE questions(
    qid INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    question varchar(200),
    answer varchar(50),
    quizid int,
    foreign key (quizid) references quiz(qid)
);

CREATE TABLE options(
    oid INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    option varchar(50),
    questionid int,
    foreign key (questionid) references questions(qid)
);