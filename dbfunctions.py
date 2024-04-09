import sqlite3

def init_db():
    with open("create_database.sql") as f:
        script = f.read()

    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()
    cursor.executescript(script)
    conn.commit()
    conn.close()

def authenticate_user(username, password):
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()
    expected_password = list(cursor.execute(f"select password from users where username='{username}';"))[0][0]
    conn.close()
    return password == expected_password