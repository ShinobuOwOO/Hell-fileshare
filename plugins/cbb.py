#(©)Codexbotz

from pyrogram import __version__
from bot import Bot
from config import OWNER_ID
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

@Bot.on_callback_query()
async def cb_handler(client: Bot, query: CallbackQuery):
    data = query.data
    if data == "about":
        await query.message.edit_text(
            text = f"<b>○ 𝗗𝗲𝘃𝗲𝗹𝗼𝗽𝗲𝗿𝘀 : <a href='tg://user?id={OWNER_ID}'>@Wdevelopers</a>\n○ 𝗟𝗮𝗻𝗴𝘂𝗮𝗴𝗲 : <code>Python3</code>\n○ 𝗟𝗶𝗯𝗿𝗮𝗿𝘆 : <a href='https://docs.pyrogram.org/'>Pyrogram asyncio {__version__}</a>\n○ 𝗖𝗵𝗮𝗻𝗻𝗲𝗹 : @OngoingAnime_Hell\n○ 𝗦𝘂𝗽𝗽𝗼𝗿𝘁 𝗖𝗵𝗮𝘁 : @Wsupportchat</b>",
            disable_web_page_preview = True,
            reply_markup = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("𝗦𝗼𝗷𝗮𝗼 🗿", callback_data = "close")
                    ]
                ]
            )
        )
    elif data == "close":
        await query.message.delete()
        try:
            await query.message.reply_to_message.delete()
        except:
            pass
