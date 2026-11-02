from lib.book_repository import BookRepository
from lib.book import Book

def test_all(db_connection):
    db_connection.seed("seeds/book_store_seed.sql")
    repo = BookRepository(db_connection)
    assert repo.all() == [
        Book('The Gruffalo', 'Julia Donaldson', 'A clever mouse invents a terrifying monster called the Gruffalo to scare off the predators in the woods, only to meet the real thing and have to outwit it too.', 5, 1),
        Book('Ada Twist, Scientist', 'Andrea Beaty', 'Ada, an endlessly curious young girl, drives her family to distraction with constant experiments and questions as she tries to figure out how the world works.', 4, 2),
        Book('The Girl Who Drank the Moon', 'Kelly Barnhill', 'A witch accidentally feeds an abandoned baby moonlight instead of starlight, filling her with powerful magic that she must learn to control as she grows up.', 2, 3),
        Book('Dragons in a Bag', 'Zetta Elliott', 'A boy named Jake is sent to spend the day with a mysterious woman who turns out to be a witch, and he’s tasked with delivering baby dragons from her bag to a magical world.', 5, 4)
    ]


def test_create(db_connection):
    db_connection.seed("seeds/book_store_seed.sql")
    repo = BookRepository(db_connection)
    book = Book("Dog Man", "Dav Pilkey", "After a police officer and his police dog are both badly injured in an explosion, surgeons sew the dog’s head onto the officer’s body, creating Dog Man, a crime-fighting hybrid who takes on the evil cat Petey.", 5, None)
    repo.create(book)
    assert repo.all() == [
        Book('The Gruffalo', 'Julia Donaldson', 'A clever mouse invents a terrifying monster called the Gruffalo to scare off the predators in the woods, only to meet the real thing and have to outwit it too.', 5, 1),
        Book('Ada Twist, Scientist', 'Andrea Beaty', 'Ada, an endlessly curious young girl, drives her family to distraction with constant experiments and questions as she tries to figure out how the world works.', 4, 2),
        Book('The Girl Who Drank the Moon', 'Kelly Barnhill', 'A witch accidentally feeds an abandoned baby moonlight instead of starlight, filling her with powerful magic that she must learn to control as she grows up.', 2, 3),
        Book('Dragons in a Bag', 'Zetta Elliott', 'A boy named Jake is sent to spend the day with a mysterious woman who turns out to be a witch, and he’s tasked with delivering baby dragons from her bag to a magical world.', 5, 4),
        Book('Dog Man', 'Dav Pilkey', 'After a police officer and his police dog are both badly injured in an explosion, surgeons sew the dog’s head onto the officer’s body, creating Dog Man, a crime-fighting hybrid who takes on the evil cat Petey.' ,5 ,5)
    ]

def test_find_by_id(db_connection):
    db_connection.seed("seeds/book_store_seed.sql")
    repo = BookRepository(db_connection)
    assert repo.find(1) == Book('The Gruffalo', 'Julia Donaldson', 'A clever mouse invents a terrifying monster called the Gruffalo to scare off the predators in the woods, only to meet the real thing and have to outwit it too.', 5, 1)

def test_find_incorrect_id_returns_false(db_connection):
    db_connection.seed("seeds/book_store_seed.sql")
    repo = BookRepository(db_connection)
    assert repo.find(10) == None