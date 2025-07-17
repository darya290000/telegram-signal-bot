import requests

TOKEN = 'توکن ربات'

def get_updates():
    url = f'https://api.telegram.org/bot{TOKEN}/getUpdates'
    response = requests.get(url)
    print(response.json())

if __name__ == "__main__":
    get_updates()
