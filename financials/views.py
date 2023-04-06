from django.http import HttpResponse
from django.shortcuts import render
import requests

# Create your views here.
def index(request):
    return HttpResponse("Hello")

def stock_info(request):
    api_key = 'd2b1cf9beb66264ece3054788678d1b4'
    symbol = 'AAPL'  # Replace with the stock symbol of your choice

    url = f'https://financialmodelingprep.com/api/v3/quote/{symbol}?apikey={api_key}'
    response = requests.get(url)
    stock_data = response.json()

    context = {
        'symbol': stock_data[0]['symbol'],
        'name': stock_data[0]['name'],
        'price': stock_data[0]['price'],
        'change': stock_data[0]['change'],
        'change_pct': stock_data[0]['changesPercentage'],
    }

    return render(request, 'stock_info.html', context)

