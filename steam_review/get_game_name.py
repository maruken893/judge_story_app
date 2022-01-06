import requests
from bs4 import BeautifulSoup

def get_game_name(id):
    res = requests.get('https://store.steampowered.com/app/{game_id}'.replace('{game_id}', str(id)))
    soup = BeautifulSoup(res.text, "html.parser")
    title = str(soup.find('div', attrs={'class': 'apphub_AppName'}))[28:][:-6]
    return title

