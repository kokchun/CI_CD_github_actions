import requests
import streamlit as st

# Retrieve API key securely from Streamlit secrets
api_key = st.secrets["api"][
    "OPEN_WEATHER_MAP_API"
]  # Store the API key in Streamlit Secrets
print(api_key)

# Title of the app
st.title("Weather Information")

# Input: User enters the city name
city = st.text_input("Enter city name:", "Oslo")


# Function to get weather data
def get_weather_data(city, api_key):
    url = f"https://api.openweathermap.org/data/2.5/weather?\
        q={city}&appid={api_key}&units=metric"
    response = requests.get(url)

    if response.status_code == 200:
        weather_data = response.json()
        return weather_data
    else:
        st.error(f"Error fetching data: {response.status_code}")
        return None


# If the user provides a city name
if city:
    weather_data = get_weather_data(city, api_key)

    if weather_data:
        # Display weather information
        st.subheader(f"Weather in {city.capitalize()}")
        st.write(f"Temperature: {weather_data['main']['temp']} °C")
        st.write(f"Humidity: {weather_data['main']['humidity']} %")
        st.write(f"Weather: {weather_data['weather'][0]['description'].capitalize()}")

        # Display weather icon
        icon_code = weather_data["weather"][0]["icon"]
        icon_url = f"http://openweathermap.org/img/wn/{icon_code}.png"
        st.image(icon_url, width=100)

        # Display more information (e.g., wind speed)
        st.write(f"Wind Speed: {weather_data['wind']['speed']} m/s")
    else:
        st.write("No data available.")
