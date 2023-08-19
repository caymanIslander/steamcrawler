import argparse
import configparser
import requests
from bs4 import BeautifulSoup
import os

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--vanityUrl', help='Steam vanity URL')
    parser.add_argument('--id', help='SteamID')
    return parser.parse_args()

def read_config(filename):
    config = configparser.ConfigParser()
    config.read(filename)
    return config

def write_config(filename, config):
    with open(filename, 'w') as config_file:
        config.write(config_file)

def is_valid(init_link):
    response = requests.get(init_link)
    soup = BeautifulSoup(response.text, 'html.parser')

    if response == 200:
        print("Having problems reaching Steam.")

    error_message = {
        'en': 'The specified profile could not be found.',
        'cn': '无法找到指定的个人资料。',
        'tr': 'Belirtilen profil bulunamadı.'
    }

    for lang, message in error_message.items():
        if message in soup.get_text():
            return False, lang

    return True, None




def create_config():
    args = parse_args()
    global config
    config = read_config('config.ini')

    selection = input("For 1: Enter Steam profile vanity url\nFor 2: Enter steam id\n")

    if selection == "1":
        vanity_url_end = input("Enter the end of the vanity URL (e.g., https://steamcommunity.com/id/\033[1mSt4ck\033[0m/): ")
        init_link = "https://steamcommunity.com/id/"+vanity_url_end+"/"
        if (is_valid(init_link)):
            config['Steam']['VanityURL'] = vanity_url_end
        else:
            print("Profile not found.")
            create_config()

    elif selection == "2":
        steam_id = input("Enter your steam id:")
        init_link = "https://steamcommunity.com/id/"+steam_id+"/"
        
        if len(steam_id) > 17 or (not is_valid(init_link)):
            print("Profile not found.")
            create_config()
        else:    
            config['Steam']['ID'] = steam_id

    write_config('config.ini', config)
    print("Created config file.\n", config)

def go_to_profile():
    config_file = 'config.ini'
    Url2profile = read_config(config_file)
    response = requests.get(Url2profile)
    soup = BeautifulSoup(response.text, 'html.parser')
    level = soup.find('div', {'class': 'persona_level'}).get_text(strip=True)
    game_count = soup.find('div', {'class': 'profile_count_link_total'}).get_text(strip=True)
    screenshot_count = soup.find('a', {'data-modal-content-id': 'Screenshot'}).find('span').get_text(strip=True)
    return {
        'level': level,
        'game_count': game_count,
        'screenshot_count': screenshot_count
    }


def print_ascii_art(file_name):
    try:
        with open(file_name, 'r') as file:
            ascii_art = file.read()
            print(ascii_art)
    except FileNotFoundError:
        print("Ascii not found.")

def main():
    ascii_art_file = "ascii.txt"
    config_file = 'config.ini'

    print_ascii_art(ascii_art_file)
    if os.path.getsize(config_file) == 28:
        print("No changes in config file, creating config file.\n")
        create_config()
    else:
        go_to_profile()

    
if __name__ == '__main__':
    main()
    
