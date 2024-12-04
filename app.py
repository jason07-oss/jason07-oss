from flask import Flask, render_template, request, redirect, url_for
import mysql.connector

app = Flask(__name__)

# Koneksi database
def get_db_connection():
    conn = mysql.connector.connect(
        host='localhost',
        user='root',  # Ganti dengan username MySQL Anda
        password='',  # Ganti dengan password MySQL Anda
        database='crud_app'
    )
    return conn

# Halaman utama untuk menampilkan data
@app.route('/')
def index():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute('SELECT * FROM users')
    users = cursor.fetchall()
    cursor.close()
    conn.close()
    return render_template('index.html', users=users)

# Halaman untuk menambah data
@app.route('/add', methods=['POST'])
def add_user():
    name = request.form['name']
    email = request.form['email']
    
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO users (name, email) VALUES (%s, %s)', (name, email))
    conn.commit()
    cursor.close()
    conn.close()
    
    return redirect(url_for('index'))

# Halaman untuk menghapus data
@app.route('/delete/<int:id>')
def delete_user(id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('DELETE FROM users WHERE id = %s', (id,))
    conn.commit()
    cursor.close()
    conn.close()
    
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
