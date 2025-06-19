import requests


def random_facts():
    try:
        response = requests.get("https://catfact.ninja/fact")
        response.raise_for_status()
        data = response.json()
        print(f"Cat fact: {data["fact"]}")
    except requests.RequestException:
        print("Something went wrong while fetching the cat fact.")
        
random_facts()