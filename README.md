# Weather Data Pipeline

This project collects and stores weather data from multiple cities on an hourly basis, using the OpenWeatherMap API. The data is then cleaned and stored in a PostgreSQL database for further analysis.

## Features

- Fetches real-time weather data for multiple cities.
- Cleans and processes the data (e.g., temperature conversion from Kelvin to Celsius).
- Stores the cleaned data in a PostgreSQL database.
- Uses threading to handle data collection for multiple cities concurrently.
- Automatically fetches and inserts weather data every hour.

## Technologies Used

- **Python** - Programming language used to develop the data pipeline.
- **PostgreSQL** - Database used to store the weather data.
- **OpenWeatherMap API** - API to fetch real-time weather data.
- **psycopg2** - Library for PostgreSQL database connection and interaction.
- **threading** - Library for handling multiple cities concurrently.

## Prerequisites

Before running this project, ensure that you have the following installed:

- Python 3.x
- PostgreSQL database running and accessible
- Required Python libraries:
  - `requests`
  - `psycopg2`
  
To install the required Python libraries, run:

```bash
pip install requests
pip install psycopg2
```

### Setup

1. Clone this repository

```bash
git clone "https://github.com/stasn03/OpenWeather-data-pipeline.git"
```

2. Setup your own PostreSQL database and your own table

3. Add your own API key from OpenWeather website

### Running the Project

To start the weather data pipeline, simply run the script.py file:

```bash
python main.py
```