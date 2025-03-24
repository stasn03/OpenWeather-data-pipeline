import requests
import json
from API_KEY import KEY

class WeatherDataPipeline:
    def __init__(self, city):
        self.city= city
        self.weather_data= self._fetch_data()
        self._clean_data()

    def display_data(self):
        print(self.weather_data)

    def _clean_data(self):
        self.weather_data= {
            "country": self.weather_data["sys"]["country"],
            "city": self.weather_data["name"],
            "temp": self.weather_data["main"]["temp"] - 273.15, # convert from kelvin to celsius
            "humidity": self.weather_data["main"]["humidity"],
            "wind_speed": self.weather_data["wind"]["speed"],

        }
    def _fetch_data(self):
        URL= f"https://api.openweathermap.org/data/2.5/weather?q={self.city}&appid={KEY}"      
        response= requests.get(URL)

        if response.status_code == 200:
            return response.json()
        else:
            print("Failed to fetch data")

    


weather_pipeline= WeatherDataPipeline("Orhei")
weather_pipeline.display_data()
