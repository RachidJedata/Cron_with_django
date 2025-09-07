from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from .models import CryptoCurrency

def show_crypto_data(request):
    bitCoin = get_object_or_404(CryptoCurrency, name="Bitcoin")
    prices = bitCoin.prices.order_by('-timestamp')[:10]

    data = [
        {"price": str(p.price), "timestamp": p.timestamp}
        for p in prices
    ]
    return JsonResponse(data, safe=False)
