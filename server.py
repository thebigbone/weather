from flask import Flask, render_template, request
from weather import get_current_weather
from waitress import serve

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/weather')
def get_weather():
    city = request.args.get('city')
    weather_data = get_current_weather(city)


    if not bool(city.strip()):
        city = "California"

    if not weather_data['cod'] == 200:
        return render_template("404.html")
    else:
        title = weather_data['name']
        status = weather_data["weather"][0]["description"].capitalize()
        temp = f"{weather_data['main']['temp']:.1f}"
        feels_like = f"{weather_data['main']['feels_like']:.1f}"

        return render_template(
            "weather.html",
            title=title,
            status=status,
            temp=temp,
            feels_like=feels_like
        )


if __name__ == "__main__":
    serve(app, host="0.0.0.0", port=8000)