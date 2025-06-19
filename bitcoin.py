import requests
import sys

def main():
    if len(sys.argv) != 2:
        sys.exit("Missing command-line argument.")

    try:
        bitcoins = float(sys.argv[1])
    except ValueError:
        sys.exit("Command-line argument is not a number.")

    try:
        url = "https://api.coincap.io/v3/assets/bitcoin"
        headers = {
            "Authorization": "Bearer 3b28b7004d59997308870b3dc598b666cbe2a38fd14f35756a46d364dbed62ef"
        }
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        data = response.json()
        price = float(data["data"]["priceUsd"])
        total = bitcoins * price
        print(f"${total:,.4f}")
    except requests.RequestException:
        sys.exit("Error: Failed to fetch Bitcoin price.")

if __name__ == "__main__":
    main()
