from telegram import (
Update,
InlineKeyboardMarkup,
InlineKeyboardButton
)

from telegram.ext import (
ContextTypes
)

from config import (
FORCE_SUB_CHANNEL,
UPDATES_CHANNEL,
SUPPORT_GROUP,
BOT_NAME,
WELCOME_TEXT
)

from database import (
save_user,
is_banned
)

# ─────────────────────────────────────────

# Force Subscribe Check

# ─────────────────────────────────────────

async def check_force_sub(
bot,
user_id
):
try:

```
    member = await bot.get_chat_member(
        FORCE_SUB_CHANNEL,
        user_id
    )

    return member.status in [
        "member",
        "administrator",
        "creator"
    ]

except Exception:
    return False
```

# ─────────────────────────────────────────

# Force Subscribe Keyboard

# ─────────────────────────────────────────

def force_sub_keyboard():

```
return InlineKeyboardMarkup([
    [
        InlineKeyboardButton(
            "📢 Join Channel",
            url=f"https://t.me/{FORCE_SUB_CHANNEL.replace('@','')}"
        )
    ],
    [
        InlineKeyboardButton(
            "🔄 Verify",
            callback_data="verify_sub"
        )
    ]
])
```

# ─────────────────────────────────────────

# Start Keyboard

# ─────────────────────────────────────────

def start_keyboard():

```
return InlineKeyboardMarkup([

    [
        InlineKeyboardButton(
            "📢 Updates",
            url=f"https://t.me/{UPDATES_CHANNEL.replace('@','')}"
        ),

        InlineKeyboardButton(
            "👥 Support",
            url=f"https://t.me/{SUPPORT_GROUP.replace('@','')}"
        )
    ],

    [
        InlineKeyboardButton(
            "🎬 Movies",
            callback_data="movies"
        ),

        InlineKeyboardButton(
            "📺 Anime",
            callback_data="anime"
        )
    ],

    [
        InlineKeyboardButton(
            "ℹ️ About",
            callback_data="about"
        )
    ]
])
```

# ─────────────────────────────────────────

# /start

# ─────────────────────────────────────────

async def start_handler(
update: Update,
context: ContextTypes.DEFAULT_TYPE
):

```
user = update.effective_user

# Save User
save_user(
    user.id,
    user.first_name,
    user.username
)

# Global Ban Check
if is_banned(user.id):

    await update.message.reply_text(
        "🚫 You are banned from using this bot."
    )

    return

# Force Subscribe Check
joined = await check_force_sub(
    context.bot,
    user.id
)

if not joined:

    await update.message.reply_text(
        "🔒 To use this bot, join our channel first.",
        reply_markup=force_sub_keyboard()
    )

    return

# Welcome Poster
poster = (
    "https://i.imgur.com/"
    "5QF4K8m.jpeg"
)

try:

    await update.message.reply_photo(
        photo=poster,
        caption=WELCOME_TEXT,
        reply_markup=start_keyboard()
    )

except Exception:

    await update.message.reply_text(
        WELCOME_TEXT,
        reply_markup=start_keyboard()
    )
```

# ─────────────────────────────────────────

# Verify Subscription Callback

# ─────────────────────────────────────────

async def verify_callback(
update: Update,
context: ContextTypes.DEFAULT_TYPE
):

```
query = update.callback_query

await query.answer()

joined = await check_force_sub(
    context.bot,
    query.from_user.id
)

if joined:

    await query.message.edit_text(
        "✅ Verification Successful!\n\n"
        "Now send a movie or anime name."
    )

else:

    await query.answer(
        "❌ You haven't joined yet.",
        show_alert=True
    )
```
from telegram import Update
from telegram.ext import ContextTypes

from database import (
search_files,
increase_search_count,
is_banned
)

from imdb import get_movie_info

from force_sub import (
check_force_sub,
force_sub_keyboard
)

from keyboards import (
language_keyboard
)

from config import PAGE_SIZE

# ─────────────────────────────────────────

# Smart Search Handler

# ─────────────────────────────────────────

async def search_handler(
update: Update,
context: ContextTypes.DEFAULT_TYPE
):

