# 🌦️ Basic Weather App

## 📌 Project Overview

This project is a Python-based Basic Weather App developed as part of my **Oasis Infobyte Python Programming Internship**.

The application fetches real-time weather information for a user-specified city using the **OpenWeatherMap API** and displays the current weather details in the command line.

## ✨ Features

- 🌍 Search weather by city name
- 🌡️ Displays temperature in Celsius (°C)
- 🌡️ Displays temperature in Fahrenheit (°F)
- 💧 Displays humidity percentage
- ☁️ Displays current weather condition
- 💨 Displays wind speed
- 🔄 Allows checking weather for multiple cities
- ⚠️ Handles invalid city names
- 🔐 Handles invalid API keys
- 🌐 Handles network connection errors
- ⏱️ Handles request timeouts
- ✅ Validates empty city input

## 🛠️ Technologies Used

- **Python**
- **Requests** – for making API requests
- **JSON** – for processing weather data
- **python-dotenv** – for securely loading the API key
- **OpenWeatherMap API** – for real-time weather data

## 🔑 API Configuration

This application uses an OpenWeatherMap API key.

The API key is stored locally in a `.env` file:

```text
OPENWEATHER_API_KEY=your_api_key_here
