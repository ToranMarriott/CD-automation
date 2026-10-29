from flask import Flask, render_template, request, redirect
from lib.book_repository import BookRepository
from lib.book import Book
from lib.user_repository import UserRepository
from lib.user import User
from lib.database_connection import DatabaseConnection

app = Flask(__name__)

@app.route("/", methods=['GET'])
def index():
    return render_template("index.html")

@app.route('/books', methods=['GET'])
def get_books():
    connection = DatabaseConnection()
    connection.connect()
    book_repository = BookRepository(connection)
    books = book_repository.all()
    return render_template("books.html", books=books)

@app.route('/books', methods=['POST'])
def create_book():
    connection = DatabaseConnection()
    connection.connect()
    book_repository = BookRepository(connection)
    book_details = request.form
    book = Book(title=book_details["title"], author=book_details["author"])
    book_repository.create(book)
    return redirect("/books")

@app.route('/authors', methods=['GET'])
def get_authors():
    return ["Julia Donaldson", "Andrea Beaty", "Kelly Barnhill", "Zetta Elliott"]

@app.route('/team', methods=['GET'])
def get_team():
    team = ["Dorothy", "Rose", "Blanche", "Sophia"]
    return render_template("team.html", team=team)

@app.route('/signup', methods=['GET'])
def get_signup():
    return render_template("signup_form.html")

@app.route('/signup', methods=['POST'])
def create_user():
    connection = DatabaseConnection()
    connection.connect()
    user_repository = UserRepository(connection)
    user_details = request.form
    user = User(username=user_details["username"], password=user_details["password"])
    user_repository.create(user)
    return redirect("/signup")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001, debug=True)
