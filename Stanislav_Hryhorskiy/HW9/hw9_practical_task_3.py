# *** Practical task 3 ***
# You need to combine two programs OWM.py and Tk_OWM.py
# into one working program.

import tkinter as tk
from datetime import datetime
from pyowm import OWM
from config_task_2 import API_KEY

HEIGHT, WIDTH = 400, 500
current_datetime = str(datetime.now())


def weather_response():
    try:
        owm = OWM(API_KEY)
        mgr = owm.weather_manager()
        observation = mgr.weather_at_place(entry_field.get())
        w = observation.weather
        temp_dict = w.temperature("celsius")
        presence = w.rain if w.rain else '0'
        response = f'Weather in locality {entry_field.get().title()} \non {current_datetime[:10]} ' \
                   f'(time {current_datetime[11:19]}):\n' \
                   f'- detailed status: {w.detailed_status};\n' \
                   f'- actual air temperature {int(temp_dict["temp"])} °С;\n' \
                   f'- minimum daily air temperature {int(temp_dict["temp_min"])} °С;\n' \
                   f'- maximum daily air temperature {int(temp_dict["temp_max"])} °С;\n' \
                   f'- the temperature feels like {int(temp_dict["feels_like"])} °С;\n' \
                   f'- wind speed {round(w.wind()["speed"], 1)} m/s, direction {w.wind()["deg"]} deg.;\n' \
                   f'- relative air humidity {w.humidity} %;\n' \
                   f'- cloud cover {w.clouds} %;\n' \
                   f'- precipitation probability: {presence}.'
        return response
    except:
        return 'Oops! Something went wrong.\n' \
               'Check that you have correctly entered\n' \
               'the name of the location to display the weather!'


def get_weather():
    label['text'] = weather_response()


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
                   bg="green", fg="white",
                   font=('Arial', 10),
                   command=lambda: get_weather())
button.place(relx=0.7, rely=0, relwidth=0.3, relheight=1)

lower_frame = tk.Frame(root, bg='gold', bd=10)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor='n')

label = tk.Label(lower_frame, font=('Arial', 11), justify='left')
label.place(relx=0, rely=0, relwidth=1, relheight=1)

root.mainloop()
