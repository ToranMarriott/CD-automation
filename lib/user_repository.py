from lib.user import User

class UserRepository:
    def __init__(self, connection):
        self._connection = connection

    def all(self):
        rows = self._connection.execute(
            "SELECT * FROM users"
        )
        users = []
        for row in rows:
            item = User(row["username"], row["password"], row["id"])
            users.append(item)
        return users

    def create(self, user):
        self._connection.execute(
            "INSERT INTO users (username, password) VALUES (%s, %s)",
            [user.username, user.password]
        )