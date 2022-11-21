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


# from flask import Flask, request, render_template, redirect
# from flask_sqlalchemy import SQLAlchemy
# from datetime import datetime
# import os

# from app import app

# project_dir = os.path.dirname(os.path.abspath(__file__))
# database_file = "sqlite:///{}".format(os.path.join(project_dir, "text.db"))
# app.config["SQLALCHEMY_DATABASE_URL"] = database_file
# db = SQLAlchemy(app)

# class Text(db.Model):
#     id = db.Column(db.Integer, primary_key = True)
#     content = db.Column(db.Text)

# def create_text(content):
#     text = Text(id=0, content=content)
#     db.session.add(text)
#     db.session.commit()
#     db.session.refresh(text)

# def read_texts():
#     return db.session.query(Text).all()

# def update_text(content):
#     db.session.query(Text).filter_by(id=0).update({
#         "content": content
#     })
#     db.session.commit()

# def delete_text():
#     db.session.query(Text).filter_by(id=0).delete()
#     db.session.commit()

# def create_or_update_text(content):
#     if len(read_texts()) == 0:
#         create_text(content)
#     else:
#         update_text(content)

# def read_text():
#     return read_texts()[0]

