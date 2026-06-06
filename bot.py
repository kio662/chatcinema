from telegram.ext import (
Application,
CommandHandler,
MessageHandler,
CallbackQueryHandler,
filters
)

from config import BOT_TOKEN

from handlers import (
start_handler,
search_handler,
index_handler,
request_callback
)

from admin import (
stats_handler,
broadcast_handler,
ban_handler,
unban_handler,
deleteall_handler,
requests_handler
)

def main():

```
app = (
    Application.builder()
    .token(BOT_TOKEN)
    .build()
)

# ─────────────────────────────
# Commands
# ─────────────────────────────

app.add_handler(
    CommandHandler(
        "start",
        start_handler
    )
)

app.add_handler(
    CommandHandler(
        "stats",
        stats_handler
    )
)

app.add_handler(
    CommandHandler(
        "broadcast",
        broadcast_handler
    )
)

app.add_handler(
    CommandHandler(
        "ban",
        ban_handler
    )
)

app.add_handler(
    CommandHandler(
        "unban",
        unban_handler
    )
)

app.add_handler(
    CommandHandler(
        "deleteall",
        deleteall_handler
    )
)

app.add_handler(
    CommandHandler(
        "requests",
        requests_handler
    )
)

# ─────────────────────────────
# Callback Queries
# ─────────────────────────────

app.add_handler(
    CallbackQueryHandler(
        request_callback,
        pattern="^request"
    )
)

# ─────────────────────────────
# Movie / Anime Search
# ─────────────────────────────

app.add_handler(
    MessageHandler(
        filters.TEXT &
        ~filters.COMMAND,
        search_handler
    )
)

# ─────────────────────────────
# DB Channel File Indexing
# ─────────────────────────────

app.add_handler(
    MessageHandler(
        filters.ALL,
        index_handler
    )
)

print(
    "━━━━━━━━━━━━━━━━━━━━━━"
)
print(
    "🎬 CinemaCityHub Started"
)
print(
    "━━━━━━━━━━━━━━━━━━━━━━"
)

app.run_polling(
    drop_pending_updates=True
)
```

if **name** == "**main**":
main()
