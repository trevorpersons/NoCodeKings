from django.http import HttpResponse
from django.shortcuts import render
import plotly.graph_objs as go
import requests

# Create your views here.


def index(request):
    return render(request, 'index2.html')


def stock_info(request):
    api_key = 'd2b1cf9beb66264ece3054788678d1b4'

    if request.method == 'POST':
        symbol = request.POST.get('symbol', 'AAPL')
    else:
        symbol = 'AAPL'

    url = f'https://financialmodelingprep.com/api/v3/quote/{symbol}?apikey={api_key}&exchange=NYSE,NASDAQ'
    response = requests.get(url)
    stock_data = response.json()

    context = {
        'symbol': stock_data[0]['symbol'],
        'name': stock_data[0]['name'],
        'price': stock_data[0]['price'],
        'change': stock_data[0]['change'],
        'change_pct': stock_data[0]['changesPercentage']+"%",
        'dayLow': stock_data[0]['dayLow'],
        'dayHigh': stock_data[0]['dayHigh'],
        'yearLow': stock_data[0]['yearLow'],
        'yearHigh': stock_data[0]['yearHigh'],
        'marketCap': stock_data[0]['marketCap'],
        'exchange': stock_data[0]['exchange'],
    }

    return render(request, 'stock_info.html', context)


def stock_chart(request, symbol):
    api_key = 'd2b1cf9beb66264ece3054788678d1b4'

    # Get stock price data from API
    url = f'https://financialmodelingprep.com/api/v3/historical-price-full/{symbol}?apikey={api_key}'
    response = requests.get(url)
    stock_data = response.json()['historical']

    # Format the data for use with plotly
    dates = []
    open_prices = []
    high_prices = []
    low_prices = []
    close_prices = []
    for day in stock_data:
        dates.append(day['date'])
        open_prices.append(day['open'])
        high_prices.append(day['high'])
        low_prices.append(day['low'])
        close_prices.append(day['close'])
    candlestick_data = go.Candlestick(
        x=dates,
        open=open_prices,
        high=high_prices,
        low=low_prices,
        close=close_prices
    )
    chart_layout = go.Layout(
        title=f"{symbol} Candlestick Chart",
        xaxis={'title': 'Date'},
        yaxis={'title': 'Price'}
    )
    chart_data = [candlestick_data]
    chart_figure = go.Figure(data=chart_data, layout=chart_layout)
    chart_div = chart_figure.to_html(full_html=False)

    context = {
        'symbol': symbol,
        'chart_div': chart_div
    }
    return render(request, 'stock_chart.html', context)

