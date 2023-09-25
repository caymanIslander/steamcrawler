import requests
from bs4 import BeautifulSoup
import configparser

config = configparser.ConfigParser()
config.read('config.ini')

def construct_url(config):
    vanity_url = config.get('Steam', 'vanityurl', fallback=None)
    print(vanity_url)


construct_url(config)

    
response = requests.get("https://steamcommunity.com/id/abc/")
soup = BeautifulSoup(response.text, 'html.parser')

profile_counts = soup.find_all('span', {'class': 'profile_count_link_total'})#.getText(strip=True)

level = soup.find('span', {'class': 'friendPlayerLevelNum'}).getText(strip=True)
badge_count = profile_counts[0].getText(strip=True)
game_count = profile_counts[1].getText(strip=True)
#screenshot_count = profile_counts[4]


#print(level,badge_count,game_count,screenshot_count)
print(game_count)


#screenshot_count = soup.find('a', {'data-modal-content-id': 'Screenshot'})#.find('span').getText(strip=True)


