from flask import Flask, render_template, request, redirect, url_for
import mysql.connector

app = Flask(__name__)

# MariaDB Connection
db = mysql.connector.connect(
    host="localhost",
    user="flaskuser",
    password="",
    database="flask_app"
)


cursor = db.cursor(dictionary=True)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        country = request.form['country']

        query = "INSERT INTO users (name, email, country) VALUES (%s, %s, %s)"
        cursor.execute(query, (name, email, country))
        db.commit()

        return redirect(url_for('view_data'))

    return render_template('index.html')


@app.route('/view')
def view_data():
    cursor.execute("SELECT * FROM users")
    data = cursor.fetchall()
    return render_template('view.html', users=data)


if __name__ == '__main__':
    app.run(debug=True)

