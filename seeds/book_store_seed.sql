DROP TABLE IF EXISTS books CASCADE;
DROP TABLE IF EXISTS users CASCADE;
DROP TABLE IF EXISTS films CASCADE;

CREATE TABLE books (
    id SERIAL PRIMARY KEY,
    title TEXT,
    author TEXT,
    synopsis TEXT,
    star_rating INT
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

INSERT INTO books (title, author, synopsis, star_rating) VALUES ('The Gruffalo', 'Julia Donaldson', 'A clever mouse invents a terrifying monster called the Gruffalo to scare off the predators in the woods, only to meet the real thing and have to outwit it too.', 5);
INSERT INTO books (title, author, synopsis, star_rating) VALUES ('Ada Twist, Scientist', 'Andrea Beaty', 'Ada, an endlessly curious young girl, drives her family to distraction with constant experiments and questions as she tries to figure out how the world works.', 4);
INSERT INTO books (title, author, synopsis, star_rating) VALUES ('The Girl Who Drank the Moon', 'Kelly Barnhill', 'A witch accidentally feeds an abandoned baby moonlight instead of starlight, filling her with powerful magic that she must learn to control as she grows up.', 2);
INSERT INTO books (title, author, synopsis, star_rating) VALUES ('Dragons in a Bag', 'Zetta Elliott', 'A boy named Jake is sent to spend the day with a mysterious woman who turns out to be a witch, and he’s tasked with delivering baby dragons from her bag to a magical world.', 5);

INSERT INTO users (username, password) VALUES ('tony29', 'tonypassword');
INSERT INTO users (username, password) VALUES ('laura85', 'laurapassword');
INSERT INTO users (username, password) VALUES ('geralt666', 'geraltpassword');

INSERT INTO films (title, release_year, director) VALUES ('Alien', 1979, 'Scott, Ridley');
INSERT INTO films (title, release_year, director) VALUES ('Braveheart', 1995, 'Gibson, Mel');
INSERT INTO films (title, release_year, director) VALUES ('2001: A Space Oddysey', 1968, 'Kubrick, Stanley');
INSERT INTO films (title, release_year, director) VALUES ('Blade Runner', 1982, 'Scott, Ridley');