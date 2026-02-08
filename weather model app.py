import streamlit as st
import joblib
import pandas as pd

model = joblib.load("weather_temperature_model.pkl")

st.title("🌦 Weather Temperature Predictor")

st.write("Enter weather conditions:")

humidity = st.slider("Humidity", 0.0, 1.0, 0.5)
wind_speed = st.number_input("Wind Speed (km/h)", 0.0, 50.0, 10.0)
pressure = st.number_input("Pressure (millibars)", 950.0, 1050.0, 1013.0)
hour = st.slider("Hour of Day", 0, 23, 12)
month = st.slider("Month", 1, 12, 6)

input_df = pd.DataFrame([{
    'Humidity': humidity,
    'Wind Speed (km/h)': wind_speed,
    'Pressure (millibars)': pressure,
    'Hour': hour,
    'Month': month
}])

if st.button("Predict Temperature"):
    prediction = model.predict(input_df)
    st.success(f"🌡 Predicted Temperature: {prediction[0]:.2f} °C")
