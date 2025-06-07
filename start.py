from pyrogram import filters
from pyrogram.types import Message
from pyrogram.handlers import MessageHandler

@filters.command("start")
def on_start(client, message: Message):
    message.reply_text("Bot is working!")

start_handler = MessageHandler(on_start, filters.command("start"))
