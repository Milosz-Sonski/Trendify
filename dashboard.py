import streamlit as st
import pandas as pd
from pymongo import MongoClient
import matplotlib.pyplot as plt

st.set_page_config(page_title="Spotify Dashboard", layout="wide")
st.title("📊 Trendify – Analiza popularności utworów Spotify ")

# MongoDB
try:
    client = MongoClient("mongodb://localhost:27017/")
    db = client["spotify_db"]
    collection = db["tracks_basic"]
    data = pd.DataFrame(list(collection.find()))
except Exception as e:
    st.error(f"Błąd połączenia z MongoDB: {e}")
    st.stop()

# Sprawdzenie danych
if data.empty:
    st.warning("Brak danych w bazie. Uruchom main.py, aby pobrać dane.")
    st.stop()

# Usuwanie ID MongoDB
if "_id" in data.columns:
    data.drop(columns=["_id"], inplace=True)

# Filtry
st.sidebar.header("🎚️ Filtry")
min_popularity = st.sidebar.slider("Minimalna popularność", 0, 100, 50)

all_genres = sorted(set(g for genre_list in data["genres"] for g in genre_list))
selected_genres = st.sidebar.multiselect("Wybierz gatunki", options=all_genres)

# Filtrowanie danych
filtered_data = data[data["popularity"] >= min_popularity]
if selected_genres:
    filtered_data = filtered_data[filtered_data["genres"].apply(lambda g: any(x in g for x in selected_genres))]

# Wyświetlanie danych
st.subheader("📄 Lista utworów")
st.dataframe(filtered_data[["name", "artist", "popularity", "genres", "release_date"]])

# Topowi artyści
st.subheader("🎤 Top 10 najpopularniejszych artystów")

top_artists = (
    filtered_data.groupby("artist")["popularity"]
    .mean()
    .sort_values(ascending=False)
    .head(10)
)

st.bar_chart(top_artists)

# Topowe gatunki
st.subheader("🎶 Najczęściej występujące gatunki")

genre_counts = pd.Series([genre for genres in filtered_data["genres"] for genre in genres])
top_genres = genre_counts.value_counts().head(10)

fig, ax = plt.subplots()
top_genres.plot(kind="bar", ax=ax)
ax.set_ylabel("Liczba utworów")
ax.set_xlabel("Gatunek")
ax.set_title("Top 10 gatunków muzycznych")
st.pyplot(fig)