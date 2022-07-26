
# Importing Requests module
import requests

# api key generate after login
API_KEY = 'bb2612fc32142ad02c306dd64d873cc5'

# url where api requests
BASIC_URL = "https://api.openweathermap.org/data/2.5/weather"

city = input("Enter a city name: ")

city = city.upper()
# Requesting basic of city
# can be request on the basic of various module
request_url = f"{BASIC_URL}?appid={API_KEY}&q={city}"

# retrieving inforamtion basic of request_url
response = requests.get(request_url)

# checking status_code is succesfull or not
if response.status_code  == 200:
    data = response.json()
    weather = data['weather'][0]['description']
    print(f"Wheather at {city} is ", weather)

    # converting fahrenheit into celsius and taking two decimal point
    temprature = round(data["main"]["temp"] - 273, 2)
    print(f"Temprature at {city} is ", temprature, "celsius")
else:
    print("Error occur in the program")