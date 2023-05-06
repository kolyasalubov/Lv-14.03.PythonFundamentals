import tkinter as tk
from tkinter import font
from OWM import mgr

HEIGHT = 350
WIDTH = 450


root = tk.Tk()


canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
root.title("Weather Application")
canvas.pack()

def get_weather(c):
    weather = mgr.weather_at_place(c).weather
    label['text'] = f"""
                    Clouds: {weather.detailed_status},
                    Wind Speed: {weather.wind()['speed']},
                    Wind degrees: {weather.wind()['deg']},
                    Humidity: {weather.humidity}%,\n
                    Temperature: {weather.temperature('celsius')['temp']}°C,
                    Temperature max: {weather.temperature('celsius')['temp_max']}°C,
                    Temperature min: {weather.temperature('celsius')['temp_min']}°C,
                    Rain: {weather.rain},
                    Heat index: {weather.heat_index},
                    Cloudiness: {weather.clouds}%"""
                    

frame = tk.Frame(root, bg="deep sky blue", bd=5)
frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')

entry_field = tk.Entry(frame, font=('Courier', 12))
entry_field.place(relx=0, rely=0, relwidth=0.65, relheight=1)

button = tk.Button(frame, 
                   text="Get Weather", 
                   bg="gray", fg="white", 
                   font=('Courier', 8), 
                   command=lambda: get_weather(entry_field.get()))
button.place(relx=0.7, rely=0, relwidth=0.3, relheight=1)



lower_frame = tk.Frame(root, bg='gold', bd=10)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.7, anchor='n')


label = tk.Label(lower_frame, font=('Courier', 10), justify='left', anchor='e')
label.place(relx=0, rely=0, relwidth=1, relheight=1)



root.mainloop()
