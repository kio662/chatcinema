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
request_callback,
verify_callback,
language_callback,
quality_callback,
page_callback,
back_callback,
home_callback
)

from admin import (
stats_handler,
broadcast_handler,
ban_handler,
unban_handler,
deleteall_handler,
requests_handler,
users_handler,
files_handler,
restart_handler
)

def main():

```
app = (
    Application.builder()
    .token(BOT_TOKEN)
    .build()
)

# Commands
app.add_handler(
    CommandHandler("start", start_handler)
)

app.add_handler(
    CommandHandler("stats", stats_handler)
)

app.add_handler(
    CommandHandler("broadcast", broadcast_handler)
)

app.add_handler(
    CommandHandler("ban", ban_handler)
)

app.add_handler(
    CommandHandler("unban", unban_handler)
)

app.add_handler(
    CommandHandler("deleteall", deleteall_handler)
)

app.add_handler(
    CommandHandler("requests", requests_handler)
)

app.add_handler(
    CommandHandler("users", users_handler)
)

app.add_handler(
    CommandHandler("files", files_handler)
)

app.add_handler(
    CommandHandler("restart", restart_handler)
)

# Callback Queries
app.add_handler(
    CallbackQueryHandler(
        verify_callback,
        pattern="^verify_sub$"
    )
)

app.add_handler(
    CallbackQueryHandler(
        request_callback,
        pattern="^request"
    )
)

app.add_handler(
    CallbackQueryHandler(
        language_callback,
        pattern="^lang"
    )
)

app.add_handler(
    CallbackQueryHandler(
        quality_callback,
        pattern="^quality"
    )
)

app.add_handler(
    CallbackQueryHandler(
        page_callback,
        pattern="^page"
    )
)

app.add_handler(
    CallbackQueryHandler(
        back_callback,
        pattern="^back"
    )
)

app.add_handler(
    CallbackQueryHandler(
        home_callback,
        pattern="^home"
    )
)

# Search Messages
app.add_handler(
    MessageHandler(
        filters.TEXT & ~filters.COMMAND,
        search_handler
    )
)

# DB Channel Indexing
app.add_handler(
    MessageHandler(
        filters.ALL,
        index_handler
    )
)

print("━━━━━━━━━━━━━━━━━━━━━━")
print("🎬 CinemaCityHub Started")
print("━━━━━━━━━━━━━━━━━━━━━━")

app.run_polling(
    drop_pending_updates=True
)
```

if **name** == "**main**":
main()
