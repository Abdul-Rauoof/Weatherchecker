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

    forecasturl = f'https://api.openweathermap.org/data/2.5/forecast?q={city}&appid={settings.OPENWEATHER_API_KEY}'

    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={settings.OPENWEATHER_API_KEY}'
    PARAMS = {'units':'metric'} 

   
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

          context = {'description':description , 'icon':icon ,'temp':temp , 'date':date , 'day':day, 'city':city , 'tempmin':tempmin, 'tempmax':tempmax, 'country':country, 'sunrise':sunrise, 'sunset':sunset, 'humidity':humidity, 'forecastdata':forecastdata['list']}

          return render(request,'appname/index.html' , context )
    
    except KeyError:
          
          messages.error(request,'Incorrect City')   

          return render(request,'appname/index.html')



          


               
    
    