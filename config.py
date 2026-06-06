import os
from dotenv import load_dotenv

load_dotenv()

# ─────────────────────────────────────────

# Telegram

# ─────────────────────────────────────────

BOT_TOKEN = os.getenv(
"BOT_TOKEN",
""
)

BOT_USERNAME = os.getenv(
"BOT_USERNAME",
"Tamil_Anime_TNMC_Bot"
)

# ─────────────────────────────────────────

# MongoDB

# ─────────────────────────────────────────

MONGO_URI = os.getenv(
"MONGO_URI",
""
)

DATABASE_NAME = os.getenv(
"DATABASE_NAME",
"cinemacityhub"
)

# ─────────────────────────────────────────

# Channels

# ─────────────────────────────────────────

DB_CHANNEL = int(
os.getenv(
"DB_CHANNEL",
"-1004294321324"
)
)

FORCE_SUB_CHANNEL = os.getenv(
"FORCE_SUB_CHANNEL",
"@Cinemacityhub_info"
)

UPDATES_CHANNEL = os.getenv(
"UPDATES_CHANNEL",
"@CinemaCityHub"
)

SUPPORT_GROUP = os.getenv(
"SUPPORT_GROUP",
"@Rising_With_The_Wind_Tamil"
)

# ─────────────────────────────────────────

# Admin

# ─────────────────────────────────────────

ADMIN_ID = int(
os.getenv(
"ADMIN_ID",
"6558711318"
)
)

# ─────────────────────────────────────────

# OMDb API

# ─────────────────────────────────────────

OMDB_API_KEY = os.getenv(
"OMDB_API_KEY",
"73e3e048"
)

# ─────────────────────────────────────────

# Auto Delete

# ─────────────────────────────────────────

AUTO_DELETE_SECONDS = int(
os.getenv(
"AUTO_DELETE_SECONDS",
"600"
)
)

# ─────────────────────────────────────────

# Pagination

# ─────────────────────────────────────────

PAGE_SIZE = int(
os.getenv(
"PAGE_SIZE",
"10"
)
)

# ─────────────────────────────────────────

# Anti Spam

# ─────────────────────────────────────────

MAX_SEARCH_PER_MINUTE = int(
os.getenv(
"MAX_SEARCH_PER_MINUTE",
"20"
)
)

# ─────────────────────────────────────────

# Bot Info

# ─────────────────────────────────────────

BOT_NAME = "CinemaCityHub"

BOT_VERSION = "3.0 Production"

WELCOME_TEXT = f'''
🎬 Welcome to {BOT_NAME}

🍿 Movie + Anime Filter Bot

✅ Smart Search
✅ IMDb Posters
✅ Multi Language
✅ Quality Filter
✅ Auto Delete
✅ Force Subscribe

Type any movie or anime name
to start searching.
'''
