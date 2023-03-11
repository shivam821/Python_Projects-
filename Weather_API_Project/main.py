import requests

api_key = '2422909f90abdea91ed5c9c0e5b2ca57'

user_input = input("Enter city: ")

weather_data = requests.get(
    f"https://api.openweathermap.org/data/2.5/weather?q={user_input}&units=imperial&APPID={api_key}")

if weather_data.json()['cod'] == '404' :
    print("No city found")
else : 

#print(weather_data.json())
    weather = weather_data.json()['weather'][0]['main']
    temp = weather_data.json()['main']['temp']

    print("Weather : "+ str(weather) + " and the temp is : " + str(temp))
