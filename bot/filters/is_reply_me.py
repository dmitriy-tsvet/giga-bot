from dataclasses import dataclass

from aiogram import types
from aiogram.filters.base import Filter


class IsReplyMeFilter(Filter):
    def __init__(self, is_reply: bool = True):
        self.is_reply = is_reply

    async def __call__(self, message: types.Message) -> bool:
        if not self.is_reply:
            return True
        if not message.reply_to_message:
            return False
        return message.reply_to_message.from_user and message.reply_to_message.from_user.id == message.bot.id
