import random
from bot.stickers import SAFE_STICKERS

def random_sticker():
    return random.choice(SAFE_STICKERS)
