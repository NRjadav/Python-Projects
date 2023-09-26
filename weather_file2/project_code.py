from tkinter import *
import tkinter as tk
from geopy.geocoders import Nominatim
from tkinter import ttk, messagebox
from timezonefinder import TimezoneFinder
from datetime import datetime
import pytz
import requests


#initialize window
root = Tk()
root.title("Weather App")
root.geometry("720x400+300+100")
root.config(bg="#1ab5ef")
root.resizable(False,False)


def getweather() :
    try :
        city  = textfield.get()
        # geolocator = Nominatim(user_agent="geoapiExercises")
        # location = geolocator.geocode(city)
        # obj = TimezoneFinder()
        # result = obj.timezone_at(lng=location.longitude, lat=location.latitude)
        # timezone.config(text=result)
        # long_lat.config(text=f"{round(location.latitude,4)}°N,{round(location.longitude,4)}°E")
    
        # home = pytz.timezone(result)
        # local_time = datetime.now(home)
        # current_time = local_time.strftime("%d-%m-%y %H:%M%p")
        # name.config(text="Current Time")
        # clock.config(text=current_time)
        #weather
        api = "http://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=2a55d9200bcc7d233bf1237d8a2e2884"
        json_data = requests.get(api)
        response = json_data.json()

        description = response['weather'][0]['description']
        temp = int(response['main']['temp']-273.15)
        humidity = response['main']['humidity']
        wind = response['wind']['speed']
        cloud = response['clouds']['all']
    
        t.config(text=(temp, "°c"))
        w.config(text=(wind, "mi/h"))
        h.config(text=(humidity, "%"))
        d.config(text=description)   
        c.config(text=(cloud, "%")) 
    except Exception as e:
        messagebox.showerror("Weather App", "Invalid Entry!!")
        
# Searchbox
search_image = PhotoImage(file="Rounded Rectangle 3.png")
myimage = Label(image=search_image, bg="#57adff")
myimage.place(x=30, y=50)

search_icon = PhotoImage(file="Layer 6.png")
myimage_icon = Button(image=search_icon, borderwidth=0, cursor="hand2", bg="#203243", activebackground="#20374d", command=getweather)
myimage_icon.place(x=407, y=55)


textfield =  tk.Entry(root, justify='center', width=15, font=('poppins', 25, 'bold'), bg="#203243", border=0, fg="white")
textfield.place(x=120, y=60)
textfield.focus()


#logo
weather_logo = PhotoImage(file="weather.png")
Label(root, image=weather_logo, borderwidth=-1).place(x=480, y=0)

#time
name = Label(root, font=("arial", 15, "bold"), fg="white", bg="#1ab5ef")
name.place(x=300, y=140)
clock = Label(root,font=("Helvetica", 11, "bold"), fg="white", bg="#1ab5ef")
clock.place(x=300, y=170)


# #BottomBox
frame = Frame(root, bg="#212120", height=150, width=720)
frame.pack(side=BOTTOM)

#BottmBoxes
first_box = PhotoImage(file="Rounded Rectangle 2 copy.png")
Label(root, image=first_box, bg="#212120", borderwidth=-2).place(x=75, y=265)
Label(root, image=first_box, bg="#212120", borderwidth=-2).place(x=200, y=265)
Label(root, image=first_box, bg="#212120", borderwidth=-2).place(x=320, y=265)
Label(root, image=first_box, bg="#212120", borderwidth=-2).place(x=440, y=265)
Label(root, image=first_box, bg="#212120", borderwidth=-2).place(x=560, y=265)

#Labels
label1 = Label(root, text="Temp", font=("Helvetica", 11, "bold"), fg="white", bg="#292928")
label1.place(x=92, y=275)
t = Label(root, text=". . . . .", font=("Helvetica", 11, "bold"), fg="white", bg="#292928")
t.place(x=95, y=320)

label2 = Label(root, text="Wind", font=("Helvetica", 11, "bold"), fg="white", bg="#292928")
label2.place(x=215, y=275)
w = Label(root, text="   . . . . .", font=("Helvetica", 11, "bold"), fg="white", bg="#292928")
w.place(x=205, y=320)

label3 = Label(root, text="Humidity", font=("Helvetica", 11, "bold"), fg="white", bg="#292928")
label3.place(x=325, y=275)
h = Label(root, text=". . . . .", font=("Helvetica", 11, "bold"), fg="white", bg="#292928")
h.place(x=342, y=320)

label4 = Label(root, text="Discription", font=("Helvetica", 10, "bold"), fg="white", bg="#292928")
label4.place(x=442, y=275)
d = Label(root, text=". . . . .", font=("Helvetica", 11, "bold"), fg="white", bg="#292928")
d.place(x=460, y=320)

label5 = Label(root, text="Clouds", font=("Helvetica", 11, "bold"), fg="white", bg="#292928")
label5.place(x=570, y=275)
c = Label(root, text=". . . . .", font=("Helvetica", 11, "bold"), fg="white", bg="#292928")
c.place(x=576, y=320)

#timezone
timezone = Label(root, font=("Helvetica", 15, "bold"), fg="white", bg="#57adff")
timezone.place(x=100, y=140)

long_lat = Label(root, font=("Helvetica", 11, "bold"), fg="white", bg="#57adff")
long_lat.place(x=100, y=170)










root.mainloop()