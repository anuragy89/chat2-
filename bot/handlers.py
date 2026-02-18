from aiogram import types
from bot.filters import has_emoji, is_hindi
from bot.utils import random_sticker
from bot.memory import save_message
from bot.database import users, groups

async def handle_message(message: types.Message):
    if message.chat.type in ["group", "supergroup"]:
        groups.update_one({"_id": message.chat.id}, {"$set": {}}, upsert=True)

    users.update_one({"_id": message.from_user.id}, {"$set": {}}, upsert=True)

    # react ONLY if reply
    if not message.reply_to_message or not message.text:
        return

    save_message(message.chat.id, message.from_user.id, message.text)

    if has_emoji(message.text):
        await message.reply_sticker(random_sticker())
    else:
        reply = "हाँ 😄" if is_hindi(message.text) else "Yeah 😄"
        await message.reply(reply)
