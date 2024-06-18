from django.shortcuts import render
import requests
from django.http import HttpResponse

# Create your views here.

def get_weather(request):
    city = request.GET.get('city')
    if not city:
        return HttpResponse('<script>alert("City not provided!");</script>')

    key = "12aa12ea545dc88663f4fbf6efa60d99" 
    weather_api = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={key}&lang=ru'

    response = requests.get(weather_api)
    data = response.json()

    if data.get('cod') != 200:
        return HttpResponse(f'<script>alert("City {city} does not exist!");</script>')

    weather_info = {
        'country': data['sys']['country'],
        'city': data['name'],
        'coords': f"{data['coord']['lon']}, {data['coord']['lat']}",
        'weather': data['weather'][0]['main'],
        'temp': round(data['main']['temp'] - 273.15, 2), 
    }

    return render(request, 'weather_app/weather.html', {'weather_info': weather_info})
