from telegram import Update
from telegram.ext import ContextTypes

from config import ADMIN_ID

from database import (
total_users,
total_files,
total_searches,
get_all_users,
get_requests,
ban_user,
unban_user,
delete_all_files
)

# ─────────────────────────────────────────

# Admin Check

# ─────────────────────────────────────────

def is_admin(user_id):
return user_id == ADMIN_ID

# ─────────────────────────────────────────

# /stats

# ─────────────────────────────────────────

async def stats_handler(
update: Update,
context: ContextTypes.DEFAULT_TYPE
):

```
if not is_admin(
    update.effective_user.id
):
    return

text = (
    "📊 CinemaCityHub Stats\n\n"
    f"👥 Users: {total_users()}\n"
    f"📦 Files: {total_files()}\n"
    f"🔍 Searches: {total_searches()}"
)

await update.message.reply_text(
    text
)
```

# ─────────────────────────────────────────

# /users

# ─────────────────────────────────────────

async def users_handler(
update: Update,
context: ContextTypes.DEFAULT_TYPE
):

```
if not is_admin(
    update.effective_user.id
):
    return

await update.message.reply_text(
    f"👥 Total Users: "
    f"{total_users()}"
)
```

# ─────────────────────────────────────────

# /files

# ─────────────────────────────────────────

async def files_handler(
update: Update,
context: ContextTypes.DEFAULT_TYPE
):

```
if not is_admin(
    update.effective_user.id
):
    return

await update.message.reply_text(
    f"📦 Total Files: "
    f"{total_files()}"
)
```

# ─────────────────────────────────────────

# /broadcast

# ─────────────────────────────────────────

async def broadcast_handler(
update: Update,
context: ContextTypes.DEFAULT_TYPE
):

```
if not is_admin(
    update.effective_user.id
):
    return

text = update.message.text.replace(
    "/broadcast",
    ""
).strip()

if not text:

    await update.message.reply_text(
        "Usage:\n"
        "/broadcast Hello"
    )

    return

success = 0
failed = 0

users = get_all_users()

for user_id in users:

    try:

        await context.bot.send_message(
            chat_id=user_id,
            text=text
        )

        success += 1

    except Exception:

        failed += 1

await update.message.reply_text(
    f"✅ Success: {success}\n"
    f"❌ Failed: {failed}"
)
```

# ─────────────────────────────────────────

# /ban

# ─────────────────────────────────────────

async def ban_handler(
update: Update,
context: ContextTypes.DEFAULT_TYPE
):

```
if not is_admin(
    update.effective_user.id
):
    return

if not context.args:
    return

user_id = int(
    context.args[0]
)

ban_user(user_id)

await update.message.reply_text(
    f"🚫 User Banned\n\n"
    f"{user_id}"
)
```

# ─────────────────────────────────────────

# /unban

# ─────────────────────────────────────────

async def unban_handler(
update: Update,
context: ContextTypes.DEFAULT_TYPE
):

```
if not is_admin(
    update.effective_user.id
):
    return

if not context.args:
    return

user_id = int(
    context.args[0]
)

unban_user(user_id)

await update.message.reply_text(
    f"✅ User Unbanned\n\n"
    f"{user_id}"
)
```

# ─────────────────────────────────────────

# /deleteall

# ─────────────────────────────────────────

async def deleteall_handler(
update: Update,
context: ContextTypes.DEFAULT_TYPE
):

```
if not is_admin(
    update.effective_user.id
):
    return

delete_all_files()

await update.message.reply_text(
    "🗑 All Indexed Files Deleted"
)
```

# ─────────────────────────────────────────

# /requests

# ─────────────────────────────────────────

async def requests_handler(
update: Update,
context: ContextTypes.DEFAULT_TYPE
):

```
if not is_admin(
    update.effective_user.id
):
    return

requests = get_requests()

if not requests:

    await update.message.reply_text(
        "📭 No Requests"
    )

    return

text = "📩 Requests\n\n"

for req in requests[:50]:

    text += (
        f"🎬 "
        f"{req['movie_name']}\n"
    )

await update.message.reply_text(
    text
)
```

# ─────────────────────────────────────────

# /restart

# ─────────────────────────────────────────

async def restart_handler(
update: Update,
context: ContextTypes.DEFAULT_TYPE
):

```
if not is_admin(
    update.effective_user.id
):
    return

await update.message.reply_text(
    "♻️ Restart Requested\n"
    "Restart Render Service."
)
```
