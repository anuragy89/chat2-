EMOJIS = ["😂", "🤣", "🔥", "👍", "❤️"]

def has_emoji(text: str) -> bool:
    return any(e in text for e in EMOJIS)

def is_hindi(text: str) -> bool:
    return any('\u0900' <= c <= '\u097F' for c in text)
