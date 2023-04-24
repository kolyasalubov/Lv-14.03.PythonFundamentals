from pyowm import OWM
import tkinter as tk
from api import API_KEY



HEIGHT = 350
WIDTH = 450



def weather_response():
  owm = OWM(API_KEY)
  mgr = owm.weather_manager()
  try:
    observation = mgr.weather_at_place(city.get())
    w = observation.weather
    weather = f'''City: {city.get()}
               \nConditions: {str(w.detailed_status)}
               \nTemperature is {str(round(w.temperature('celsius')['temp'], 2))} 
               \nWind speed is {str(w.wind()['speed'])} km/hours
               \nHumidity of the air is {str(w.humidity)} '''
    return weather
  except:
    return 'Something went wrong :('

def get_weather():
  label['text'] = weather_response()
  return


root = tk.Tk()


canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
root.title("Weather Application")
canvas.pack()


frame = tk.Frame(root, bg="deep sky blue", bd=5)
frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')

city = tk.StringVar()
entry_field = tk.Entry(frame,
                       font=('Courier', 12),
                       textvariable=city)
entry_field.place(relx=0, rely=0, relwidth=0.65, relheight=1)


button = tk.Button(frame,
                   text="Get Weather",
                   bg="gold", fg="black",
                   font=('Courier', 8),
                   command=lambda: get_weather())
button.place(relx=0.7, rely=0, relwidth=0.3, relheight=1)


lower_frame = tk.Frame(root, bg='deep sky blue', bd=3)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor='n')


label = tk.Label(lower_frame, font=('Courier', 14))
label.place(relx=0, rely=0, relwidth=1, relheight=1)


root.mainloop()