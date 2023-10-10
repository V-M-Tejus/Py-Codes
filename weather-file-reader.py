import json

# Function to load JSON data from a file
def load_weather_data(file_path):
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
        return data
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return None
    except json.JSONDecodeError:
        print(f"Invalid JSON format in file: {file_path}")
        return None

# Function to access specific weather data
def get_weather_info(weather_data, key):
    if key in weather_data:
        return weather_data[key]
    else:
        return None

# Specify the file path
file_path = 'weather_data.json'

# Load the weather data from the JSON file
weather_data = load_weather_data(file_path)

print(weather_data)

if weather_data:

    for data in weather_data:
        # Access specific weather information
        wind_speed = get_weather_info(data, "Wind-speed")
        humidity = get_weather_info(data, "Humidity")
        temperature = get_weather_info(data, "Temperature")
        weather = get_weather_info(data, "weather")
        if wind_speed is not None:
            print(f"Wind Speed: {wind_speed}")
        if humidity is not None:
            print(f"Humidity: {humidity}")
        if temperature is not None:
            print(f"Temperature: {temperature}")
        if weather is not None:
            print(f"Weather: {weather}")
        print()
