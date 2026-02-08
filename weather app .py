
import requests

APi_KEY="756894706808749026746fa436541911"
BASE_url="https://api.openweathermap.org/data/2.5/weather"

def getweather(city):
    params = {
    "q": city,
    "appid": APi_KEY,
    "units" : "metric"
    }
    response= requests.get(BASE_url, params=Params )

    if response.status_code == 200 :
        data=response.json

        temp = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        weather = data["weather"][0]["description"]
        wind = data["wind"]["speed"]
     

        print(f"\nWeather in {city}")
        print(f"Temperature: {temp}°C")
        print(f"Condition: {weather}")
        print(f"Humidity: {humidity}%")
        print(f"Wind Speed: {wind} m/s")
    else:
        print("City not found!")

if __name__ == "__main__":
    while True:
        city = input("\nEnter city name (or 'exit'): ")

        if city.lower() == "exit":
            print("Goodbye!")
            break
            getweather(city)




# import requests

# API_KEY = "756894706808749026746fa436541911"
# BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

# def get_weather(city):
#     params = {
#         "q": city,
#         "appid": API_KEY,
#         "units": "metric"
#     }

#     response = requests.get(BASE_URL, params=params)

#     if response.status_code == 200:
#         data = response.json()

#         temp = data["main"]["temp"]
#         humidity = data["main"]["humidity"]
#         weather = data["weather"][0]["description"]
#         wind = data["wind"]["speed"]

#         print(f"\nWeather in {city}")
#         print(f"Temperature: {temp}°C")
#         print(f"Condition: {weather}")
#         print(f"Humidity: {humidity}%")
#         print(f"Wind Speed: {wind} m/s")
#     else:
#         print("City not found!")

# if __name__ == "__main__":
#     while True:
#         city = input("\nEnter city name (or 'exit'): ")

        # if city.lower() == "exit":
        #     print("Goodbye!")
        #     break

        # get_weather(city)


