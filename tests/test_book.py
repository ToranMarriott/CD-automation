from lib.book import Book

def test_book_instantiates_with_properties():
    book = Book("The Gruffalo", "Julia Donaldson", 'A clever mouse invents a terrifying monster called the Gruffalo to scare off the predators in the woods, only to meet the real thing and have to outwit it too.', 5, 1)
    assert book.id == 1
    assert book.title == "The Gruffalo"
    assert book.author == "Julia Donaldson"
    assert book.synopsis == "A clever mouse invents a terrifying monster called the Gruffalo to scare off the predators in the woods, only to meet the real thing and have to outwit it too."
    assert book.star_rating == 5

def test_equality():
    book1 = Book("The Gruffalo", "Julia Donaldson", 'A clever mouse invents a terrifying monster called the Gruffalo to scare off the predators in the woods, only to meet the real thing and have to outwit it too.', 5, 1)
    book2 = Book("The Gruffalo", "Julia Donaldson", 'A clever mouse invents a terrifying monster called the Gruffalo to scare off the predators in the woods, only to meet the real thing and have to outwit it too.', 5, 1)
    assert book1 == book2

def test_formats_nicely():
    book = Book("The Gruffalo", "Julia Donaldson", 'A clever mouse invents a terrifying monster called the Gruffalo to scare off the predators in the woods, only to meet the real thing and have to outwit it too.', 5, 1)
    assert str(book) == "Book(1, The Gruffalo, Julia Donaldson, A clever mouse invents a terrifying monster called the Gruffalo to scare off the predators in the woods, only to meet the real thing and have to outwit it too., 5)"