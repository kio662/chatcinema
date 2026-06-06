# ─────────────────────────────────────────

# Supported Languages

# ─────────────────────────────────────────

LANGUAGES = [
"tamil",
"hindi",
"english",
"telugu",
"malayalam",
"kannada",
"dual",
"multi"
]

# ─────────────────────────────────────────

# Detect Language

# ─────────────────────────────────────────

def detect_language(
filename
):

```
if not filename:
    return "unknown"

name = filename.lower()

for language in LANGUAGES:

    if language in name:
        return language

return "unknown"
```

# ─────────────────────────────────────────

# Pretty Language Name

# ─────────────────────────────────────────

def format_language(
language
):

```
mapping = {
    "tamil": "Tamil",
    "hindi": "Hindi",
    "english": "English",
    "telugu": "Telugu",
    "malayalam": "Malayalam",
    "kannada": "Kannada",
    "dual": "Dual Audio",
    "multi": "Multi Audio",
    "unknown": "Unknown"
}

return mapping.get(
    language,
    language.title()
)
```

# ─────────────────────────────────────────

# Get All Languages

# ─────────────────────────────────────────

def get_languages():

```
return LANGUAGES
```
