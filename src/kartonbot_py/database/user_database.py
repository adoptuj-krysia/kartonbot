import sqlite3
from datetime import datetime
from kartonbot_py.common.date_utils import str_to_date, date_to_str


class UserDatabase:
    """Umożliwia operacje na bazie danych przechowującej użytkowników,
    którzy chociaż raz skorzystali z komendy !kartonbot"""

    def __init__(self):
        self._connection = sqlite3.connect('data/users.db')
        cursor = self._connection.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS users "
                       "(username TEXT, first_use TEXT, total_uses INTEGER, last_used TEXT, admin INT)")
        self._connection.commit()

    def close(self):
        self._connection.close()

    def contains_user(self, username):
        cursor = self._connection.cursor()
        cursor.execute("SELECT * FROM users WHERE username=?", (str(username),))
        row = cursor.fetchone()
        return row is not None

    def register_user(self, username):
        cursor = self._connection.cursor()
        registration_date = date_to_str(datetime.now())
        cursor.execute("INSERT INTO users VALUES (?, ?, 0, ?, 0)", (str(username), registration_date, registration_date))
        self._connection.commit()

    def increment_usage_count(self, username):
        cursor = self._connection.cursor()
        cursor.execute("UPDATE users SET last_used=?, total_uses=total_uses+1 WHERE username=?", (date_to_str(datetime.now()), str(username)))
        self._connection.commit()

    def get_total_uses(self, username):
        cursor = self._connection.cursor()
        cursor.execute("SELECT total_uses FROM users WHERE username=?", (str(username),))
        return int(cursor.fetchone()[0])

    def get_registration_date(self, username):
        cursor = self._connection.cursor()
        cursor.execute("SELECT first_use FROM users WHERE username=?", (str(username),))
        return str(cursor.fetchone()[0])

    def set_admin(self, username, admin):
        cursor = self._connection.cursor()
        cursor.execute("UPDATE users SET admin=? WHERE username=?", ("1" if admin else "0", str(username)))
        self._connection.commit()

    def is_admin(self, username):
        cursor = self._connection.cursor()
        cursor.execute("SELECT admin FROM users WHERE username=?", (str(username),))
        return str(cursor.fetchone()[0]) == "1"

    def get_seconds_since_last_use(self, username):
        cursor = self._connection.cursor()
        cursor.execute("SELECT last_used FROM users WHERE username=?", (str(username),))
        last_used = str_to_date(str(cursor.fetchone()[0]))
        delta = datetime.now() - last_used
        return delta.total_seconds()

    def dump_db_to_str(self):
        cursor = self._connection.cursor()
        rows = [
            "**__Zrzut bazy danych z dnia {}__**".format(date_to_str(datetime.now())),
            "**Nazwa użytkownika | Data pierwszego użycia | Łączna liczba użyć | Ostanie użycie | Czy admin?**"
        ]
        for row in cursor.execute("SELECT * FROM users"):
            rows.append("{} | {} | {} | {} | {}".format(*row))
        return "\n".join(rows)

