import os

from dotenv import load_dotenv
from groq import Groq


load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)


def generate_weather_report(weather_data):

    prompt = f"""
    Weather Data:
    {weather_data}

    Important Rules:

    1. Temperature values are already in Celsius (°C).
    2. Wind speed values are already in kilometers per hour (km/h).
    3. Never convert units.
    4. Never mention miles per hour (mph).
    5. Use only the units provided.

    Explain this weather in a simple and friendly way.

    Mention:
    - Temperature
    - Wind speed
    - Overall weather feeling
    - A practical suggestion for the user
    """

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response.choices[0].message.content


# weather = {
#     "temperature": 28,
#     "windspeed": 10
# }

# print(generate_weather_report(weather))