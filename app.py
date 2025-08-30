from flask import Flask, render_template, request, redirect, g
import sqlite3
import os
import string
import random

app = Flask(__name__)
app.config['DATABASE'] = 'url_shortener.db'  # Corrected name

# Function to connect to the SQLite Database
def get_db():
    if 'db' not in g:
        g.db = sqlite3.connect(app.config['DATABASE'])
        g.db.row_factory = sqlite3.Row
    return g.db

# Function to close the Database connection
def close_db(e=None):
    db = g.pop('db', None)
    if db is not None:
        db.close()

# Initialize the Database (Create Tables)
def init_db():
    with app.app_context():
        db = get_db()
        with app.open_resource('Schema.sql', mode='r') as f:
            db.executescript(f.read())
        db.commit()

# Function to generate a unique short code
def generate_short_code():
    characters = string.ascii_letters + string.digits
    return "".join(random.choice(characters) for _ in range(6))

# Routes
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/shorten', methods=['POST'])
def shorten():
    long_url = request.form.get('long_url')
    if not long_url:
        return "URL is required!", 400

    db = get_db()
    short_code = generate_short_code()

    # Check if the short code already exists
    while db.execute('SELECT id FROM urls WHERE short_code=?', (short_code,)).fetchone() is not None:
        short_code = generate_short_code()

    db.execute(
        'INSERT INTO urls (long_url, short_code) VALUES (?, ?)',
        (long_url, short_code)
    )
    db.commit()

    short_url = request.host_url + short_code
    return render_template('index.html', short_url=short_url)

@app.route('/<short_code>')
def redirect_to_long_url(short_code):
    db = get_db()
    url = db.execute(
        'SELECT long_url FROM urls WHERE short_code=?',
        (short_code,)
    ).fetchone()
    if url is None:
        return "URL not found!", 404
    return redirect(url['long_url'])

# Close the database connection after each request
app.teardown_appcontext(close_db)

if __name__ == '__main__':
    if not os.path.exists(app.config['DATABASE']):
        init_db()
    app.run(debug=True)
