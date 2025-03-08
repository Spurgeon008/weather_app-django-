from django.shortcuts import render
import requests

def get_weather(request):
    city = request.GET.get('city', 'New York')  
    api_key = "9290644557db78227d3e26b24e99a42b"
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        data = response.json()

        weather_data = {
            "temperature": data["main"]["temp"],
            "weather": data["weather"][0]["description"],
            "city": city
        }
        return render(request, 'weather/index.html', {'weather_data': weather_data})
    
    except requests.exceptions.RequestException as e:
        error = f"Failed to fetch weather data: {str(e)}"
        return render(request, 'weather/index.html', {'error': error})