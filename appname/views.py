from django.shortcuts import render 
from django.contrib import messages
from django.conf import settings
import requests
import datetime


def home(request):
    day = datetime.date.today().strftime("%A")
    days = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
    temp = days[slice(0,days.index(day))]
    weakdays = days[slice(days.index(day),len(days))]
    weakdays.extend(temp)
    print(weakdays)



   
    if 'city' in request.POST:
         city = request.POST['city']
    else:
         city = 'kanpur'     


    forecasturl = f'https://api.openweathermap.org/data/2.5/forecast?q={city}&appid=a42469a41ce090cafeca8469554ee09b'

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
#     image_url = search_items[1]['link']
    

    try:
          
          forecastdata = requests.get(forecasturl,params=PARAMS).json()


          data = requests.get(url,params=PARAMS).json()
          description = data['weather'][0]['description']
          icon = data['weather'][0]['icon']
          temp = data['main']['temp']
          tempmin = data['main']['temp_min']
          tempmax = data['main']['temp_max']
          humidity = data['main']['humidity']
          country = data['sys']['country']
          sunrise = data['sys']['sunrise']
          sunset = data['sys']['sunset']

          date = datetime.date.today()
          day = datetime.date.today().strftime("%A")

          context = {'description':description , 'icon':icon ,'temp':temp , 'date':date , 'day':day, 'city':city , 'tempmin':tempmin, 'tempmax':tempmax, 'country':country, 'sunrise':sunrise, 'sunset':sunset, 'humidity':humidity, 'weakdays':weakdays, 'forecastdata':forecastdata['list'][slice(0,7)]}

          return render(request,'appname/index.html' , context )
    
    except KeyError:
          
          messages.error(request,'Incorrect City')   
          day = datetime.date.today()

          return render(request,'appname/index.html')
               
    
    