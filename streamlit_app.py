import streamlit as st
import pandas as pd
from predictor import predict_game

st.set_page_config(page_title="MLB Prediction Dashboard", layout="centered")

st.title("⚾ MLB Prediction Dashboard")
st.markdown("This app predicts MLB game outcomes using a trained machine learning model.")

# Example static matchups (these would be dynamically pulled in a full version)
games = [
    {"Matchup": "Yankees vs Red Sox", "features": [1.2, -0.8, 3, -2, 0.6]},
    {"Matchup": "Dodgers vs Padres", "features": [0.5, -1.1, 1, 0, 0.3]}
]

data = []
for game in games:
    prediction, confidence = predict_game(game["features"])
    data.append({
        "Matchup": game["Matchup"],
        "Predicted Winner": "Home" if prediction else "Away",
        "Confidence": f"{confidence:.2%}"
    })

df = pd.DataFrame(data)

st.subheader("Today's Predictions")
st.table(df)
