from app import app
from lib.database_connection import DatabaseConnection
from playwright.sync_api import Page, expect

def test_create_user_is_saved_to_database(page: Page):
    client = app.test_client()
    connection = DatabaseConnection()
    connection.connect()
    connection.execute("TRUNCATE TABLE users")
    connection.execute("INSERT INTO users (username, password) values ('test', '1234');")
    response = client.post('/sessions/new', data={
        'username': 'test',
        'password': '1234'
    })
    assert response.status_code == 302
    assert response.headers['Location'].endswith('/books')

def test_auth_playwright(page: Page):
    connection = DatabaseConnection()
    connection.connect()
    connection.execute("TRUNCATE TABLE users;")
    connection.execute("INSERT INTO users (username, password) values ('test', '1234');")
    page.goto("http://localhost:5001/sessions/new")
    page.locator("#username").fill("test")
    page.locator("#password").fill("1234")
    page.get_by_role("button").click()
    assert page.url == "http://localhost:5001/books"

def test_failed_auth(page: Page, db_connection):
    client = app.test_client()
    db_connection.seed("seeds/book_store_seed.sql")
    response = client.post('/sessions/new', data={
        'username': 'test',
        'password': '1234'
    })
    assert response.status_code == 302
    assert response.headers['Location'].endswith('/sessions/new')

def test_failed_auth_playwright(page: Page, db_connection):
    db_connection.seed("seeds/book_store_seed.sql")
    page.goto("http://localhost:5001/sessions/new")
    page.locator("#username").fill("test")
    page.locator("#password").fill("1234")
    page.get_by_role("button").click()
    assert page.url == "http://localhost:5001/sessions/new"

def test_failed_auth_creates_book(page: Page, db_connection):
    db_connection.seed("seeds/book_store_seed.sql")
    page.goto("http://localhost:5001/books/add_book")
    assert page.url == "http://localhost:5001/sessions/new"