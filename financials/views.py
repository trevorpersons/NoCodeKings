from django.http import HttpResponse
from django.shortcuts import render 
import requests

# Create your views here.
def index(request):
    return render(request, 'index2.html')

def stock_info(request, symbol=None):
    
    if symbol is None:
        symbol = 'AAPL'
    url = f'https://financialmodelingprep.com/api/v3/quote/{symbol}?apikey=d2b1cf9beb66264ece3054788678d1b4'
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