```
if not update.message:
    return

query = update.message.text.strip()

if len(query) < 3:
    return

user = update.effective_user

# Ban Check
if is_banned(user.id):

    await update.message.reply_text(
        "🚫 You are banned."
    )

    return

# Force Sub Check
joined = await check_force_sub(
    context.bot,
    user.id
)

if not joined:

    await update.message.reply_text(
        "🔒 Join channel first.",
        reply_markup=force_sub_keyboard()
    )

    return

# Statistics
increase_search_count()

# Search Files
results = search_files(query)

if not results:

    await update.message.reply_text(
        f"❌ No results found for:\n\n{query}\n\n"
        "Use request button if needed."
    )

    return

# Available Languages
languages = sorted(
    list(
        set(
            r.get(
                "language",
                "unknown"
            )
            for r in results
        )
    )
)

# IMDb Info
imdb_data = get_movie_info(query)

if imdb_data:

    caption = (
        f"🎬 {imdb_data['title']}\n\n"
        f"⭐ IMDb: {imdb_data['rating']}\n"
        f"📅 Year: {imdb_data['year']}\n"
        f"🎭 Genre: {imdb_data['genre']}\n\n"
        f"📝 {imdb_data['plot'][:300]}"
    )

    try:

        await update.message.reply_photo(
            photo=imdb_data["poster"],
            caption=caption,
            reply_markup=
            language_keyboard(
                query,
                languages
            )
        )

    except Exception:

        await update.message.reply_text(
            caption,
            reply_markup=
            language_keyboard(
                query,
                languages
            )
        )

else:

    await update.message.reply_text(
        f"🎬 Search Results\n\n"
        f"Movie: {query}\n"
        f"Files Found: {len(results)}",
        reply_markup=
        language_keyboard(
            query,
            languages
        )
    )
```

# ─────────────────────────────────────────

# Fuzzy Search Helper

# ─────────────────────────────────────────

def fuzzy_match(
query,
filename
):

```
query = query.lower()
filename = filename.lower()

return query in filename
```
from telegram import Update
from telegram.ext import ContextTypes

from database import (
search_by_filter
)

from keyboards import (
quality_keyboard,
pagination_keyboard,
language_keyboard
)

from config import PAGE_SIZE

# ─────────────────────────────────────────

# Language Callback

# ─────────────────────────────────────────

async def language_callback(
update: Update,
context: ContextTypes.DEFAULT_TYPE
):

```
query = update.callback_query

await query.answer()

_, movie, language = (
    query.data.split("|")
)

results = search_by_filter(
    movie,
    language=language
)

qualities = sorted(
    list(
        set(
            r.get(
                "quality",
                "unknown"
            )
            for r in results
        )
    )
)

await query.message.edit_text(
    f"🎬 {movie}\n\n"
    f"🌐 Language: "
    f"{language.title()}\n\n"
    f"Select Quality",
    reply_markup=
    quality_keyboard(
        movie,
        language,
        qualities
    )
)
```

# ─────────────────────────────────────────

# Quality Callback

# ─────────────────────────────────────────

async def quality_callback(
update: Update,
context: ContextTypes.DEFAULT_TYPE
):

```
query = update.callback_query

await query.answer()

(
    _,
    movie,
    language,
    quality
) = query.data.split("|")

results = search_by_filter(
    movie,
    language,
    quality
)

context.user_data[
    "results"
] = results

context.user_data[
    "movie"
] = movie

await send_page(
    query,
    results,
    page=1
)
```

# ─────────────────────────────────────────

# Pagination Callback

# ─────────────────────────────────────────

async def page_callback(
update: Update,
context: ContextTypes.DEFAULT_TYPE
):

```
query = update.callback_query

await query.answer()

page = int(
    query.data.split("|")[1]
)

results = context.user_data.get(
    "results",
    []
)

await send_page(
    query,
    results,
    page
)
```

# ─────────────────────────────────────────

# Send Page

# ─────────────────────────────────────────

async def send_page(
query,
results,
page
):

```
total_pages = (
    len(results)
    + PAGE_SIZE - 1
) // PAGE_SIZE

start = (
    page - 1
) * PAGE_SIZE

end = start + PAGE_SIZE

files = results[start:end]

text = (
    f"📦 Files\n\n"
    f"Page {page}/{total_pages}\n\n"
)

for idx, item in enumerate(
    files,
    start=1
):

    text += (
        f"{idx}. "
        f"{item['file_name']}\n"
    )

await query.message.edit_text(
    text,
    reply_markup=
    pagination_keyboard(
        page,
        total_pages
    )
)
```

