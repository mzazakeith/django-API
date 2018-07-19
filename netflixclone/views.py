from django.http import JsonResponse
from django.shortcuts import render
import requests

from netflix import settings


def date(request):
    response = requests.get('http://www.convert-unix-time.com/api?timestamp=now')
    geodata = response.json()
    # print(geodata)
    return render(request, 'date.html', {'localdata': geodata['localDate']})


def github(request):
    user = {}
    if 'username' in request.GET:
        username = request.GET['username']
        url = 'https://api.github.com/users/%s' % username
        response = requests.get(url)
        user = response.json()
    return render(request, 'github.html', {'user': user})


def movie(request):
    endpoint = 'https://api.themoviedb.org/3/movie/top_rated?api_key={api_key}&language=en-US&page=1'
    image_url = 'https://image.tmdb.org/t/p/w600_and_h900_bestv2'
    url = endpoint.format(api_key=settings.MOVIE_API_KEY)
    response = requests.get(url)
    results = response.json()
    # print(results)
    return render(request, 'movie.html', {'results': results['results'], 'image_url': image_url})


def search_youtube(request):
    items={}
    if 'search' in request.GET:
        search=request.GET["search"]
        # search ='hello'
        endpoint = 'https://www.googleapis.com/youtube/v3/search?part=snippet&order=viewCount&q='+search+'trailer'+'&type=video&videoCaption=closedCaption&key={YT_API_KEY}'
        url = endpoint.format(YT_API_KEY=settings.YT_API_KEY)
        response=requests.get(url)
        results = response.json()
        items = results['items']
    return render(request, 'youtube.html',{'items':items})
    # return render(request, 'youtube.html', {'items': results['items']})
    # return JsonResponse(results['items'], safe=False)


def netflix(request):
    endpoint = 'https://api.themoviedb.org/3/movie/top_rated?api_key={api_key}&language=en-US&page=1'
    image_url = 'https://image.tmdb.org/t/p/w600_and_h900_bestv2'
    url = endpoint.format(api_key=settings.MOVIE_API_KEY)
    response = requests.get(url)
    results = response.json()
    movies = results['results']
    search_items = []
    for movie in movies:
        search = movie['title']
        # search='avengers'
        # print(movie['title'])
        search_endpoint = 'https://www.googleapis.com/youtube/v3/search?part=snippet&order=viewCount&q='+search+'trailer'+'&type=video&videoCaption=closedCaption&key={YT_API_KEY}'
        url_search = search_endpoint.format(YT_API_KEY=settings.YT_API_KEY)
        search_response = requests.get(url_search)
        search_results = search_response.json()
        search_items.append(search_results['items'])
        # print(search_items.append(search_results['items']))
    return render(request, 'netflix.html',{'movies':movies , 'image_url': image_url,'search_items':search_items})