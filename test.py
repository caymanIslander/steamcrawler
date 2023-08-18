import argparse
import configparser
import requests

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

def create_config():
    args = parse_args()
    config = read_config('config.ini')

    selection = input("For 1: Enter Steam profile vanity url\nFor 2: Enter steam id\n")

    if selection == "1":
        vanity_url_end = input("Enter the end of the vanity URL (e.g., https://steamcommunity.com/id/\033[1mSt4ck\033[0m/): ")
        init_link = "https://steamcommunity.com/id/"+vanity_url_end+"/"
        response = requests.get(init_link)
        if response == 200:
            print("Profile not found.")
            create_config()
        else:    
            config['Steam']['VanityURL'] = vanity_url_end

    elif selection == "2":
        steam_id = input("Enter your steam id:")
        init_link = "https://steamcommunity.com/id/"+steam_id+"/"
        response = requests.get(init_link)
        if response == 200 or len(steam_id) > 17:
            print("Profile not found.")
            create_config()
        else:    
            config['Steam']['ID'] = steam_id

    write_config('config.ini', config)
    print("Created config file.\n", config)


if __name__ == '__main__':
    create_config()
