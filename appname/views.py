from django.shortcuts import render 
from django.contrib import messages
from django.conf import settings
import requests
import datetime


def home(request):
   
    if 'city' in request.POST:
         city = request.POST['city']
    else:
         city = 'kanpur'     
    
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid=a42469a41ce090cafeca8469554ee09b'
    PARAMS = {'units':'metric'}

    apikey =  settings.API_KEY

    searchengineid = settings.SEARCH_ENGINE_ID
     
    query = city + " 1920x1080"
    page = 1
    start = (page - 1) * 10 + 1
    searchType = 'image'
    city_url = f"https://www.googleapis.com/customsearch/v1?key={apikey}&cx={searchengineid}&q={query}&start={start}&searchType={searchType}&imgSize=xlarge"

    data = requests.get(city_url).json()
    count = 1
    search_items = data.get("items")
    image_url = search_items[1]['link']
    

    try:
          
          data = requests.get(url,params=PARAMS).json()
          description = data['weather'][0]['description']
          icon = data['weather'][0]['icon']
          temp = data['main']['temp']
          day = datetime.date.today()

          return render(request,'appname/index.html' , {'description':description , 'icon':icon ,'temp':temp , 'day':day , 'city':city ,'image_url':image_url})
    
    except KeyError:
          
          messages.error(request,'Incorrect City name')   
          day = datetime.date.today()

          return render(request,'appname/index.html' ,{'description':'clear sky', 'icon':'01d'  ,'temp':25 , 'day':day , 'city':city } )
               
    
    