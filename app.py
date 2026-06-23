import streamlit as st

from services.geocoding import get_coordinates
from services.weather import get_weather
from services.llm import generate_weather_report
from utils.weather_codes import WEATHER_CODES
from streamlit_geolocation import streamlit_geolocation
from services.reverse_geocoding import get_city_from_coordinates


st.title("AI Weather Assistant")

location = streamlit_geolocation()



with st.form("weather_form"):

    city = st.text_input(
        "Enter a city name",
        value=st.session_state.get("city", ""),
        label_visibility="visible"
    )

    use_location = st.form_submit_button(
    "📍 Use My Current Location"
)

    submitted = st.form_submit_button(
        "Get Weather"
    )

    


if submitted or use_location:

    if use_location:

        if location and location["latitude"]:

            city_name = get_city_from_coordinates(
                location["latitude"],
                location["longitude"]
            )

            st.session_state["city"] = city_name

            st.session_state["latitude"] = location["latitude"]

            st.session_state["longitude"] = location["longitude"]

            st.session_state["use_current_location"] = True

            st.rerun()

        else:

            st.warning("Please allow location access.")

    elif not city.strip():

        st.warning("Please enter a city name.")
        st.stop()

    else:

        if st.session_state.get("use_current_location"):

            coordinates = {
                "city": city,
                "latitude": st.session_state["latitude"],
                "longitude": st.session_state["longitude"]
            }

        else:

            coordinates = get_coordinates(city)

            if coordinates is None:
                st.error("City not found. Please enter a valid city name.")
                st.stop()

        with st.spinner("Generating weather report..."):

            weather = get_weather(
                coordinates["latitude"],
                coordinates["longitude"]
            )

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