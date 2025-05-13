import streamlit as st
import pandas as pd

st.set_page_config(page_title="MLB Prediction Dashboard", layout="centered")

st.title("MLB Prediction Dashboard")
st.markdown("This app displays today's matchups and predicted winners.")

# Example data (mocked for now)
data = {
    "Matchup": ["Yankees vs Red Sox", "Dodgers vs Padres"],
    "Predicted Winner": ["Yankees", "Dodgers"],
    "Confidence": ["71.2%", "68.5%"]
}
df = pd.DataFrame(data)
st.table(df)
