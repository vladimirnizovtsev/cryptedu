import requests

def get_coin_data():
    url = 'https://api.coingecko.com/api/v3/coins/markets'
    params = {'vs_currency': 'usd', 'order': 'market_cap_desc', 'per_page': 10}
    response = requests.get(url, params=params)
    return response.json()

def get_historical_data(coin_id):
    url = f'https://api.coingecko.com/api/v3/coins/{coin_id}/market_chart'
    params = {'vs_currency': 'usd', 'days': '30'}
    response = requests.get(url, params=params)
    return response.json()
