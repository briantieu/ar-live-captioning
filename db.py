import sqlite3

def connect_db():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = connect_db()
    with open('schema.sql') as f:
        conn.executescript(f.read())
    conn.close()

def insert_db(content):
    conn = connect_db()
    cur = conn.cursor()
    cur.execute("DELETE FROM Texts")
    cur.execute("INSERT INTO Texts (content) VALUES (?)", (content,))
    conn.commit()
    conn.close()

def read_db():
    conn = connect_db()
    texts = conn.execute('SELECT * FROM Texts').fetchall()
    conn.close()
    return texts

if __name__ == '__main__':
    init_db()
    insert_db('Listening...')