from services.geocoding import get_coordinates
from services.weather import get_weather
from services.llm import generate_weather_report


city = "Hyderabad"

coordinates = get_coordinates(city)

weather = get_weather(
    coordinates["latitude"],
    coordinates["longitude"]
)

report = generate_weather_report(weather)

print(report)