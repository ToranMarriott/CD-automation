class Book:
    def __init__(self, title, author, synopsis, star_rating, id=None):
        self.id = id
        self.title = title
        self.author = author
        self.synopsis = synopsis
        self.star_rating = star_rating

    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    def __repr__(self):
        return f"Book({self.id}, {self.title}, {self.author}, {self.synopsis}, {self.star_rating})"