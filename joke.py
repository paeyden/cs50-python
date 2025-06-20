import requests
import sys

def main():
    try:
        url = "https://official-joke-api.appspot.com/random_joke"
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        print(f"{data[data]}")
    except requests.RequestException:
        sys.exit()
        
main()