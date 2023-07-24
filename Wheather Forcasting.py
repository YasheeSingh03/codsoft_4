import tkinter as tk
from tkinter import PhotoImage
import requests


def get(city):
    key = '9ed4b30ad5233cfb3df6f18d42972f69'
    url = 'https://api.openweathermap.org/data/2.5/weather'
    p = {'APPID': key, 'q': city, 'units': 'metric'}
    response = requests.get(url, params=p)
    data = response.json()

    if data['cod'] == 200:
        city_name = data['name']
        temperature = data['main']['temp']
        humidity = data['main']['humidity']
        wind_speed = data['wind']['speed']
        description = data['weather'][0]['description']

        weather_info = f'City: {city_name}\nTemperature: {temperature}°C\nHumidity: {humidity}%\nWind Speed: {wind_speed} m/s\nShort Description: {description}'
        label_t['text'] = weather_info
    else:
        label_t['text'] = 'Error fetching weather data'

weather= tk.Tk()
weather.title('Weather Forecast')
image=PhotoImage(file=r"C:\Users\akars\Desktop\Programming\cloud-g7215b1076_1280.png")
background_label=tk.Label(weather, image=image)
background_label.place(x=0,y=0,relwidth=1,relheight=1)

weather.geometry(("1400x1000"))
label = tk.Label(weather, text='CITY NAME',font=("Algerian",40,"bold italic"))
label.place(x=650,y=170)
entry = tk.Entry(weather,font=("Times",30,"italic"),width=30)
entry.place(x=500,y=240)
buton = tk.Button(weather, text='GET FORECAST',font=("Times",23,"bold"),bg="dark cyan",command=lambda: get(entry.get()))
buton.place(x=670,y=320)

label_t = tk.Label(weather, text='', justify='left',font=("Algerian",18,"bold"))
label_t.place(x=670,y=420)

weather.mainloop()