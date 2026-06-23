import requests


def get_city_from_coordinates(latitude, longitude):

    url = (
        f"https://nominatim.openstreetmap.org/reverse"
        f"?lat={latitude}"
        f"&lon={longitude}"
        f"&format=json"
    )

    headers = {
        "User-Agent": "AI-Weather-Assistant"
    }

    response = requests.get(
        url,
        headers=headers
    )

    data = response.json()

    print(data)

    address = data.get("address", {})

    return (
        address.get("city")
        or address.get("town")
        or address.get("village")
        or "Current Location"
    )

