from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
import os
import sys
from threading import Thread
from pyrogram import idle, filters
from pyrogram.handlers import MessageHandler
from helpers.wrappers import errors, admins_only


@Client.on_message(
    filters.command("start")
    & filters.private
    & ~ filters.edited
)
async def start_(client: Client, message: Message):
    await message.reply_text(
       f"""🤓 Hi {message.from_user.first_name}!

🤓 I am քʀɨռƈɛֆֆ ʍǟʀƈɛʟʟǟ. 🤓

😈 @me_harry 😈

😜 I can play music in your Telegram Group's Voice Chat😜

😶 WANNA KNOW ABOUT ME. 😶""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "Code", url="https://github.com/princessmarcella/princess"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "Our Group", url="https://t.me/loveshoveishqzaade"
                    ),
                    InlineKeyboardButton(
                        "Owner", url="https://t.me/me_harry"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "END", callback_data="close"
                    )
                ]
            ]
        )
    )


@Client.on_message(
    filters.command("start")
    & filters.group
    & ~ filters.edited
)
async def start(client: Client, message: Message):
    await message.reply_text(
        "**քʀɨռƈɛֆֆ:** I'm Working!!!\nUse me in Inline to search for a YouTube Video/Music. \n**Happy Streaming**",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🎶 Search 🎶", switch_inline_query_current_chat=""
                    ),
                    InlineKeyboardButton(
                        "❌ Close ❌", callback_data="close"
                    )
                ]
            ]
        )
    )
