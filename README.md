# Weather App

A simple web application built with Flask that allows users to check the
current weather for a city using the OpenWeather API.

## Features

- Search weather by city, state, and country
- Shows temperature and weather description
- Clean and simple user interface
- Uses the OpenWeather API

## Technologies Used

- Python
- Flask
- HTML / CSS
- Bootstrap
- Requests
- dotenv

## Requirements

- Python 3.x
- An OpenWeather API key

## Installation

1.  Clone this repository\
    `git clone https://github.com/MohaOuakki/Weather_App_Flask.git`

2.  Navigate into the project folder\
    `cd Weather_App_Flask`

3.  Install dependencies\
    `pip install -r requirements.txt`

4.  Create a `.env` file in the project root and add your API key:

        API_KEY=your_api_key_here

## Usage

Run the application with:

    python app.py

Then open your browser and go to:

    http://127.0.0.1:5000

Enter a city name and view the current weather.

## Project Structure

    app.py
    weather.py
    templates/
    static/
    README.md

## License

This project is available for personal and educational use.
