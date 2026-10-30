from lib.film import Film

def test_film_instantiates_with_properties():
    film = Film(1, 'Alien', 1979, 'Scott, Ridley')
    assert film.id == 1
    assert film.title == "Alien"
    assert film.release_year == 1979
    assert film.director == "Scott, Ridley"

def test_equality():
    film1 = Film(1, 'Alien', 1979, 'Scott, Ridley')
    film2 = Film(1, 'Alien', 1979, 'Scott, Ridley')
    assert film1 == film2

def test_formats_nicely():
    film = Film(1, 'Alien', 1979, 'Scott, Ridley')
    assert str(film) == "Film(1, Alien, 1979, Scott, Ridley)"