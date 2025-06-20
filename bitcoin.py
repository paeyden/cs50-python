import requests
import sys

def api():
    if len(sys.argv) != 2:
        sys.exit("Missing command-line argument.")

    try:
        bitcoins = float(sys.argv[1])
    except ValueError:
        sys.exit("Command-line argument is not a number.")

    try:
        url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd"
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        price = float(data["bitcoin"]["usd"])
        total = bitcoins * price
        print(f"${total:,.4f}")
    except requests.RequestException:
        sys.exit("Error: Failed to fetch Bitcoin price.")

if __name__ == "__main__":
    api()
