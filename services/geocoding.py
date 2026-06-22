import requests


def get_coordinates(city):

    url = (
        f"https://geocoding-api.open-meteo.com/v1/search"
        f"?name={city}&count=1"
    )

    response = requests.get(url)

    data = response.json()

    if "results" not in data:
        return None

    location = data["results"][0]

    return {
        "city": location["name"],
        "latitude": location["latitude"],
        "longitude": location["longitude"]
    }


# print(get_coordinates("Hyderabad"))