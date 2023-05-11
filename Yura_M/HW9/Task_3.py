from pyowm import OWM
import Task_3_config
import tkinter as tk


try:
    def weather_responce():
        owm = OWM(Task_3_config.API_KEY)
        mgr = owm.weather_manager()

        input_city = entry_field.get()  # input("What city you are interested: ")

        observation = mgr.weather_at_place(input_city)
        w = observation.weather
        speed_wind = w.wind()['speed']
        humidity = w.humidity                # 87

        temperature_max = w.temperature('celsius')['temp_max']
        temperature = w.temperature('celsius')['temp']
        temperature_min = w.temperature('celsius')['temp_min']
        w.rain
        w.heat_index
        w.clouds

        return f"""
        In {input_city} the wind speed is {speed_wind} km/hours
        In {input_city} the humidity of the air is {humidity}
        In {input_city} thetemperature of the air is {temperature}
        In {input_city} the maximal temperature of the air is {temperature_max}
        In {input_city} the minimal temperature of the air is {temperature_min}
        """
except:
    print(''' Ooops!!! Thera was a problem \n retrieving that information.!!!''')


def get_weather():
    label['text'] = weather_responce()


HEIGHT = 500
WIDTH = 800

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
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75,
                  relheight=0.6, anchor='n')

label = tk.Label(lower_frame, font=('Courier', 10))
label.place(relx=0, rely=0, relwidth=1, relheight=1)

root.mainloop()
