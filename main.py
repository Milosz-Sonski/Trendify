import os
from dotenv import load_dotenv
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from pymongo import MongoClient
from pprint import pprint

# Ładowanie zmiennych środowiskowych
load_dotenv()
client_id = os.getenv("SPOTIPY_CLIENT_ID")
client_secret = os.getenv("SPOTIPY_CLIENT_SECRET")

if not client_id or not client_secret:
    raise Exception("Brakuje danych w .env!")

# Autoryzacja
sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id, client_secret))

# MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["spotify_db"]
collection = db["tracks_basic"]

# Wyszukiwanie utworów
print("🔍 Pobieram popularne utwory z danego roku...")
results = sp.search(q="year:1990", type="track", limit=50)

for item in results["tracks"]["items"]:
    track = item
    track_id = track.get("id")
    if not track_id:
        continue

    try:
        name = track["name"]
        artist = track["artists"][0]["name"]
        artist_id = track["artists"][0]["id"]
        album = track["album"]["name"]
        release_date = track["album"]["release_date"]
        popularity = track["popularity"]
        duration_ms = track["duration_ms"]
        explicit = track["explicit"]

        # Pobranie gatunków
        try:
            artist_info = sp.artist(artist_id)
            genres = artist_info.get("genres", [])
        except:
            genres = []

        doc = {
            "track_id": track_id,
            "name": name,
            "artist": artist,
            "album": album,
            "release_date": release_date,
            "popularity": popularity,
            "duration_ms": duration_ms,
            "explicit": explicit,
            "genres": genres
        }

        collection.update_one({"track_id": track_id}, {"$set": doc}, upsert=True)
        print(f"✅ Zapisano: {name} – {artist}")

    except Exception as e:
        print(f"⚠️ Błąd przy zapisie utworu: {e}")

# Przykład pobranych danych
sample = collection.find_one()
print("🔎 Przykład zapisanego dokumentu:")
pprint(sample)