import streamlit as st
import threading
from pipeline import WeatherDataPipeline as dp

cities= ["London", "New York", "Paris", "Berlin", "Beijing"]
threads= []



st.title("Wheather Pipeline")
if st.button("Download CSV"):
    pipeline= dp(cities[0])
    pipeline.download_csv()
elif st.button("Run"):
    for city in cities:
        pipeline= dp(city)
        weather_thread= threading.Thread(target= pipeline.run)
        threads.append(weather_thread)
        weather_thread.start()

    for thread in threads:
        thread.join()

elif st.button("Stop"):
    pipeline= dp(cities[0])
    pipeline.stop()
