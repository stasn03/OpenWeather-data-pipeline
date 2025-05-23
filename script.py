import requests
from datetime import datetime, timezone, timedelta
import psycopg2
import time
import threading
import os
from dotenv import find_dotenv, load_dotenv

load_dotenv(find_dotenv())
class WeatherDataPipeline:
    def __init__(self, city):
        self.city= city
        self.conn= self._connect_to_database()

    def run(self):
        try:
            while True:
                self.weather_data= self._fetch_data()
                self._clean_data()
                self._insert_to_database()
                print(f"Data inserted:")
                self.display_data()

                time.sleep(3600)
        except Exception as e:
            print(f"Pipeline failed: {e}")

    def display_data(self):
        for i in self.weather_data.items():
            print(i)

    def _clean_data(self):
        self.weather_data= {
            "timestamp": datetime.fromtimestamp(self.weather_data["dt"], tz= timezone.utc).strftime("%Y-%m-%d %H:%M:%S"),
            "country": self.weather_data["sys"]["country"],
            "city": self.weather_data["name"],
            "temp": int(self.weather_data["main"]["temp"] - 273.15), # convert from kelvin to celsius
            "humidity": self.weather_data["main"]["humidity"],
            "wind_speed": self.weather_data["wind"]["speed"]
        }
        
    def _fetch_data(self):
        URL= f"https://api.openweathermap.org/data/2.5/weather?q={self.city}&appid={os.getenv('KEY')}"      
        response= requests.get(URL)

        if response.status_code == 200:
            return response.json()
        else:
            print("Failed to fetch data")

    def _connect_to_database(self):
        try:
            conn= psycopg2.connect(
                dbname= os.getenv('DBNAME'),
                user= os.getenv('USER'),
                password= os.getenv('PASSWORD'),
                host= os.getenv('HOST'),
                port= os.getenv('PORT')
            )

            return conn
        except Exception as e:
            print(f"Error: {e}")
        
    def _insert_to_database(self):
        cursor= self.conn.cursor()
        insert_query= """
        INSERT INTO weather_log(timestamp, country, city, temperature, humidity, wind_speed) 
        VALUES(%s, %s, %s, %s, %s, %s);
        """

        data= (
        self.weather_data["timestamp"],
        self.weather_data["country"],
        self.weather_data["city"],
        self.weather_data["temp"],
        self.weather_data["humidity"],
        self.weather_data["wind_speed"]
        )

        cursor.execute(insert_query, data)
        self.conn.commit()
        cursor.close()
        

if __name__ == "__main__":
    cities= ["London", "New York", "Paris", "Berlin", "Beijing"]
    threads= []

    for city in cities:
        pipeline= WeatherDataPipeline(city)
        weather_thread= threading.Thread(target= pipeline.run)
        threads.append(weather_thread)
        weather_thread.start()

    for thread in threads:
        thread.join()

