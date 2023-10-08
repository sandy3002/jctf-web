from flask import Flask, request, render_template
import sqlite3

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method =='POST':


        connection = sqlite3.connect('user_data.db')
        cursor =    connection.cursor()

        name = request.form['name']
        password = request.form['password']

        query = "SELECT name,password FROM users where name= '"+name+"' and password= '"+password+"'"
        cursor.execute(query)

        results = cursor.fetchall()

        if len(results) == 0:
            return render_template("index.html", error="Invalid Username or Password")
        else:
            return render_template("logged_in.html")

    return render_template("index.html")

