from django.shortcuts import render
import requests
import json 
from django.contrib import messages

# Create your views here.
def index(request):
    if request.method == 'POST':
        city=request.POST['city']
    else:
        city='Kathmandu'
    url=f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid=bf22686cf11682e29d657b984d138978"
    PARAMS={'units':'metric'}
    try:
        data=requests.get(url,PARAMS).json()
        temp=data['main']['temp']
        icon=data['weather'][0]['icon']
        description=data['weather'][0]['description']
        humidity=data['main']['humidity']
        wind=data['wind']['speed']
        return render(request,'index.html',{'temp':temp,'description':description,'city':city,'icon':icon,'humidity':humidity,'wind':wind})

    except:
        messages.error(request,'There is no such city')
        city='Kathmandu'

        return render(request,'index.html',{'temp':'23 deg','description':'clear sky','city':city,'icon':'there is no such icon','humidity':'no humidity','wind':'no wind'})

