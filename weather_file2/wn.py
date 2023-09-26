# ... (your existing imports and code)

import geocoder
import requests

# ... (your existing functions and UI elements)

def get_user_location():
    try:
        # Fetch user's location based on their IP address
        g = geocoder.ip('me')
        return g.latlng
    except Exception as e:
        print("Error fetching user location:", e)
        return None

def getweather():
    try:
        # Get the user's location
        user_location = get_user_location()

        if user_location:
            latitude, longitude = user_location

            # Use latitude and longitude to fetch weather data
            api = f"https://api.openweathermap.org/data/2.5/weather?lat={latitude}&lon={longitude}&appid=2a55d9200bcc7d233bf1237d8a2e2884"
            json_data = requests.get(api).json()

            # ... (rest of your weather data fetching and display code)

        else:
            print("ok1")
    except Exception as e:
        print("ok")
# ... (the rest of your code)




get_user_location()
getweather()