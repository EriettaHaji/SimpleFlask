from flask import Flask, request, render_template
app = Flask(__name__)

@app.route('/')
def home():
    return render_template("simple_form.html")

@app.route('/hello', methods=['POST'])
def hello():
    name = request.form['un']
    return 'hello ' + name

