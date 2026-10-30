from flask import Flask, request, redirect, render_template, session
from lib.book_repository import BookRepository
from lib.book import Book
from lib.user_repository import UserRepository
from lib.user import User
from lib.database_connection import DatabaseConnection
from lib.film_repository import FilmRepository
from lib.login_required import login_required

app = Flask(__name__)

app.secret_key = "some_really_secret_key"

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
@login_required
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

@app.route('/sessions/new', methods = ["GET"])
def get_sign_in():
    return render_template("login_form.html")

@app.route('/sessions/new', methods=["POST"])
def sign_in():
    connection = DatabaseConnection()
    connection.connect()
    user_repository = UserRepository(connection)
    username = request.form["username"]
    password = request.form["password"]
    user = user_repository.find_by_username(username)
    if user and user.password == password:
        session["user_id"] = user.id
        session["username"] = username
        return redirect("/books")
    else:
        return redirect("/sessions/new")

@app.route('/films', methods=["GET"])
def get_films():
    connection = DatabaseConnection()
    connection.connect()
    film_repository = FilmRepository(connection)
    films = film_repository.all()
    return render_template("films.html", films=films)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001, debug=True)
