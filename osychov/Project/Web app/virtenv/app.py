import requests
from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
import os


app = Flask(__name__)
app.config['DEBUG'] = True
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir,"weather.db")


db = SQLAlchemy(app)


class City(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)

@app.route('/', methods=['GET', 'POST'])
def index():
    
    if request.method == 'POST':
        new_city = request.form.get('city')
        
        if new_city:
            new_city_obj = City(name=new_city)

            db.session.add(new_city_obj)
            db.session.commit()

    cities = City.query.all()

    url = "https://api.openweathermap.org/data/2.5/weather?q={}&appid=ef2206ff5da67de63306d0b143e20872&units=metric"

    weather_data = []

    for city in cities:

        r = requests.get(url.format(city.name)).json()

        weather = {
            'city' : city.name,
            'temperature' : r['main']['temp'],
            'feel_like' : r["main"]["feels_like"],
            'description' : r['weather'][0]['description'],
            'icon' : r['weather'][0]['icon'],
            'wind' : r["wind"]["speed"],
            'humidity' : r["main"]["humidity"],
            'pressure' : r["main"]["pressure"],
        }

        weather_data.append(weather)


    return render_template('weather.html', weather_data=weather_data)


if __name__ == '__main__':
    app.run(debug = True, port=5000)
    
