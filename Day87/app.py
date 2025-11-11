from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

DB_NAME = 'cafes.db'

def init_db():
    with sqlite3.connect(DB_NAME) as conn:
        c = conn.cursor()
        c.execute('''CREATE TABLE IF NOT EXISTS cafes (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        name TEXT NOT NULL,
                        location TEXT NOT NULL,
                        wifi TEXT NOT NULL,
                        power TEXT NOT NULL,
                        coffee_price TEXT NOT NULL
                    )''')
        conn.commit()

@app.route('/')
def home():
    with sqlite3.connect(DB_NAME) as conn:
        c = conn.cursor()
        c.execute("SELECT * FROM cafes")
        cafes = c.fetchall()
    return render_template('index.html', cafes=cafes)

@app.route('/add', methods=['GET', 'POST'])
def add_cafe():
    if request.method == 'POST':
        name = request.form['name']
        location = request.form['location']
        wifi = request.form['wifi']
        power = request.form['power']
        coffee_price = request.form['coffee_price']
        with sqlite3.connect(DB_NAME) as conn:
            c = conn.cursor()
            c.execute("INSERT INTO cafes (name, location, wifi, power, coffee_price) VALUES (?, ?, ?, ?, ?)",
                      (name, location, wifi, power, coffee_price))
            conn.commit()
        return redirect(url_for('home'))
    return render_template('add.html')

@app.route('/delete/<int:cafe_id>', methods=["POST"])
def delete_cafe(cafe_id):
    db = sqlite3.connect("cafes.db")
    cursor = db.cursor()
    cursor.execute("DELETE FROM cafes WHERE id = ?", (cafe_id,))
    db.commit()
    db.close()
    return redirect(url_for('home'))

if __name__ == '__main__':
    init_db()
    app.run(debug=True)