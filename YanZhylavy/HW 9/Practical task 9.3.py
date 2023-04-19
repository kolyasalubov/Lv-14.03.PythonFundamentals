import tkinter as tk
HEIGHT = 400
WIDTH = 550
def get_weather():
      label['text'] = weather_response()



def weather_response(): 
      from pyowm import OWM
      owm = OWM('ef2206ff5da67de63306d0b143e20872')
      mgr = owm.weather_manager()
      input_city = entry_field.get()
      observation = mgr.weather_at_place(input_city)
      w = observation.weather 
      temperature = w.temperature('celsius')
      weather_info = f'Generaly, we have {w.detailed_status} here.\n' \
                     f'Wind speed is {w.wind()["speed"]} meters per second.\n' \
                     f'Current air temperature is {int(temperature["temp"])} °С.\n' \
                     f'Air humidity is {w.humidity} %'  
                               
      
      return weather_info                

  
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
                    command= get_weather)
button.place(relx=0.7, rely=0, relwidth=0.3, relheight=1)



lower_frame = tk.Frame(root, bg='deep sky blue', bd=10)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor='n')


label = tk.Label(lower_frame, font=('Courier', 11), justify='center')
label.place(relx=0, rely=0, relwidth=1, relheight=1)



root.mainloop()