# ─────────────────────────────────────────

# Send File

# ─────────────────────────────────────────

async def send_file(
bot,
chat_id,
file_data,
db_channel
):

```
try:

    await bot.copy_message(
        chat_id=chat_id,
        from_chat_id=db_channel,
        message_id=
        file_data["message_id"]
    )

except Exception:
    pass
```

# ─────────────────────────────────────────

# Home Callback

# ─────────────────────────────────────────

async def home_callback(
update: Update,
context: ContextTypes.DEFAULT_TYPE
):

```
query = update.callback_query

await query.answer()

await query.message.edit_text(
    "🏠 Home Menu"
)
```

# ─────────────────────────────────────────

# Back Callback

# ─────────────────────────────────────────

async def back_callback(
update: Update,
context: ContextTypes.DEFAULT_TYPE
):

```
query = update.callback_query

await query.answer()

movie = context.user_data.get(
    "movie",
    "Unknown"
)

results = context.user_data.get(
    "results",
    []
)

languages = sorted(
    list(
        set(
            r.get(
                "language",
                "unknown"
            )
            for r in results
        )
    )
)

await query.message.edit_text(
    f"🎬 {movie}\n\n"
    f"Select Language",
    reply_markup=
    language_keyboard(
        movie,
        languages
    )
)
```
import time
import asyncio

from telegram import Update
from telegram.ext import ContextTypes

from config import (
AUTO_DELETE_SECONDS,
MAX_SEARCH_PER_MINUTE,
ADMIN_ID
)

from database import (
save_request
)

from force_sub import (
check_force_sub
)

# ─────────────────────────────────────────

# Anti Spam Cache

# ─────────────────────────────────────────

USER_SEARCH_CACHE = {}

# ─────────────────────────────────────────

# Anti Spam Check

# ─────────────────────────────────────────

def anti_spam(user_id):

```
now = time.time()

if user_id not in USER_SEARCH_CACHE:
    USER_SEARCH_CACHE[user_id] = []

USER_SEARCH_CACHE[user_id] = [
    t for t in USER_SEARCH_CACHE[user_id]
    if now - t < 60
]

if len(
    USER_SEARCH_CACHE[user_id]
) >= MAX_SEARCH_PER_MINUTE:

    return False

USER_SEARCH_CACHE[user_id].append(
    now
)

return True
```

# ─────────────────────────────────────────

# Auto Delete

# ─────────────────────────────────────────

async def auto_delete_messages(
bot,
chat_id,
message_ids
):

```
await asyncio.sleep(
    AUTO_DELETE_SECONDS
)

for msg_id in message_ids:

    try:

        await bot.delete_message(
            chat_id,
            msg_id
        )

    except Exception:
        pass
```

# ─────────────────────────────────────────

# Request Movie / Anime

# ─────────────────────────────────────────

async def request_callback(
update: Update,
context: ContextTypes.DEFAULT_TYPE
):

```
query = update.callback_query

await query.answer()

movie = query.data.split("|")[1]

save_request(
    query.from_user.id,
    movie
)

await query.message.reply_text(
    f"✅ Request Saved\n\n"
    f"🎬 {movie}"
)

try:

    await context.bot.send_message(
        chat_id=ADMIN_ID,
        text=(
            "📩 New Request\n\n"
            f"👤 User ID: "
            f"{query.from_user.id}\n\n"
            f"🎬 Movie: {movie}"
        )
    )

except Exception:
    pass
```

# ─────────────────────────────────────────

# Verify Force Subscribe

# ─────────────────────────────────────────

async def verify_callback(
update: Update,
context: ContextTypes.DEFAULT_TYPE
):

```
query = update.callback_query

await query.answer()

joined = await check_force_sub(
    context.bot,
    query.from_user.id
)

if joined:

    await query.message.edit_text(
        "✅ Verification Successful\n\n"
        "Now search your movie or anime."
    )

else:

    await query.answer(
        "❌ Join channel first.",
        show_alert=True
    )
```

# ─────────────────────────────────────────

# Search Protection Wrapper

# ─────────────────────────────────────────

async def protected_search(
update,
context
):

```
user_id = update.effective_user.id

allowed = anti_spam(
    user_id
)

if not allowed:

    await update.message.reply_text(
        "⚠️ Too many searches.\n"
        "Please wait a minute."
    )

    return False

return True
```
