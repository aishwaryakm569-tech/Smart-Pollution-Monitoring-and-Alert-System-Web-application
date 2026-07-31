import streamlit as st
import random

st.set_page_config(page_title="Smart Pollution Monitoring", layout="centered")

st.title(" Smart Pollution Monitoring & Alert System")


st.header(" Enter Location Details")
area = st.text_input("Enter Area in Bengaluru:")


if st.button("Check Pollution Levels"):

    if area:
        aqi = random.randint(50, 300)
        water_quality = random.choice(["Good", "Moderate", "Poor"])

        st.subheader(f" Pollution Data for {area}")
        st.write(f"Air Quality Index (AQI): {aqi}")
        st.write(f"Water Quality: {water_quality}")

        
        st.header(" AI Analysis")

        if aqi > 200:
            st.error(" High Pollution Hotspot Detected!")
            alert = "High AQI - Immediate Action Required"
        elif aqi > 100:
            st.warning(" Moderate Pollution Level")
            alert = "Moderate AQI - Monitor Closely"
        else:
            st.success("Air Quality is Good")
            alert = "Safe"

        
        st.header(" Alert System")
        st.write(f"Alert Sent to BBMP: {alert}")

        
        st.header(" Dashboard")
        st.info("Live Pollution Map (Simulated)")
        st.write("Area:", area)
        st.write("AQI:", aqi)

        
        st.header(" Suggested Action")

        if aqi > 200:
            st.write(" Deploy emergency pollution control measures")
        elif aqi > 100:
            st.write(" Monitor area and reduce traffic")
        else:
            st.write(" No immediate action required")

    else:
        st.warning("Please enter an area name")
