from telegram import (
InlineKeyboardMarkup,
InlineKeyboardButton
)

from config import (
FORCE_SUB_CHANNEL
)

# ─────────────────────────────────────────

# Force Subscribe Keyboard

# ─────────────────────────────────────────

def force_sub_keyboard():

```
return InlineKeyboardMarkup([
    [
        InlineKeyboardButton(
            "📢 Join Channel",
            url=(
                f"https://t.me/"
                f"{FORCE_SUB_CHANNEL.replace('@','')}"
            )
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

# Check Membership

# ─────────────────────────────────────────

async def check_force_sub(
bot,
user_id
):

```
try:

    member = await bot.get_chat_member(
        chat_id=
        FORCE_SUB_CHANNEL,
        user_id=user_id
    )

    if member.status in [
        "member",
        "administrator",
        "creator"
    ]:
        return True

    return False

except Exception:
    return False
```

# ─────────────────────────────────────────

# Verify User

# ─────────────────────────────────────────

async def verify_user(
bot,
user_id
):

```
try:

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

# Verify Callback Message

# ─────────────────────────────────────────

def verify_success_text():

```
return (
    "✅ Verification Successful\n\n"
    "Now send a movie or anime name."
)
```

def verify_failed_text():

```
return (
    "❌ You haven't joined the "
    "channel yet.\n\n"
    "Join first and press Verify."
)
```

# ─────────────────────────────────────────

# Force Sub Warning

# ─────────────────────────────────────────

def force_sub_warning():

```
return (
    "🔒 To use this bot,\n"
    "you must join our channel."
)
```

# ─────────────────────────────────────────

# Error Message

# ─────────────────────────────────────────

def force_sub_error():

```
return (
    "⚠️ Unable to verify membership.\n"
    "Please try again later."
)
```
