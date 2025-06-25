import requests

def get_weather():
    api_key = "3f3690fbbd04fd8cc4b1d28635dcb2a6"
      # Replace with your OpenWeatherMap API key
    city = input("Enter the city name: ")
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

    response = requests.get(url)
    if response.status_code != 200:
        print("Failed to fetch weather data. Check the city name or try again.")
        return
    
    data = response.json()
    print("\nWeather Information:")
    print(f"City: {data['name']}, {data['sys']['country']}")
    print(f"Temperature: {data['main']['temp']}°C")
    print(f"Weather: {data['weather'][0]['description'].capitalize()}")
    print(f"Humidity: {data['main']['humidity']}%")
    print(f"Wind Speed: {data['wind']['speed']} m/s")
    print(f"Pressure: {data['main']['pressure']} hPa")

get_weather()
