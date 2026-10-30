from lib.film_repository import FilmRepository
from lib.film import Film

def test_all(db_connection):
    db_connection.seed("seeds/book_store_seed.sql")
    repo = FilmRepository(db_connection)
    assert repo.all() == [
        Film(1, 'Alien', 1979, 'Scott, Ridley'),
        Film(2, 'Braveheart', 1995, 'Gibson, Mel'),
        Film(3, '2001: A Space Oddysey', 1968, 'Kubrick, Stanley'),
        Film(4, 'Blade Runner', 1982, 'Scott, Ridley')
    ]