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
        'The Gruffalo by Julia Donaldson',
        'Ada Twist, Scientist by Andrea Beaty',
        'The Girl Who Drank the Moon by Kelly Barnhill',
        'Dragons in a Bag by Zetta Elliott'
    ]
    actual_books = books.all_inner_texts()
    assert actual_books == expected_books

def test_form_submission_recieved(page: Page, db_connection):
    db_connection.seed("seeds/book_store_seed.sql")
    page.goto("http://127.0.0.1:5001/books")
    page.locator("#title").fill("The Chronicles of Geronimo (the cat)")
    page.locator("#author").fill("Geronimo")
    page.get_by_role("button", name="Submit").click()
    books = page.locator('li')
    new_book = books.all_inner_texts()[-1]
    assert new_book == "The Chronicles of Geronimo (the cat) by Geronimo"