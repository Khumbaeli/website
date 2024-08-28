from django.shortcuts import render, redirect
from django.contrib import messages
from dotenv import load_dotenv
from .models import Locations
from .forms import InputLocation
import googlemaps

import requests, os, json, datetime



# Create your views here.


def index(request):
    if request.method == 'POST':
        form = InputLocation(request.POST)
        token = request.POST.get('form_token')
        if form.is_valid():
            form.save()
            return redirect('index') 

    
    locations = getLocations().all()
    ls = []
    for area in locations:
        ls.append(getWeather(area.name, area.latitude, area.longitude))

    tables = generateTables(ls)

    context = {'tables' : tables, 'form': InputLocation()}
    
    return render(request, 'conditions.html', context)   


def generateTables(data):
    htmlTables = []
    index = 0
    for crag in data:
        dt = json.loads(crag)


        html = '<table border="1">'
        html += '<tr><th>City</th>'
        html += '<th>Distance</th>'
    


        for day in dt['list']:
            date = day['dt']
            html += f'<th>{date}</th>'
        html += '</tr>'

        html += '<tr>'
        html += f'<td>{dt["city"]["name"]}</td>'

        coord = (dt['city']['coord']['lat'],dt['city']['coord']['lon'])

        html += f'<td>{ distance(coordinates=coord) }</td>'

        for day in dt['list']:
            feels_like_day = (day['feels_like']['day'])
            weather = day['weather'][0]['description']
            html += f'<td>{feels_like_day}°F<br>{weather}</td>'
        html += '</tr>'

        html += '</table>'

        index += 1
        htmlTables.append(html)
    return htmlTables

def distance(coordinates):
    load_dotenv()
    map_client = googlemaps.Client(key=os.getenv("GOOGLE_API_KEY"))

    my_coordinates = (26.3650, -80.1328)
    
    directions_result = map_client.distance_matrix(my_coordinates,
                                     coordinates,
                                     mode="driving",
                                     departure_time=datetime.datetime.now())
    return directions_result["rows"][0]["elements"][0]["duration"]["text"]

def forecast_actions(request, index):
    if request.method == 'POST':
        action = request.POST.get('action')
        location = getLocations().all()[index]
        
        if action == 'delete':
            location.delete()
            messages.success(request, 'Location deleted successfully.')
        elif action == 'move_up':
            if index > 0:
                location.up()
                messages.success(request, 'Location moved up successfully.')
            else:
                messages.warning(request, 'Location is already at the top.')
        elif action == 'move_down':
            if index < len(getLocations().all()):
                location.down()
                messages.success(request, 'Location moved down successfully.')
            else:
                messages.warning(request, 'Location is already at the bottom.')
        elif action == 'top':
            if index != 0:
                location.top()
                messages.success(request, 'Location moved to the top successfully.')
            else:
                messages.success(request, 'Location already at the top')
            
            
    return redirect('index')
            

def cut(temps, name):
    data = json.loads(temps)

    data["city"]["name"] = name

    goodTemps = [
    {
        'dt': day['dt'],
        'feels_like': day['feels_like'],
        'weather': day['weather']
    }
    for day in data['list']
    if day['feels_like']['day'] <= 70
    ]

    for days in goodTemps:
        days['dt'] = str(datetime.datetime.fromtimestamp(days['dt']).strftime('%Y-%m-%d'))
    data['list'] = goodTemps
    return json.dumps(data)

def getLocations():
    return Locations.objects

def getWeather(name, lat, lon):
    load_dotenv()
    api_key = os.getenv('WEATHER_API_KEY')

    url = f"https://pro.openweathermap.org/data/2.5/forecast/climate?lat={lat}&lon={lon}&appid={api_key}&units=imperial"
    response = requests.get(url)
    if response.status_code == 200:
    # Parse the response as JSON
        data = json.dumps(response.json())
    # Now you can work with your data
        data = cut(data, name) #cut the data up
        return data
    else:
        print(f"Request failed with status code {response.status_code}")
