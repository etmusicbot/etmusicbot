import asyncio
from pyrogram import Client, filters
from strings import get_command
from strings.filters import command
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from YukkiMusic import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)


@app.on_message(
     command(["مبرمج السورس","ايطالي","المبرمج"])
    & ~filters.edited
)
async def khalid(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/f4a1b7af9f582d2cf3004.jpg",
caption=f"""✧ الزرار الاول -> قناه السورس \n✧ الزرار الثاني -> هو مبرمج السورس""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                InlineKeyboardButton(
                    "𓆩𝚂𝙾𝚄𝚁𝙲𝙴 𝙴𝚃𝙰𝙻𝙴𝙴𓆪", url=f"https://t.me/ET_WO"
                ),
                ],
                [
                    InlineKeyboardButton(
                        "الإيـ ـطـ ـالـ ـي حـِْـٰــ۫͜ ــزًيــ۫͜ ـن 𓆩🖤🥀𓆪", url=f"https://t.me/ETALEE0"),
                ],
            ]
        ),
    )
