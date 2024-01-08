import requests

api_key = 'efc647bff60bdaca1bdddf1f7e9786e5'

user_input = input("Enter city: ")

weather_data = requests.get(
    f"https://api.openweathermap.org/data/2.5/weather?q={user_input}&units=imperial&APPID={api_key}")

if weather_data.json()['cod'] == '404':
    print("No City Found")
else:
    weather = weather_data.json()['weather'][0]['main']
    temp = round(weather_data.json()['main']['temp'])

    # Store the information in a text file
    with open('weather_info.txt', 'w') as file:
        file.write(f"The weather in {user_input} is: {weather}\n")
        file.write(f"The temperature in {user_input} is: {temp}\n")

    print(f"Weather information saved in 'weather_info.txt'")
