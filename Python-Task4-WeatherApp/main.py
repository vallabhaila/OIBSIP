import os
import requests
from dotenv import load_dotenv

# Load API key from .env
load_dotenv()

API_KEY = os.getenv("OPENWEATHER_API_KEY")

print("==============================")
print("       WEATHER APP")
print("==============================")

while True:

    # Get city from user
    city = input("\nEnter city name: ").strip()

    # Validate empty input
    if not city:
        print("ERROR: City name cannot be empty.")
        continue

    url = "https://api.openweathermap.org/data/2.5/weather"

    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"
    }

    try:
        response = requests.get(url, params=params, timeout=10)

        # Check for API errors
        if response.status_code == 404:
            print("ERROR: City not found.")

        elif response.status_code == 401:
            print("ERROR: Invalid API key.")

        elif response.status_code != 200:
            print("ERROR: Unable to fetch weather data.")

        else:
            data = response.json()

            # Extract weather information
            temperature_c = data["main"]["temp"]
            temperature_f = (temperature_c * 9 / 5) + 32
            humidity = data["main"]["humidity"]
            condition = data["weather"][0]["description"].title()
            wind_speed = data["wind"]["speed"]

            # Display weather report
            print("\n==============================")
            print(f" Weather Report for {city.title()}")
            print("==============================")
            print(f"Temperature : {temperature_c:.1f} °C")
            print(f"Temperature : {temperature_f:.1f} °F")
            print(f"Humidity    : {humidity}%")
            print(f"Condition   : {condition}")
            print(f"Wind Speed  : {wind_speed} m/s")
            print("==============================")

    except requests.exceptions.Timeout:
        print("ERROR: Request timed out. Please try again.")

    except requests.exceptions.ConnectionError:
        print("ERROR: Network connection problem.")

    except requests.exceptions.RequestException:
        print("ERROR: Unable to connect to the weather service.")

    # Ask whether the user wants another city
    choice = input("\nDo you want to check another city? (y/n): ").strip().lower()

    if choice != "y":
        print("\nThank you for using the Weather App! 🌤️")
        break