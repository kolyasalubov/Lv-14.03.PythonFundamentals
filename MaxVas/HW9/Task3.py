import tkinter as tk
from pyowm import OWM

HEIGHT = 350
WIDTH = 450


def get_weather():
  owm = OWM('ef2206ff5da67de63306d0b143e20872')
  mgr = owm.weather_manager()
  observation = mgr.weather_at_place(entry_field.get())
  w = observation.weather

  w.detailed_status
  w.wind()
  w.humidity
  w.temperature('celsius')
  w.rain
  w.heat_index
  w.clouds
  output = f"City: {entry_field.get()}\nConditions: {w.detailed_status }\nTemperature is  {round(w.temperature('celsius')['temp'], 2)} C\nWind speed is {w.wind()['speed']} km/hours\nHumidity of the air is {w.humidity}"
  label = tk.Label(lower_frame, text=output, font=("Arial", 16))
  label.grid(row=0, column=0)


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
                   bg="gray",
                   fg="white",
                   font=('Courier', 8),
                   command=lambda: get_weather())
button.place(relx=0.7, rely=0, relwidth=0.3, relheight=1)

lower_frame = tk.Frame(root, bg='gold', bd=10)
lower_frame.place(relx=0.5,
                  rely=0.25,
                  relwidth=0.75,
                  relheight=0.6,
                  anchor='n')

label = tk.Label(lower_frame, font=('Courier', 14))
label.place(relx=0, rely=0, relwidth=1, relheight=1)

root.mainloop()
