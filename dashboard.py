from pipeline import WeatherDataPipeline as dp

pipeline= dp("London")
pipeline.download_csv()

