from flask import Flask, request, redirect, render_template, session, abort
from lib.book_repository import BookRepository
from lib.book import Book
from lib.user_repository import UserRepository
from lib.user import User
from lib.database_connection import DatabaseConnection
from lib.film_repository import FilmRepository
from lib.login_required import login_required
from flagsmith import Flagsmith
from dotenv import load_dotenv
import os

load_dotenv()

flagsmith = Flagsmith(
    environment_key=os.environ["FLAGSMITH_ENVIRONMENT_KEY"],
)

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
    book = Book(
        title=book_details["title"], 
        author=book_details["author"], 
        synopsis=book_details["synopsis"], 
        star_rating=book_details["star_rating"])
    book_repository.create(book)
    return redirect("/books")

@app.route('/authors', methods=['GET'])
def get_authors():
    return ["Julia Donaldson", "Andrea Beaty", "Kelly Barnhill", "Zetta Elliott"]

@app.route('/team', methods=['GET'])
def get_team():
    flags = flagsmith.get_environment_flags()
    team = ["Dorothy", "Rose", "Blanche", "Sophia"]
    if flags.is_feature_enabled("new_page"):
        return render_template("team_v2.html", team=team)
    else:
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
    flags = flagsmith.get_environment_flags()
    connection = DatabaseConnection()
    connection.connect()
    film_repository = FilmRepository(connection)
    films = film_repository.all()
    if flags.is_feature_enabled("film_page"):
        return render_template("films.html", films=films)
    else:
        abort(404)

@app.route('/books/add_book', methods=["GET"])
@login_required
def get_add_book_form():
    return render_template("add_book.html")

@app.route('/books/<id>', methods=["GET"])
def get_book_by_id(id):
    connection = DatabaseConnection()
    connection.connect()
    book_repository = BookRepository(connection)
    book = book_repository.find(id)
    if book:
        return render_template("books.html", books=[book])
    else:
        abort(404)

@app.errorhandler(404)
def handle_404_error(err):
    return render_template("404.html"), 404

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001, debug=True)
