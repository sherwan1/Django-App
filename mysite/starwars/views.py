from django.shortcuts import render

from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
import requests

# Create your views here.

def films(request):
	response = requests.get('https://swapi.co/api/films/')
	starwars = response.json()
	films = []
	counter = []
	films_director = []
	films_releasedate = []
	for i in range(starwars['count']):
		films.append( starwars['results'][i]['title'])
		counter.append(i)
		films_director.append(starwars['results'][i]['director'])
		films_releasedate.append(starwars['results'][i]['release_date'])

	mylist = zip(films , counter, films_director, films_releasedate)
	return render(request, 'starwars/films.html', {'films':films, 'counter':counter, 'films_director':films_director, 'films_releasedate':films_releasedate,
		'mylist':mylist})


def characters(request, id):
	response = requests.get('https://swapi.co/api/films/')
	starwars = response.json()
	characters_url = []
	characters = []

	for i in range(len(starwars['results'][int(id)]['characters'])):
		
		characters_url.append(starwars['results'][int(id)]['characters'][i])
		response1 = requests.get(characters_url[i])
		starwars2 = response1.json()
		characters.append(starwars2['name'])

	characters_url.clear()

	return render(request, 'starwars/characters.html', {'characters':characters})

	