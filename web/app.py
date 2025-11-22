import os
import random
from flask import Flask, render_template, request
import mysql.connector
from mysql.connector import Error

app = Flask(__name__)

def get_db_connection():
    try:
        conn = mysql.connector.connect(
            host=os.environ.get('MYSQL_HOST', 'db'),
            port=int(os.environ.get('MYSQL_PORT', 3306)),
            user=os.environ.get('MYSQL_USER'),
            password=os.environ.get('MYSQL_PASSWORD'),
            database=os.environ.get('MYSQL_DATABASE')
        )
        return conn
    except Error:
        return None

@app.route('/', methods=['GET', 'POST'])
def index():
    message = None
    bandnames = []
    
    if request.method == 'POST':
        action = request.form.get('action')
        
        if action == 'test':
            conn = get_db_connection()
            if conn:
                try:
                    cursor = conn.cursor()
                    cursor.execute('SELECT 1')

                    
                    cursor.fetchall()

                    message = "Communication avec la base de données établie"
                except Exception:
                    message = "Impossible de se connecter à la base de données"
                finally:
                    cursor.close()
                    conn.close()
            else:
                message = "Impossible de se connecter à la base de données"

        elif action == 'generate':
            conn = get_db_connection()
            if conn:
                try:
                    cursor = conn.cursor(dictionary=True)

                    cursor.execute("SELECT adjective FROM adjectives")
                    adjectives = [row['adjective'] for row in cursor.fetchall()]

                    cursor.execute("SELECT noun FROM nouns")
                    nouns = [row['noun'] for row in cursor.fetchall()]

                    cursor.close()
                    conn.close()

                    if not adjectives or not nouns:
                        message = "La base ne contient pas assez de données."
                    else:
                        for _ in range(10):
                            a = random.choice(adjectives)
                            n = random.choice(nouns)
                            bandnames.append(f"The {a} {n}")

                except:
                    message = "Impossible de se connecter à la base de données"
            else:
                message = "Impossible de se connecter à la base de données"

    return render_template('index.html', message=message, bandnames=bandnames)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
