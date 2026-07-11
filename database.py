import sqlite3

# ---------- DATABASE CONNECTION ----------
conn = sqlite3.connect(
    "loan_system.db",
    check_same_thread=False
)

cursor = conn.cursor()

# ---------- CREATE USERS TABLE ----------
cursor.execute("""
CREATE TABLE IF NOT EXISTS users (

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    username TEXT NOT NULL,

    email TEXT UNIQUE NOT NULL,

    password TEXT NOT NULL
)
""")

conn.commit()

# ---------- REGISTER USER ----------
def register_user(
    username,
    email,
    password
):

    try:

        cursor.execute(
            """
            INSERT INTO users
            (username, email, password)

            VALUES (?, ?, ?)
            """,

            (
                username,
                email,
                password
            )
        )

        conn.commit()

        return True

    except sqlite3.IntegrityError:

        # Email already exists
        return False

    except Exception as e:

        print(e)

        return False

# ---------- LOGIN USER ----------
def login_user(
    email,
    password
):

    cursor.execute(
        """
        SELECT * FROM users

        WHERE email=? AND password=?
        """,

        (
            email,
            password
        )
    )

    user = cursor.fetchone()

    return user

# ---------- GET ALL USERS ----------
def get_all_users():

    cursor.execute(
        "SELECT * FROM users"
    )

    return cursor.fetchall()