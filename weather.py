from dotenv import load_dotenv
from pprint import pprint
import os
import requests

load_dotenv()

def get_current_weather(city='New York City'):
    request_url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={os.getenv("API_KEY")}&units=imperial'

    weather_data = requests.get(request_url).json()

    return weather_data


if __name__ == "__main__":
    print("\n *** get weather conditions ***\n")

    city_name = input("enter city: ")

    weather_data = get_current_weather(city)
    print("\n")
    pprint(weather_data)