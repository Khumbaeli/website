from django.shortcuts import render
from dotenv import load_dotenv
import requests, os, json, datetime

from .models import Locations

# Create your views here.


def index(request):
    
    locations = Locations.objects.all()
    ls = []
    for area in locations:
        ls.append(getWeather(area.latitude, area.longitude))

    tables = generateTables(ls)

    context = {'all_locations': tables}
    
    return render(request, 'conditions.html', context)

def generateTables(data):
    htmlTables = []
    for crag in data:
        dt = json.loads(crag)

        html = '<table border="1">'
        html += '<tr><th>City</th>'


        for day in dt['list']:
            date = day['dt']
            html += f'<th>{date}</th>'
        html += '</tr>'

        html += '<tr>'
        html += f'<td>{dt["city"]["name"]}</td>'

        for day in dt['list']:
            feels_like_day = (day['feels_like']['day'])
            weather = day['weather'][0]['description']
            html += f'<td>{feels_like_day}°F<br>{weather}</td>'
        html += '</tr>'

        html += '</table>'

        htmlTables.append(html)
    return htmlTables

def cut(temps):
    data = json.loads(temps)

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

def getWeather(lat, lon):
    load_dotenv()
    api_key = os.getenv('WEATHER_API_KEY')

    url = f"https://pro.openweathermap.org/data/2.5/forecast/climate?lat={lat}&lon={lon}&appid={api_key}&units=imperial"
    response = requests.get(url)
    if response.status_code == 200:
    # Parse the response as JSON
        data = json.dumps(response.json())
    # Now you can work with your data
        data = cut(data) #cut the data up
        return data
    else:
        print(f"Request failed with status code {response.status_code}")
