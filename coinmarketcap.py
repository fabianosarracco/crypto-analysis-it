import requests

def fetch_historical_data(date, limit=500, start=1):
    '''
    Recupera i dati storici da coinmarketcap relativi ad una giornata.
    '''
    date_string = date.strftime("%Y-%m-%d")
    url = 'https://web-api.coinmarketcap.com/v1/cryptocurrency/listings/historical?convert=USD,BTC&date=%s&limit=%d&start=%d' \
        % (date, limit, start)
    response = requests.get(url,timeout=10)
    if response.status_code != 200:
        raise Exception("Failed to load page") 
    return response.json()['data']