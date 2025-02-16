from django.shortcuts import render,HttpResponse
from django.contrib import messages

from .models import CryptoPrice

from datetime import date
from django.db.models import Sum
import requests
# Create your views here.

def adminlogincheck(request):
    if request.method=='POST':
        usrid = request.POST.get('adminid')
        pswd  = request.POST.get('pswd')
        print("User ID is = ", usrid)
        if usrid == 'admin' and pswd == 'admin':
            return render(request, 'admins/adminhome.html')
        else:
            messages.success(request, 'Please Check Your Login Details')
    return render(request, 'admins.html')

def currentrate(request):
    fetch_crypto_prices()

    # Get the latest data from the database
    cryptocurrencies = CryptoPrice.objects.all()
    return render(request,'admins/cryptoratecurrent.html',{'cryptocurrencies': cryptocurrencies})

def fetch_crypto_prices():
    # CoinGecko API endpoint
    url = "https://api.coingecko.com/api/v3/simple/price"
    params = {
        "ids": "bitcoin,ethereum,dogecoin",
        "vs_currencies": "usd"
    }
    response = requests.get(url, params=params)
    data = response.json()

    # Update the prices in the database
    for crypto_name, price_info in data.items():
        crypto, created = CryptoPrice.objects.update_or_create(
            name=crypto_name.capitalize(),
            defaults={'price': price_info['usd']}
        )

