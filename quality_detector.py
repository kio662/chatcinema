# ─────────────────────────────────────────

# Supported Qualities

# ─────────────────────────────────────────

QUALITIES = [
"4k",
"2160p",
"1080p",
"720p",
"480p",
"360p"
]

# ─────────────────────────────────────────

# Detect Quality

# ─────────────────────────────────────────

def detect_quality(
filename
):

```
if not filename:
    return "unknown"

name = filename.lower()

for quality in QUALITIES:

    if quality in name:
        return quality

return "unknown"
```

# ─────────────────────────────────────────

# Pretty Quality Name

# ─────────────────────────────────────────

def format_quality(
quality
):

```
mapping = {
    "4k": "4K UHD",
    "2160p": "2160p UHD",
    "1080p": "1080p Full HD",
    "720p": "720p HD",
    "480p": "480p SD",
    "360p": "360p Mobile",
    "unknown": "Unknown"
}

return mapping.get(
    quality,
    quality.upper()
)
```

# ─────────────────────────────────────────

# Get All Qualities

# ─────────────────────────────────────────

def get_qualities():

```
return QUALITIES
```
