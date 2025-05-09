# 🎵 Trendify – Analiza popularności utworów Spotify

Trendify to aplikacja służąca do pobierania, zapisywania i analizowania popularnych utworów muzycznych z Spotify. Wykorzystuje dane API Spotify oraz bazę MongoDB i oferuje interaktywny dashboard w Streamlit.

---

## 🔧 Technologie

- **Python 3.x**
- **Spotify Web API** – przez bibliotekę `spotipy`
- **MongoDB** – lokalna baza danych
- **Streamlit** – dashboard interaktywny
- **Pandas**, **Matplotlib** – analiza i wizualizacja danych

---

## 📁 Struktura projektu

```
Trendify/
├── .env                  # Dane API Spotify
├── main.py               # Pobieranie danych i zapis do MongoDB
├── dashboard.py          # Interaktywny dashboard Streamlit
└── README.md             # Dokumentacja projektu
```

---

## ⚙️ Instalacja

### 1. Klonowanie repozytorium

```
git clone https://github.com/Milosz-Sonski/Trendify.git
cd trendify
```

### 2. Instalacja zależności

```
pip install -r requirements.txt
```

Lub ręcznie:

```
pip install spotipy pymongo python-dotenv streamlit pandas matplotlib
```

### 3. Utwórz plik `.env`

```
SPOTIPY_CLIENT_ID=twoj_client_id
SPOTIPY_CLIENT_SECRET=twoj_client_secret
SPOTIPY_REDIRECT_URI=http://localhost:8888/callback
```

---

## 🚀 Uruchomienie

### 1. Uruchom MongoDB lokalnie

```
mongod
```

### 2. Pobierz dane z Spotify:

```
python main.py
```

### 3. Uruchom dashboard:

```
streamlit run dashboard.py
```

---

## 📊 Funkcje dashboardu

- Filtracja utworów według popularności i gatunku
- Tabela z wynikami
- Wykres najpopularniejszych artystów (średnia popularność)
- Wykres najczęściej występujących gatunków

---

## 🧠 Możliwości rozszerzeń

- Predykcja hitów (ML)
- Analiza tekstów piosenek (NLP)
- Trendy czasowe
- Uwierzytelnianie użytkownika
- Eksport danych do CSV

---

## 🔁 Jak odtworzyć venv na innym komputerze?

python -m venv venv
source venv/bin/activate  # lub .\venv\Scripts\activate na Windows
pip install -r requirements.txt

## 📝 Licencja

Projekt edukacyjny. Możesz używać, modyfikować i rozszerzać.

## ❤️ Miłosz Soński; Wiktor Wardziak; Marcin Zaręba 👲🏿
