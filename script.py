import requests
from datetime import datetime, timezone
import psycopg2
from API_KEY import KEY
from PSQL_DATA import DBNAME, USERNAME, PASSWORD, HOST, PORT

class WeatherDataPipeline:
    def __init__(self, city):
        self.city= city
        self.weather_data= self._fetch_data()
        self._clean_data()
        self._connect_to_database()

    def display_data(self):
        for i in self.weather_data.items():
            print(i)

    def _clean_data(self):
        self.weather_data= {
            "timestamp": datetime.fromtimestamp(self.weather_data["dt"], tz= timezone.utc).strftime("%Y-%m-%d %H:%M:%S"),
            "country": self.weather_data["sys"]["country"],
            "city": self.weather_data["name"],
            "temp": round(self.weather_data["main"]["temp"] - 273.15, 2), # convert from kelvin to celsius
            "humidity": self.weather_data["main"]["humidity"],
            "wind_speed": self.weather_data["wind"]["speed"]
        }
        
    def _fetch_data(self):
        URL= f"https://api.openweathermap.org/data/2.5/weather?q={self.city}&appid={KEY}"      
        response= requests.get(URL)

        if response.status_code == 200:
            return response.json()
        else:
            print("Failed to fetch data")

    def _connect_to_database(self):
        conn= psycopg2.connect(
            dbname= DBNAME,
            user= USERNAME,
            password= PASSWORD,
            host= HOST,
            port= PORT
        )


    
    


weather_pipeline= WeatherDataPipeline("London")
weather_pipeline.display_data()
