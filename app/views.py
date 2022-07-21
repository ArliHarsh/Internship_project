import requests
from django.shortcuts import render

# Create your views here.

def index(request):
    records = {}
    url = "https://inshortsapi.vercel.app/news?category=all"
    response = requests.get(url=url)
    inshorts_data = response.json
    records['alldata'] = inshorts_data
    return render(request, 'index.html', records)

def sports(request):
    records = {}
    url = "https://inshortsapi.vercel.app/news?category=sports"
    response = requests.get(url=url)
    inshorts_data = response.json
    records['sportsdata'] = inshorts_data
    return render(request, 'sports.html', records)

def entertainment(request):
    records = {}
    url = "https://inshortsapi.vercel.app/news?category=entertainment"
    response = requests.get(url=url)
    inshorts_data = response.json
    records['entertainmentdata'] = inshorts_data
    return render(request, 'entertainment.html', records)

def business(request):
    records = {}
    url = "https://inshortsapi.vercel.app/news?category=business"
    response = requests.get(url=url)
    inshort_data = response.json()
    records['businessdata'] = inshort_data
    return render(request, 'business.html', records)

def politics(request):
    records = {}
    url = "https://inshortsapi.vercel.app/news?category=politics"
    response = requests.get(url=url)
    inshorts_data = response.json()
    records['politicsdata'] = inshorts_data
    return render(request, 'politics.html', records)

def startup(request):
    records = {}
    url = "https://inshortsapi.vercel.app/news?category=startup"
    response = requests.get(url=url)
    inshorts_data = response.json()
    records['startupdata'] = inshorts_data
    return render(request, 'startup.html', records)

def world(request):
    records = {}
    url = "https://inshortsapi.vercel.app/news?category=world"
    response = requests.get(url=url)
    inshorts_data = response.json()
    records['worlddata'] = inshorts_data
    return render(request, 'world.html', records)

def tech(request):
    records = {}
    url = "https://inshortsapi.vercel.app/news?category=technology"
    response = requests.get(url=url)
    inshorts_data = response.json()
    records['techdata'] = inshorts_data
    return render(request, 'tech.html', records)

def national(request):
    records = {}
    url = "https://inshortsapi.vercel.app/news?category=national"
    response = requests.get(url=url)
    inshorts_data = response.json()
    records['nationaldata'] = inshorts_data
    return render(request, 'national.html', records)

def miscellaneous(request):
    records = {}
    url = "https://inshortsapi.vercel.app/news?category=miscellaneous"
    response = requests.get(url=url)
    inshorts_data = response.json()
    records['miscellaneousdata'] = inshorts_data
    return render(request, 'miscellaneous.html', records)

def hatke(request):
    records = {}
    url = "https://inshortsapi.vercel.app/news?category=hatke"
    response = requests.get(url=url)
    inshorts_data = response.json()
    records['hatkedata'] = inshorts_data
    return render(request, 'hatke.html', records)

def science(request):
    records = {}
    url = "https://inshortsapi.vercel.app/news?category=science"
    response = requests.get(url=url)
    inshorts_data = response.json()
    records['sciencedata'] = inshorts_data
    return render(request, 'science.html', records)

def automobile(request):
    records = {}
    url = "https://inshortsapi.vercel.app/news?category=automobile"
    response = requests.get(url=url)
    inshorts_data = response.json()
    records['automobiledata'] = inshorts_data
    return render(request, 'automobile.html', records)







