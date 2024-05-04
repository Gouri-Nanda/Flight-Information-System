from django.shortcuts import render


import requests

def index(request):
    if request.method == 'POST':
        origin = request.POST.get("Origin")
        destination = request.POST.get("Destination")
        departure_date = request.POST.get("Departure_date")
        api_url = f'http://127.0.0.1:8000/flights/{origin}/{destination}/{departure_date}/'  # Replace with your API endpoint URL
        response = requests.get(api_url)
        flight_data = response.json()
        if response.status_code == 200:
            flight_data = response.json()
            return render(request, 'info.html', {'flight_data': flight_data})
        else:
            return render(request, 'index.html', {'message': 'Oopss!! Looks like no flights are available.'})
    
        
    return render(request, 'index.html')


