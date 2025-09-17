import requests
import os
from .models import CryptoCurrency, CryptoPrice
from django.conf import settings

def fetchCryptoData():
    API_KEY = settings.CMC_PRO_API_KEY
    headers = {
        "Accept": "application/json",
        "X-CMC_PRO_API_KEY": API_KEY
    }
    try:
        response = requests.get(settings.API_URL, headers=headers)
        if response.status_code != 200:
            print(f"Error fetching data: {response.status_code}, {response.text}")
            return

        data = response.json()
        print("Fetching Crypto Data...")

        for crypto in data['data']:
            name = crypto['name']
            symbol = crypto['symbol']
            price = crypto['quote']['USD']['price']

            crypto_obj, created = CryptoCurrency.objects.get_or_create(
                name=name,
                symbol=symbol
            )
            CryptoPrice.objects.create(crypto=crypto_obj, price=price)

    except Exception as e:
        print(f"Exception occurred: {e}")
