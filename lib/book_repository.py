from lib.book import Book

class BookRepository:
    def __init__(self, connection):
        self._connection = connection

    def all(self):
        rows = self._connection.execute('SELECT * from books')
        books = []
        for row in rows:
            item = Book(row["title"], row["author"], row["id"])
            books.append(item)
        return books

    # # Find a single book by their id
    # def find(self, book_id):
    #     rows = self._connection.execute(
    #         'SELECT * from books WHERE id = %s', [book_id])
    #     row = rows[0]
    #     return book(row["id"], row["name"], row["genre"])

    def create(self, book):
        self._connection.execute(
            'INSERT INTO books (title, author) VALUES (%s, %s)',
            [book.title, book.author]
        )
        return None

    # # Delete an book by their id
    # def delete(self, book_id):
    #     self._connection.execute(
    #         'DELETE FROM books WHERE id = %s', [book_id])
    #     return None