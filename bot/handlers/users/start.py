from aiogram import types, Dispatcher, F
from aiogram.filters import CommandStart, CommandObject

import tools.filer
from bot import keyboards, config, filters
from aiogram.utils.keyboard import InlineKeyboardBuilder, InlineKeyboardButton
from sqlalchemy import select
from bot import models
from datetime import datetime
import pytz


from gigachat import GigaChat


async def start_handler(message: types.Message):
    with GigaChat(credentials=config.TOKEN, model="GigaChat-2", verify_ssl_certs=False) as giga:
        response = giga.chat("Привет!")
        await message.bot.send_chat_action(
            chat_id=message.chat.id,
            action="typing"
        )
        await message.answer(text=response.choices[0].message.content)
    # print(response.choices[0].message.content)


async def text_handler(message: types.Message):
    with GigaChat(credentials=config.TOKEN, model="GigaChat-2", verify_ssl_certs=False) as giga:
        response = giga.chat(message.text)
        await message.bot.send_chat_action(
            chat_id=message.chat.id,
            action="typing"
        )
        await message.answer(text=response.choices[0].message.content, parse_mode="Markdown")


def setup(dp: Dispatcher):
    dp.message.register(
        start_handler,
        CommandStart()
    )

    dp.message.register(
        text_handler,
        F.text.regexp(r"^Додик")
    )

    dp.message.register(
        text_handler,
        filters.IsReplyMeFilter()
    )
