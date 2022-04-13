import sqlite3 as sq

with sq.connect('saper.db') as con:
    cur = con.cursor()
    cur.execute('''CREATE TABLE IF NOT EXISTS users (
        user_id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        sex INTEGER NOT NULL DEFAULT 1,
        old INTEGER,
        score INTEGER
    )''')

    # cur.execute("INSERT INTO users VALUES (1, 'Алексей', 1, 22, 1000)")
    # cur.execute("INSERT INTO users VALUES (2, 'Миша', 1, 19, 800)")
    # cur.execute("INSERT INTO users VALUES (3, 'Сергей', 1, 19, 900)")
    # cur.execute("INSERT INTO users VALUES (4, 'Мария', 2, 18, 1500)")
    # cur.execute("INSERT INTO users VALUES (5, 'Александр', 1, 20, 1100)")

    cur.execute("SELECT * FROM users")
    print(cur.fetchall())
    cur.execute("SELECT * FROM users WHERE sex = 2")
    print(cur.fetchall())
    cur.execute("SELECT * FROM users WHERE score < 1000")
    print(cur.fetchall())
    cur.execute("SELECT * FROM users ORDER BY score DESC")
    print(cur.fetchone())
    cur.execute("SELECT * FROM users WHERE old BETWEEN 18 AND 20")
    print(cur.fetchall())

    cur.execute("UPDATE users SET old = 20 WHERE old = 19")
    cur.execute("UPDATE users SET score = score + 300 WHERE score < 1000")
    cur.execute("UPDATE users SET score = score + 100 WHERE old >= 20")
    cur.execute("DELETE FROM users WHERE score < 1000")
