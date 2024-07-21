from django.shortcuts import render
import requests, os

from .models import Locations

# Create your views here.


def index(request):
    locations = Locations.objects.all()
    context = {'all_locations': locations}
    
    return render(request, 'conditions.html', context)

def detail(request, location_name):
    context = {
        "title": "Location_name",
    }
    return render(request, "condition/" % location_name, context)

def getWeather(lat, lon):
    api_key = os.getenv("WEATHER_API_KEY")
    response = requests.get("https://api.openweathermap.org/data/3.0/onecall?lat="+lat+"&lon="+lon+"&exclude={part}&appid="+api_key)

    if response.status_code == 200:
    # Parse the response as JSON
        data = response.json()

    # Now you can work with your data
        print(data)
    else:
        print(f"Request failed with status code {response.status_code}")
