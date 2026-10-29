TRUNCATE TABLE books RESTART IDENTITY;

INSERT INTO books (title, author) VALUES ('The Gruffalo', 'Julia Donaldson');
INSERT INTO books (title, author) VALUES ('Ada Twist, Scientist', 'Andrea Beaty');
INSERT INTO books (title, author) VALUES ('The Girl Who Drank the Moon', 'Kelly Barnhill');
INSERT INTO books (title, author) VALUES ('Dragons in a Bag', 'Zetta Elliott');

TRUNCATE TABLE users RESTART IDENTITY;

INSERT INTO users (username, password) VALUES ('tony29', 'tonypassword');
INSERT INTO users (username, password) VALUES ('laura85', 'laurapassword');
INSERT INTO users (username, password) VALUES ('geralt666', 'geraltpassword');