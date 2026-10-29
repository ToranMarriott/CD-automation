from lib.user import User

def test_user_instantiates_with_properties():
    user = User("Toran1994", "password123", 1)
    assert user.id == 1
    assert user.username == "Toran1994"
    assert user.password == "password123"

def test_equality():
    user1 = User("Toran1994", "password123", 1)
    user2 = User("Toran1994", "password123", 1)
    assert user1 == user2

def test_formats_nicely():
    user = User("Toran1994", "password123", 1)
    assert str(user) == "User(1, Toran1994, password123)"