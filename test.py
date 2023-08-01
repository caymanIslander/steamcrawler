import requests
from bs4 import BeautifulSoup




    



def fetch():
    selection = input("For 1: Enter Steam profile custom url \n For 2: Enter steam id \n")
    if selection == "1":
        custom_url_end = input("Enter the end of the custom URL (e.g., https://steamcommunity.com/id/\033[1mSt4ck\033[0m/): ")
        URL = "https://steamcommunity.com/id/"+custom_url_end+"/"
        response = requests.get(URL)
        if response != 200:
            soup = BeautifulSoup()
            profile_name = soup.find('span', {'class': 'actual_persona_name'})
            print(profile_name)

    elif selection == "2":
        URL_end = input("Enter your steam id:")
        
        response = requests.get(URL)

        if URL.length() != 17 or response != 200 :
            print("Your steam id is wrong or the page is not available...")
        else:
            soup = BeautifulSoup()
            profile_name = soup.find('span', {'class': 'actual_persona_name'})
            print(profile_name)

fetch()