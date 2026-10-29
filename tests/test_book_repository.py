from lib.book_repository import BookRepository
from lib.book import Book

def test_all(db_connection):
    db_connection.seed("seeds/book_store_seed.sql")
    repo = BookRepository(db_connection)
    assert repo.all() == [
        Book('The Gruffalo', 'Julia Donaldson', 1),
        Book('Ada Twist, Scientist', 'Andrea Beaty', 2),
        Book('The Girl Who Drank the Moon', 'Kelly Barnhill', 3),
        Book('Dragons in a Bag', 'Zetta Elliott', 4)
    ]

def test_create(db_connection):
    db_connection.seed("seeds/book_store_seed.sql")
    repo = BookRepository(db_connection)
    book = Book("Dog Man", "Dav Pilkey", None)
    repo.create(book)
    assert repo.all() == [
        Book('The Gruffalo', 'Julia Donaldson', 1),
        Book('Ada Twist, Scientist', 'Andrea Beaty', 2),
        Book('The Girl Who Drank the Moon', 'Kelly Barnhill', 3),
        Book('Dragons in a Bag', 'Zetta Elliott', 4),
        Book('Dog Man', 'Dav Pilkey', 5)
    ]