import streamlit as st
import requests

# Fonction pour récupérer une activité aléatoire de l'API
def get_random_activity():
    url = "https://bored-api.appbrewery.com/random"
    response = requests.get(url)
    activity_data = response.json()
    return activity_data["activity"]

# Interface Streamlit
st.title("Bored API Activity Generator")

if st.button("Get an activity"):
    activity = get_random_activity()
    st.success(f"Suggested activity: {activity}")
else:
    st.write("Click the button to get a random activity suggestion.")
