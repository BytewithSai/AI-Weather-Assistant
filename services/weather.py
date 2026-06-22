import requests


def get_weather(latitude, longitude):

    url = (
        f"https://api.open-meteo.com/v1/forecast"
        f"?latitude={latitude}"
        f"&longitude={longitude}"
        f"&current_weather=true"
    )

    response = requests.get(url)

    data = response.json()

    return {
        "temperature": data["current_weather"]["temperature"],
        "windspeed": data["current_weather"]["windspeed"],
        "weathercode": data["current_weather"]["weathercode"],
        "time": data["current_weather"]["time"]
    }


print(get_weather(17.38405, 78.45636))