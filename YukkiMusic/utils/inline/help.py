#
# Copyright (C) 2021-2022 by TeamYukki@Github, < https://github.com/TeamYukki >.
#
# This file is part of < https://github.com/TeamYukki/YukkiMusicBot > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/TeamYukki/YukkiMusicBot/blob/master/LICENSE >
#
# All rights reserved.

from typing import Union

from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from YukkiMusic import app


def help_pannel(_, START: Union[bool, int] = None):
    first = [
        InlineKeyboardButton(
            text=_["CLOSEMENU_BUTTON"], callback_data=f"close"
        )
    ]
    second = [
        InlineKeyboardButton(
            text=_["BACK_BUTTON"],
            callback_data=f"settingsback_helper",
        ),
        InlineKeyboardButton(
            text=_["CLOSEMENU_BUTTON"], callback_data=f"close"
        ),
    ]
    mark = second if START else first
    upl = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    text=_["H_B_1"],
                    callback_data="help_callback hb1",
                    await message.reply_photo(
        photo=f"https://telegra.ph/file/f4a1b7af9f582d2cf3004.jpg",
                ),
                InlineKeyboardButton(
                    text=_["H_B_2"],
                    callback_data="help_callback hb2",
                    await message.reply_photo(
        photo=f"https://telegra.ph/file/f4a1b7af9f582d2cf3004.jpg",
                ),
            ],
            [
                InlineKeyboardButton(
                    text=_["H_B_3"],
                    callback_data="help_callback hb3",
                    await message.reply_photo(
        photo=f"https://telegra.ph/file/f4a1b7af9f582d2cf3004.jpg",
                ),
                InlineKeyboardButton(
                    text=_["H_B_4"],
                    callback_data="help_callback hb4",
                    await message.reply_photo(
        photo=f"https://telegra.ph/file/f4a1b7af9f582d2cf3004.jpg",
                ),
            ],
            [
                InlineKeyboardButton(
                    text=_["H_B_6"],
                    callback_data="help_callback hb5",
                    await message.reply_photo(
        photo=f"https://telegra.ph/file/f4a1b7af9f582d2cf3004.jpg",
                        ),
            ],
            [
        InlineKeyboardButton(
                    text=_["H_B_7"],
                    callback_data="help_callback hb1",
                    await message.reply_photo(
        photo=f"https://telegra.ph/file/f4a1b7af9f582d2cf3004.jpg",
                ),
            ],
            mark,
        ]
    )
    return upl


def help_back_markup(_):
    upl = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    text=_["BACK_BUTTON"],
                    callback_data=f"settings_back_helper",
                ),
                InlineKeyboardButton(
                    text=_["CLOSE_BUTTON"], callback_data=f"close"
                ),
            ]
        ]
    )
    return upl


def private_help_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["S_B_1"],
                url=f"https://t.me/{app.username}?start=help",
            ),
        ],
    ]
    return buttons
