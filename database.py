from pymongo import MongoClient, TEXT
from config import MONGO_URI, DATABASE_NAME

client = MongoClient(MONGO_URI)

db = client[DATABASE_NAME]

files_col = db["files"]
users_col = db["users"]
requests_col = db["requests"]
banned_col = db["banned_users"]
stats_col = db["stats"]

# ─────────────────────────────────────────

# Indexes

# ─────────────────────────────────────────

files_col.create_index([
("file_name", TEXT)
])

users_col.create_index(
"user_id",
unique=True
)

banned_col.create_index(
"user_id",
unique=True
)

# ─────────────────────────────────────────

# User Functions

# ─────────────────────────────────────────

def save_user(
user_id,
first_name,
username=None
):
users_col.update_one(
{"user_id": user_id},
{
"$set": {
"user_id": user_id,
"first_name": first_name,
"username": username
}
},
upsert=True
)

def get_user(user_id):
return users_col.find_one(
{"user_id": user_id}
)

def get_all_users():
return [
user["user_id"]
for user in users_col.find(
{},
{"user_id": 1}
)
]

def total_users():
return users_col.count_documents({})

# ─────────────────────────────────────────

# File Functions

# ─────────────────────────────────────────

def save_file(data):

```
exists = files_col.find_one(
    {
        "file_unique_id":
        data["file_unique_id"]
    }
)

if exists:
    return False

files_col.insert_one(data)

return True
```

def search_files(query):

```
return list(
    files_col.find(
        {
            "$text": {
                "$search": query
            }
        }
    ).limit(50)
)
```

def search_by_filter(
movie,
language=None,
quality=None
):

```
query = {
    "file_name": {
        "$regex": movie,
        "$options": "i"
    }
}

if language:
    query["language"] = language

if quality:
    query["quality"] = quality

return list(
    files_col.find(query)
)
```

def total_files():
return files_col.count_documents({})

def delete_all_files():
files_col.delete_many({})

# ─────────────────────────────────────────

# Request System

# ─────────────────────────────────────────

def save_request(
user_id,
movie_name
):

```
requests_col.insert_one(
    {
        "user_id": user_id,
        "movie_name": movie_name
    }
)
```

def get_requests():

```
return list(
    requests_col.find({})
)
```

# ─────────────────────────────────────────

# Ban System

# ─────────────────────────────────────────

def ban_user(user_id):

```
banned_col.update_one(
    {"user_id": user_id},
    {"$set": {"user_id": user_id}},
    upsert=True
)
```

def unban_user(user_id):

```
banned_col.delete_one(
    {"user_id": user_id}
)
```

def is_banned(user_id):

```
return banned_col.find_one(
    {"user_id": user_id}
) is not None
```

# ─────────────────────────────────────────

# Statistics

# ─────────────────────────────────────────

def increase_search_count():

```
stats_col.update_one(
    {"_id": "searches"},
    {"$inc": {"count": 1}},
    upsert=True
)
```

def total_searches():

```
data = stats_col.find_one(
    {"_id": "searches"}
)

if not data:
    return 0

return data["count"]
```
