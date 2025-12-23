from flask import Flask, render_template, request
from weather import main as weather

app = Flask(__name__)



if __name__ == '__main__':
    app.run(debug=True)