from flask import Flask, request, render_template
app = Flask(__name__)
import sqlite3

@app.route('/')
def home():
    return render_template("simple_form.html")

@app.route('/insert', methods=['POST'])
def insert():
    con = sqlite3.connect('login.db')
    cur = con.cursor()
    cur.execute("INSERT INTO USERS (Username, Password) VALUES (?,?)
                (request.form['un'],request.form['pw']
    con.commit()
    return request.form['un'] + ' added'
                 
@app.route('/select')
def select():     
    con = sqlite3.connect('login.db')
    cur = con.cursor()
    cur.execute("SELECT * FROM Users")
    return str(cur.fetchall())            
             
