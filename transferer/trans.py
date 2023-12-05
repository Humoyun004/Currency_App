import requests

def get_currency_rate(currency_from, currency_to):
    url = f'https://cdn.jsdelivr.net/gh/fawazahmed0/currency-api@1/latest/currencies/{currency_from}/{currency_to}.json'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data.get('rates', {}).get(currency_to)
    return None
