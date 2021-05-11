from flask import Flask, request
app = Flask(__name__)

@app.route('/')
def home():
    return "test"

@app.route('/hello', methods=['POST'])
def hello():
    name = request.form['un']
    return 'hello ' + name

