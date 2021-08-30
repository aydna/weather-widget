import tkinter as tk
import requests
from PIL import Image
from PIL import ImageTk


HEIGHT = 700
WIDTH = 800

def responseFormatter(weather):
    try:
        name = weather['name']
        description = weather['weather'][0]['description']
        temperature = weather['main']['temp']
        
        finalMsg = "Location: %s \nConditions: %s \nTemperature: %s°C" %(name, description, temperature)
    except:
        finalMsg = "Problem retrieving data"

    return finalMsg


def getWeather(city):
    weatherKey = 'ce3996dffe9b21c46dca439d05d0e22c'
    url = 'https://api.openweathermap.org/data/2.5/weather'
    params = {'APPID': weatherKey, 'q': city, 'units': 'metric'}
    response = requests.get(url, params=params)
    weather = response.json()

    label['text'] = responseFormatter(weather)
    iconCode = weather['weather'][0]['icon']
    open_image(iconCode)


def open_image(icon):
    size = int(lowerFrame.winfo_height()*0.25)
    img = ImageTk.PhotoImage(Image.open('./img/'+icon+'.png').resize((size, size)))
    weatherIcon.delete("all")
    weatherIcon.create_image(0,0, anchor='nw', image=img)
    weatherIcon.image = img

# api.openweathermap.org/data/2.5/forecast?q={city name}&appid={API key}
# API Key f4c4bf592995aa2d5ca73916ee5c7867


# GUI
root = tk.Tk()

canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

bgImg = Image.open('weatherBg.png')
bgImg = ImageTk.PhotoImage(bgImg)
bgLabel = tk.Label(root, image=bgImg)
bgLabel.place(relwidth=1, relheight=1)

frame = tk.Frame(root, bg='#99ceff', bd=5)
frame.place(relwidth=0.75, relheight=0.1, relx=0.5, rely=0.1, anchor="n")

entry = tk.Entry(frame, font=('Arial', 15))
entry.place(relwidth=0.7, relheight=1)

button1 = tk.Button(frame, text="Check Weather", font=('Arial', 20), command=lambda: getWeather(entry.get()))
button1.place(relwidth=0.3, relheight=1, relx=0.7)

lowerFrame = tk.Frame(root, bg='#99ceff', bd=10)
lowerFrame.place(relwidth=0.75, relheight=0.6, relx=0.5, rely=0.25, anchor='n')

label = tk.Label(lowerFrame, font=('Courier', 21), anchor='nw', justify='left', pady=16, padx=21)
label.place(relwidth=1, relheight=1)

# place icon
weatherIcon = tk.Canvas(label, bd=0, highlightthickness=0)
weatherIcon.place(relx=.75, rely=0, relwidth=1, relheight=0.5)

root.mainloop()