import requests
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
import os


app = Flask(__name__)
app.config['DEBUG'] = True
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir,"weather.db")
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'thisisasecret'




db = SQLAlchemy(app)


class City(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)

def get_weather_data(city):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid=ef2206ff5da67de63306d0b143e20872&units=metric"
    r = requests.get(url).json()
    return r 

@app.route('/')
def index_get():
    cities = City.query.all()
    weather_data = []

    for city in cities:
        r= get_weather_data(city.name)
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

@app.route('/', methods=['POST'])
def index_post():
    err_mess = ''
    new_city = request.form.get('city')
    if new_city:
        existing_city = City.query.filter_by(name = new_city).first()
        
        if not existing_city:
            new_city_data = get_weather_data(new_city)
            if new_city_data['cod'] == 200:
                new_city_obj = City(name=new_city)

                db.session.add(new_city_obj)
                db.session.commit()
            else:
                err_mess = 'City does not exists in the world!'
        else:
            err_mess = 'City already exists in database!'
            
    if err_mess:
        flash(err_mess, 'error')
    else:
        flash('City added succesfully!')
        
    return redirect(url_for('index_get'))

if __name__ == '__main__':
    app.run(debug = True, port=5000)
    
