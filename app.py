from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def hello():
    nombre = "Carlos Taba"
    return render_template('index.html', nombre=nombre)