import requests

from config import (
OMDB_API_KEY
)

# ─────────────────────────────────────────

# OMDb API Request

# ─────────────────────────────────────────

def get_movie_info(
movie_name
):

```
try:

    url = (
        "https://www.omdbapi.com/"
        f"?apikey={OMDB_API_KEY}"
        f"&t={movie_name}"
    )

    response = requests.get(
        url,
        timeout=10
    )

    data = response.json()

    if data.get(
        "Response"
    ) == "False":

        return None

    return {
        "title":
            data.get("Title"),

        "year":
            data.get("Year"),

        "rating":
            data.get("imdbRating"),

        "genre":
            data.get("Genre"),

        "plot":
            data.get("Plot"),

        "poster":
            data.get("Poster"),

        "runtime":
            data.get("Runtime"),

        "language":
            data.get("Language"),

        "country":
            data.get("Country"),

        "director":
            data.get("Director"),

        "actors":
            data.get("Actors")
    }

except Exception:

    return None
```

# ─────────────────────────────────────────

# Build IMDb Caption

# ─────────────────────────────────────────

def build_imdb_caption(
imdb_data
):

```
if not imdb_data:

    return (
        "❌ IMDb information "
        "not available."
    )

caption = f"""
```

🎬 {imdb_data['title']}

⭐ IMDb : {imdb_data['rating']}
📅 Year : {imdb_data['year']}
🎭 Genre : {imdb_data['genre']}

🎬 Runtime :
{imdb_data['runtime']}

🌐 Language :
{imdb_data['language']}

🌍 Country :
{imdb_data['country']}

🎬 Director :
{imdb_data['director']}

👥 Cast :
{imdb_data['actors']}

📝 Plot :

{imdb_data['plot']}
"""

```
return caption
```

# ─────────────────────────────────────────

# Search By IMDb ID

# ─────────────────────────────────────────

def get_by_imdb_id(
imdb_id
):

```
try:

    url = (
        "https://www.omdbapi.com/"
        f"?apikey={OMDB_API_KEY}"
        f"&i={imdb_id}"
    )

    response = requests.get(
        url,
        timeout=10
    )

    data = response.json()

    if data.get(
        "Response"
    ) == "False":

        return None

    return data

except Exception:

    return None
```

# ─────────────────────────────────────────

# Search By Year

# ─────────────────────────────────────────

def get_movie_year(
movie_name,
year
):

```
try:

    url = (
        "https://www.omdbapi.com/"
        f"?apikey={OMDB_API_KEY}"
        f"&t={movie_name}"
        f"&y={year}"
    )

    response = requests.get(
        url,
        timeout=10
    )

    data = response.json()

    if data.get(
        "Response"
    ) == "False":

        return None

    return data

except Exception:

    return None
```

# ─────────────────────────────────────────

# Poster Validation

# ─────────────────────────────────────────

def get_poster_url(
imdb_data
):

```
if not imdb_data:
    return None

poster = imdb_data.get(
    "poster"
)

if not poster:
    return None

if poster == "N/A":
    return None

return poster
```
