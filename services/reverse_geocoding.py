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

    try:

        response = requests.get(
            url,
            headers=headers,
            timeout=10
        )

        if response.status_code != 200:
            return "Current Location"

        data = response.json()

        print("REVERSE DATA:", data)

        address = data.get("address", {})

        return (
            address.get("city")
            or address.get("town")
            or address.get("village")
            or address.get("suburb")
            or "Current Location"
        )

    except Exception as e:

        print("Reverse Geocoding Error:", e)

        return "Current Location"