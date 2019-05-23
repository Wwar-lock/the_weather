import requests
from django.shortcuts import render

def index(request):
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&APPID=7bb08d2a6c908beeeb03fb23231b711e'
    city = 'Dehradun'

    r = requests.get(url.format(city)).json()      # json object
    # print(r.text)

    city_weather = {
        'city':  city,
        'temprature' : r['main']['temp'],
        'description' : r['weather'][0]['description'],
        'icon' : r['weather'][0]['icon'],
    }

    print(city_weather['city'])

    context = {'city_weather':city_weather}

    return render(request,'weather/weather.html',context)
    
