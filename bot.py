import asyncio

try:
asyncio.get_event_loop()
except RuntimeError:
asyncio.set_event_loop(
asyncio.new_event_loop()
)

from telegram.ext import (
Application
)

from config import BOT_TOKEN

def main():

```
app = (
    Application.builder()
    .token(BOT_TOKEN)
    .build()
)

print(
    "🎬 CinemaCityHub Started"
)

app.run_polling(
    drop_pending_updates=True
)
```

if **name** == "**main**":
main()
