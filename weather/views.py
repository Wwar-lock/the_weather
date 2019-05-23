import requests
from django.shortcuts import render

def index(request):
    url = 'http://api.openweathermap.org/data/2.5/weather?q=London,uk&APPID=7bb08d2a6c908beeeb03fb23231b711e'
    city = 'Las Vegas'

    r = requests.get(url.format(city))
    print(r.text)

    return render(request,'weather/weather.html')
    
