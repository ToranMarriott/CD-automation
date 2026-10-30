DROP TABLE IF EXISTS books CASCADE;
DROP TABLE IF EXISTS users CASCADE;
DROP TABLE IF EXISTS films CASCADE;

CREATE TABLE books (
    id SERIAL PRIMARY KEY,
    title TEXT,
    author TEXT
);

CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    username VARCHAR(255),
    password VARCHAR(255)
);

CREATE TABLE films (
    id SERIAL PRIMARY KEY,
    title TEXT,
    release_year INT,
    director TEXT
);

INSERT INTO books (title, author) VALUES ('The Gruffalo', 'Julia Donaldson');
INSERT INTO books (title, author) VALUES ('Ada Twist, Scientist', 'Andrea Beaty');
INSERT INTO books (title, author) VALUES ('The Girl Who Drank the Moon', 'Kelly Barnhill');
INSERT INTO books (title, author) VALUES ('Dragons in a Bag', 'Zetta Elliott');

INSERT INTO users (username, password) VALUES ('tony29', 'tonypassword');
INSERT INTO users (username, password) VALUES ('laura85', 'laurapassword');
INSERT INTO users (username, password) VALUES ('geralt666', 'geraltpassword');

INSERT INTO films (title, release_year, director) VALUES ('Alien', 1979, 'Scott, Ridley');
INSERT INTO films (title, release_year, director) VALUES ('Braveheart', 1995, 'Gibson, Mel');
INSERT INTO films (title, release_year, director) VALUES ('2001: A Space Oddysey', 1968, 'Kubrick, Stanley');
INSERT INTO films (title, release_year, director) VALUES ('Blade Runner', 1982, 'Scott, Ridley');