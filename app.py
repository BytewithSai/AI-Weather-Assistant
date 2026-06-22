import streamlit as st

from services.geocoding import get_coordinates
from services.weather import get_weather
from services.llm import generate_weather_report
from utils.weather_codes import WEATHER_CODES


st.title("AI Weather Assistant")

with st.form("weather_form"):

    city = st.text_input(
    "Enter a city name",
    label_visibility="visible"
    )

    submitted = st.form_submit_button("Get Weather")


if submitted:

    if not city.strip():
        st.warning("Please enter a city name.")
    
    else:

        with st.spinner("Generating weather report..."):

            coordinates = get_coordinates(city)

            if coordinates is None:
                st.error("City not found. Please enter a valid city name.")

            else:

                weather = get_weather(
                    coordinates["latitude"],
                    coordinates["longitude"]
                )
                # st.write(weather)

                st.subheader(f"📍 {coordinates['city']}")

                condition = WEATHER_CODES.get(
                weather["weathercode"],
                "Weather condition unavailable"
                )

                st.write(condition)

                st.caption(f"Last Updated: {weather['time']}")

                col1, col2 = st.columns(2)

                with col1:
                    st.metric(
                        "Temperature",
                        f"{weather['temperature']} °C"
                    )

                with col2:
                    st.metric(
                        "Wind Speed",
                        f"{weather['windspeed']} km/h"
                    )

                report = generate_weather_report(weather)

                st.subheader("AI Weather Summary")

                st.info(report)