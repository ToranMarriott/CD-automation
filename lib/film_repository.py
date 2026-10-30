from lib.film import Film

class FilmRepository:
    def __init__(self, connection):
        self._connection = connection

    def all(self):
        rows = self._connection.execute('SELECT * from films')
        films = []
        for row in rows:
            item = Film(row["id"], row["title"], row["release_year"], row["director"])
            films.append(item)
        return films