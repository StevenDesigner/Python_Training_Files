import sqlite3
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Function to connect to DB
def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row  # results as dictionaries
    return conn

@app.route('/')
def index():
    conn = get_db_connection()
    students = conn.execute('SELECT * FROM students').fetchall()
    conn.close()
    return render_template('index.html', students=students)

@app.route('/add', methods=['POST'])
def add_student():
    name = request.form['name']
    age = request.form['age']
    conn = get_db_connection()
    conn.execute('INSERT INTO students (name, age) VALUES (?, ?)', (name, age))
    conn.commit()
    conn.close()
    return redirect(url_for('index'))

@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit_student(id):
    conn = get_db_connection()
    if request.method == 'POST':
        name = request.form['name']
        age = request.form['age']
        conn.execute('UPDATE students SET name=?, age=? WHERE id=?', (name, age, id))
        conn.commit()
        conn.close()
        return redirect(url_for('index'))
    student = conn.execute('SELECT * FROM students WHERE id=?', (id,)).fetchone()
    conn.close()
    return render_template('edit.html', student=student)

@app.route('/delete/<int:id>')
def delete_student(id):
    conn = get_db_connection()
    conn.execute('DELETE FROM students WHERE id=?', (id,))
    conn.commit()
    conn.close()
    return redirect(url_for('index'))

if __name__=="__main__":
    app.run()