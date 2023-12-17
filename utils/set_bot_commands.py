from aiogram import Bot
from aiogram.methods.set_my_commands import BotCommand
from aiogram.types import BotCommandScopeAllPrivateChats


async def set_default_commands(bot: Bot):
    commands = [
        BotCommand(command="/item", description="WoW 3.3.5 versiyasidagi barcha buyumlarni qidirish"),
        BotCommand(command="/online", description="WoW.GAME barcha onlayn o'yinchilarni ko'rsatish"),
        BotCommand(command="/ba", description="Battle-Arena.uz barcha onlayn o'yinchilarni ko'rsatish"),
        BotCommand(command="/warmane", description="Barcha onlayn o'yinchilarni ko'rsatish"),
        BotCommand(command="/circle", description="Barcha onlayn o'yinchilarni ko'rsatish"),
        BotCommand(command="/sirus", description="Barcha onlayn o'yinchilarni ko'rsatish"),

    ]
    await bot.set_my_commands(commands=commands, scope=BotCommandScopeAllPrivateChats())
