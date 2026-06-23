# 🌦️ AI Weather Assistant

An AI-powered weather application built with Streamlit, Open-Meteo APIs, Reverse Geocoding, and Groq LLM.

## 🚀 Live Demo

https://ai-weather-assistant-irnb8hbo7jzd38jtior8fk.streamlit.app/

## 📌 Project Overview

AI Weather Assistant allows users to:

* Search weather by city name
* Use live GPS location
* View current weather conditions
* Get AI-generated weather summaries
* Access weather information through a simple web interface

This project demonstrates how traditional APIs and Large Language Models can be combined to build practical AI applications.

---

## ✨ Features

### 🌍 City-Based Weather Search

Enter any city name and receive:

* Temperature
* Wind Speed
* Weather Condition
* Last Updated Time
* AI Weather Summary

### 📍 Live Location Weather

Uses browser GPS location to:

* Detect current latitude and longitude
* Convert coordinates into a location name
* Fetch weather for the user's exact location

### 🤖 AI Weather Summary

Weather data is sent to a Groq-hosted Llama model which generates:

* Easy-to-understand weather explanation
* Weather feeling
* Practical outdoor suggestions

---

## 🏗️ Project Architecture

User Input / GPS Location
↓
Geocoding / Reverse Geocoding
↓
Weather API
↓
Groq LLM
↓
AI Weather Summary
↓
Streamlit UI

---

## 📂 Project Structure

AI-Weather-Assistant/

├── app.py

├── services/

│ ├── geocoding.py

│ ├── reverse_geocoding.py

│ ├── weather.py

│ └── llm.py

├── utils/

│ └── weather_codes.py

├── requirements.txt

└── README.md

---

## 🛠️ Tech Stack

* Python
* Streamlit
* Open-Meteo API
* OpenStreetMap Reverse Geocoding
* Groq API
* Llama 3.3 70B Versatile

---

## ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/BytewithSai/AI-Weather-Assistant.git
```

Move into the project folder:

```bash
cd AI-Weather-Assistant
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Create a `.env` file:

```env
GROQ_API_KEY=your_groq_api_key
```

Run the application:

```bash
streamlit run app.py
```

---

## 🎯 Learning Outcomes

Through this project I learned:

* API Integration
* Geocoding & Reverse Geocoding
* LLM Integration
* Prompt Engineering
* Streamlit Development
* Session State Management
* Location Services
* Cloud Deployment
* GitHub Project Management

---

## 🔮 Future Improvements

* 5-Day Weather Forecast
* Weather Charts & Visualizations
* Multi-language Support
* Weather Alerts
* Voice Assistant Integration
* Tool Calling Architecture

---

## 👨‍💻 Author

Sai Prakash Reddy

Built while learning AI Engineering and Generative AI through hands-on projects.
