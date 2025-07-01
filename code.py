from tkinter import *
import requests
import datetime
from PIL import ImageTk, Image

# API details
API_KEY = "eb35883a9381e6fcba10db7e3ef9a636"  # Replace with your actual API key
BASE_URL = "http://api.openweathermap.org/data/2.5/weather?"

# Create window
root = Tk()
root.title("Weather App")
root.geometry("450x700")
root.configure(background="white")

# Load static logo
logo_img = ImageTk.PhotoImage(Image.open("logo.png"))
logo_panel = Label(root, image=logo_img, bg="white")
logo_panel.place(x=100, y=10)

# Entry box
city_entry = Entry(root, justify='center', width=30, font=("poppins", 14, "bold"))
city_entry.place(x=75, y=150)
city_entry.focus()

# Dynamic weather icon label (will change)
img_panel = Label(root, bg="white")
img_panel.place(x=130, y=350)

# Load both icons for switching
sun_icon = ImageTk.PhotoImage(Image.open("sun.png"))
moon_icon = ImageTk.PhotoImage(Image.open("moon.png"))

def fetch_weather():
    city = city_entry.get()
    if not city:
        return

    url = f"{BASE_URL}appid={API_KEY}&q={city}&units=metric"
    response = requests.get(url)
    data = response.json()

    if data["cod"] != 200:
        lable_citi.config(text="City Not Found")
        return

    weather = data["weather"][0]["main"]
    temp = data["main"]["temp"]
    humidity = data["main"]["humidity"]
    temp_max = data["main"]["temp_max"]
    temp_min = data["main"]["temp_min"]
    description = data["weather"][0]["description"]
    icon_code = data["weather"][0]["icon"]

    # Get current time details
    now = datetime.datetime.now()
    day = now.strftime("%A")
    date = now.strftime("%d %B")
    time = now.strftime("%I : %M %p")

    # Determine icon (day vs night)
    if "d" in icon_code:
        img_panel.config(image=sun_icon)
        img_panel.image = sun_icon
    else:
        img_panel.config(image=moon_icon)
        img_panel.image = moon_icon

    # Update labels
    lable_temp.config(text=f"{temp:.1f}°C")
    lable_citi.config(text=data["name"])
    lable_desc.config(text=description.title())
    lable_day.config(text=day)
    lable_date.config(text=date)
    lable_time.config(text=time)
    lable_humidity.config(text=f"Humidity: {humidity}%")
    max_temp.config(text=f"Max. Temp.: {temp_max:.1f}°C")
    min_temp.config(text=f"Min. Temp.: {temp_min:.1f}°C")

# Search button
search_button = Button(root, text="Search", command=fetch_weather, font=("poppins", 12, "bold"))
search_button.place(x=180, y=200)

# Labels
lable_citi = Label(root, text="", font=("poppins", 18, "bold"), bg="white")
lable_citi.place(x=150, y=250)

lable_day = Label(root, text="", font=("Helvetica", 10), bg="white")
lable_day.place(x=30, y=290)

lable_date = Label(root, text="", font=("Helvetica", 10), bg="white")
lable_date.place(x=300, y=290)

lable_time = Label(root, text="", font=("Helvetica", 10), bg="white")
lable_time.place(x=30, y=320)

lable_desc = Label(root, text="", font=("Helvetica", 14), bg="white")
lable_desc.place(x=160, y=460)

lable_temp = Label(root, text="", font=("poppins", 20, "bold"), bg="white")
lable_temp.place(x=180, y=500)

lable_humidity = Label(root, text="", font=("Helvetica", 10), bg="white")
lable_humidity.place(x=100, y=550)

max_temp = Label(root, text="", font=("Helvetica", 10), bg="white")
max_temp.place(x=100, y=580)

min_temp = Label(root, text="", font=("Helvetica", 10), bg="white")
min_temp.place(x=100, y=610)

footer = Label(root, text="All temperatures in degree Celsius", font=("Helvetica", 8), bg="white")
footer.place(x=120, y=640)

root.mainloop()
