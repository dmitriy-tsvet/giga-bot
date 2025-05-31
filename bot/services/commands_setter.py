from aiogram import Bot
from aiogram.types import BotCommand, BotCommandScopeChat
from bot import config


async def set_bot_commands(bot: Bot):
    await bot.set_my_commands(
        [
            BotCommand(command="start", description="Start"),
        ]
    )
