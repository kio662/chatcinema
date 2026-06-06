from telegram import (
InlineKeyboardMarkup,
InlineKeyboardButton
)

from config import (
UPDATES_CHANNEL,
SUPPORT_GROUP
)

# ─────────────────────────────────────────

# Start Menu

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

# Language Keyboard

# ─────────────────────────────────────────

def language_keyboard(
movie,
languages
):

```
buttons = []

for lang in languages:

    buttons.append([
        InlineKeyboardButton(
            f"🌐 {lang.title()}",
            callback_data=
            f"lang|{movie}|{lang}"
        )
    ])

buttons.append([
    InlineKeyboardButton(
        "🏠 Home",
        callback_data="home"
    )
])

return InlineKeyboardMarkup(
    buttons
)
```

# ─────────────────────────────────────────

# Quality Keyboard

# ─────────────────────────────────────────

def quality_keyboard(
movie,
language,
qualities
):

```
buttons = []

for quality in qualities:

    buttons.append([
        InlineKeyboardButton(
            f"📽 {quality.upper()}",
            callback_data=
            f"quality|{movie}|{language}|{quality}"
        )
    ])

buttons.append([
    InlineKeyboardButton(
        "⬅ Back",
        callback_data="back"
    ),

    InlineKeyboardButton(
        "🏠 Home",
        callback_data="home"
    )
])

return InlineKeyboardMarkup(
    buttons
)
```

# ─────────────────────────────────────────

# Pagination Keyboard

# ─────────────────────────────────────────

def pagination_keyboard(
page,
total_pages
):

```
buttons = []

row = []

if page > 1:

    row.append(
        InlineKeyboardButton(
            "⬅ Prev",
            callback_data=
            f"page|{page-1}"
        )
    )

row.append(
    InlineKeyboardButton(
        f"{page}/{total_pages}",
        callback_data="ignore"
    )
)

if page < total_pages:

    row.append(
        InlineKeyboardButton(
            "Next ➡",
            callback_data=
            f"page|{page+1}"
        )
    )

buttons.append(row)

buttons.append([
    InlineKeyboardButton(
        "🏠 Home",
        callback_data="home"
    )
])

return InlineKeyboardMarkup(
    buttons
)
```

# ─────────────────────────────────────────

# Request Keyboard

# ─────────────────────────────────────────

def request_keyboard(
movie
):

```
return InlineKeyboardMarkup([
    [
        InlineKeyboardButton(
            "📩 Request Movie",
            callback_data=
            f"request|{movie}"
        )
    ]
])
```

# ─────────────────────────────────────────

# Admin Menu

# ─────────────────────────────────────────

def admin_keyboard():

```
return InlineKeyboardMarkup([

    [
        InlineKeyboardButton(
            "📊 Stats",
            callback_data="admin_stats"
        ),

        InlineKeyboardButton(
            "👥 Users",
            callback_data="admin_users"
        )
    ],

    [
        InlineKeyboardButton(
            "📦 Files",
            callback_data="admin_files"
        ),

        InlineKeyboardButton(
            "📩 Requests",
            callback_data="admin_requests"
        )
    ],

    [
        InlineKeyboardButton(
            "🏠 Home",
            callback_data="home"
        )
    ]
])
```
