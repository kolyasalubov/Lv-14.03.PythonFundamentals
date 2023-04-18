import tkinter as tk
from pyowm import OWM
from API_KEY import API_KEY


HEIGHT = 350
WIDTH = 450


def weather_responce():
    input_city = entry_field.get()
    owm = OWM(API_KEY)
    mgr = owm.weather_manager()
    observation = mgr.weather_at_place(input_city)
    w = observation.weather
    return f"""Conditions: {w.detailed_status}\nTemperature is {w.temperature('celsius')['temp']}\n
Wind speed is {w.wind()['speed']} km/hours\nHumidity of air is {w.humidity}
\nCloudiness is {w.clouds}%\nWhether it's raining or not: {w.rain}\n
Heat index is {w.heat_index}"""


def get_weather():
    label['text'] = weather_responce()


root = tk.Tk()

canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
root.title("Weather Application")
canvas.pack()

frame = tk.Frame(root, bg="deep sky blue", bd=5)
frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')

entry_field = tk.Entry(frame, font=('Courier', 12))
entry_field.place(relx=0, rely=0, relwidth=0.65, relheight=1)

button = tk.Button(frame,
                   text="Get Weather",
                   bg="gray", fg="white",
                   font=('Courier', 8),
                   command=lambda: get_weather())
button.place(relx=0.7, rely=0, relwidth=0.3, relheight=1)

lower_frame = tk.Frame(root, bg='gold', bd=10)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor='n')

label = tk.Label(lower_frame, font=('Courier', 10))
label.place(relx=0, rely=0, relwidth=1, relheight=1)

root.mainloop()
