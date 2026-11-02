import sys
import os
from playwright.sync_api import Page, expect
from lib.database_connection import DatabaseConnection

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from app import app

def test_get_books_returns_200():
    client = app.test_client()
    response = client.get("/books")
    assert response.status_code == 200

def test_get_books_returns_all_books():
    client = app.test_client()
    response = client.get("/books")
    assert response.content_type.startswith("text/html")

def test_get_authors_returns_200():
    client = app.test_client()
    response = client.get("/authors")
    assert response.status_code == 200

def test_get_authors_returns_list_of_authors():
    client = app.test_client()
    response = client.get('/authors')
    assert response.json == ["Julia Donaldson", "Andrea Beaty", "Kelly Barnhill", "Zetta Elliott"]

def test_has_title(page: Page):
    page.goto("http://127.0.0.1:5001")
    h1 = page.locator("h1")
    expect(h1).to_have_text("Welcome to AceReads!")

def test_book_content_correct(page: Page, db_connection):
    db_connection.seed("seeds/book_store_seed.sql")
    page.goto("http://127.0.0.1:5001/books")
    books = page.locator("li")
    expected_books = [
        "The Gruffalo by Julia Donaldson\nA clever mouse invents a terrifying monster called the Gruffalo to scare off the predators in the woods, only to meet the real thing and have to outwit it too.\n5/5 Stars",
        "Ada Twist, Scientist by Andrea Beaty\nAda, an endlessly curious young girl, drives her family to distraction with constant experiments and questions as she tries to figure out how the world works.\n4/5 Stars",
        "The Girl Who Drank the Moon by Kelly Barnhill\nA witch accidentally feeds an abandoned baby moonlight instead of starlight, filling her with powerful magic that she must learn to control as she grows up.\n2/5 Stars",
        "Dragons in a Bag by Zetta Elliott\nA boy named Jake is sent to spend the day with a mysterious woman who turns out to be a witch, and he’s tasked with delivering baby dragons from her bag to a magical world.\n5/5 Stars"
    ]
    actual_books = books.all_inner_texts()
    assert actual_books == expected_books

def test_create_new_book(page: Page):
    connection = DatabaseConnection()
    connection.connect()
    connection.execute("TRUNCATE TABLE users;")
    connection.execute("INSERT INTO users (username, password) values ('test', '1234');")
    page.goto("http://localhost:5001/sessions/new")
    page.locator("#username").fill("test")
    page.locator("#password").fill("1234")
    page.get_by_role("button").click()
    expect(page).to_have_url("http://localhost:5001/books")
    page.goto("http://localhost:5001/books/add_book")
    page.locator("#title").fill("The Chroicles of Geronimo (the cat)")
    page.locator("#author").fill("Geronimo")
    page.locator("#synopsis").fill("A hungry street dog follows a cat home, decides to live as one of the family’s cats, and has to rescue the kittens when they’re cat-napped at a pet show if he wants to be allowed to stay.")
    page.locator("#star_rating").fill("3")
    page.get_by_role("button", name="Submit").click()
    expect(page.locator("li").last).to_have_text(
        "The Chroicles of Geronimo (the cat) by Geronimo\nA hungry street dog follows a cat home, decides to live as one of the family’s cats, and has to rescue the kittens when they’re cat-napped at a pet show if he wants to be allowed to stay.\n3/5 Stars"
        )

def test_film_content_correct(page: Page, db_connection):
    db_connection.seed("seeds/book_store_seed.sql")
    page.goto("http://127.0.0.1:5001/films")
    films = page.locator("li")
    expected_films = [
        'Alien, 1979 by Scott, Ridley',                   
        'Braveheart, 1995 by Gibson, Mel',             
        '2001: A Space Oddysey, 1968 by Kubrick, Stanley',
        'Blade Runner, 1982 by Scott, Ridley'            
    ]
    actual_films = films.all_inner_texts()
    assert actual_films == expected_films

def test_find_book_route_shows_correct_page(page: Page, db_connection):
    db_connection.seed("seeds/book_store_seed.sql")
    page.goto("http://127.0.0.1:5001/books/1")
    books = page.locator("li")
    expected_books = [
        "The Gruffalo by Julia Donaldson\nA clever mouse invents a terrifying monster called the Gruffalo to scare off the predators in the woods, only to meet the real thing and have to outwit it too.\n5/5 Stars"
    ]
    actual_books = books.all_inner_texts()
    assert actual_books == expected_books

def test_find_book_with_incorrect_id_shows_404(page: Page, db_connection):
    page.goto("http://127.0.0.1:5001/books/10")
    h2 = page.locator("h2")
    expect(h2).to_have_text("404")