from flask import Flask, render_template, g
import sqlite3
import os

app = Flask(__name__)
DATABASE = os.path.join(os.path.dirname(__file__), 'app.db')

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

def init_db():
    with app.app_context():
        db = get_db()
        cursor = db.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS example (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            question TEXT,
            answer TEXT
        )''')
        db.commit()

@app.route('/')
def main_1200():
    return render_template('main_1200.html')

@app.route('/faq')
def faq():
    db = get_db()
    cursor = db.cursor()
    cursor.execute('SELECT question, answer FROM example')
    faqs = cursor.fetchall()
    return render_template('faq.html', faqs=faqs)

if __name__ == '__main__':
    init_db()
    app.run(debug=True) 