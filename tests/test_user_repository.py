from lib.user_repository import UserRepository
from lib.user import User

def test_all(db_connection):
    db_connection.seed("seeds/book_store_seed.sql")
    repo = UserRepository(db_connection)
    assert repo.all() == [
        User('tony29', 'tonypassword', 1),     
        User('laura85', 'laurapassword', 2),   
        User('geralt666', 'geraltpassword', 3)
    ]

def test_create(db_connection):
    db_connection.seed("seeds/book_store_seed.sql")
    repo = UserRepository(db_connection)
    user = User('ciri33', "ciripassword", None)
    assert repo.create(user) == None
    assert repo.all() == [
        User('tony29', 'tonypassword', 1),     
        User('laura85', 'laurapassword', 2),   
        User('geralt666', 'geraltpassword', 3),
        User('ciri33', 'ciripassword', 4)
    ]