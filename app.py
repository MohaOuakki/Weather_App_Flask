from flask import Flask, render_template, request
from weather import main as weather

app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def home():
    data = None
    if request.method == 'POST':
        city = request.form['cityName']
        state = request.form['stateName']
        country = request.form['countryName']
        data = weather(city, state, country)
    return render_template('index.html', data=data)


if __name__ == '__main__':
    app.run(debug=True)