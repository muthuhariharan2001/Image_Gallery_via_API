from django.shortcuts import render
from django.http import JsonResponse
import requests

# Pexels API key
PEXELS_API_KEY = '0ugYYg8ReFflTabOpFvbOapK8SFFGuHOLHk4q0CNfE7cO3rtHjQaRoan'
PEXELS_API_URL = 'https://api.pexels.com/v1/search'

def index(request):
    return render(request, 'index.html')

def search_images(request):
    query = request.GET.get('query')
    headers = {
        'Authorization': PEXELS_API_KEY
    }
    params = {
        'query': query,
        'per_page': 50
    }
    response = requests.get(PEXELS_API_URL, headers=headers, params=params)
    data = response.json()
    images = [{'url': photo['src']['medium'], 'description': photo.get('alt', 'No description available')} for photo in data['photos']]
    return JsonResponse(images, safe=False)
