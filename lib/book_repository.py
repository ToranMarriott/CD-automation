from lib.book import Book

class BookRepository:
    def __init__(self, connection):
        self._connection = connection

    def all(self):
        rows = self._connection.execute('SELECT * from books')
        books = []
        for row in rows:
            item = Book(row["title"], row["author"], row["synopsis"], row["star_rating"] ,row["id"])
            books.append(item)
        return books

    def find(self, book_id):
        rows = self._connection.execute(
            'SELECT * from books WHERE id = %s', [book_id])
        if rows:
            row = rows[0]
            return Book(row["title"], row["author"], row["synopsis"], row["star_rating"] ,row["id"])
        else: 
            return None

    def create(self, book):
        self._connection.execute(
            'INSERT INTO books (title, author, synopsis, star_rating) VALUES (%s, %s, %s, %s)',
            [book.title, book.author, book.synopsis, book.star_rating]
        )
        return None

    # # Delete an book by their id
    # def delete(self, book_id):
    #     self._connection.execute(
    #         'DELETE FROM books WHERE id = %s', [book_id])
    #     return None