from aiogram import Router, types
from aiogram.filters.command import Command

router = Router()


@router.message(Command('help'))
async def bot_help(message: types.Message):
    text = ("Buyruqlar: ",
            "/online - Battle-arena.uz serveri barcha realmidagi onlaynni ko'rsatadi."
            "/warmane - Warmane.com serveri barcha realmidagi onlaynni ko'rsatadi.",
            "/circle - WoWCircle.com serveri barcha realmidagi onlaynni ko'rsatadi.",
            "/sirus - Sirus.one serveri barcha realmidagi onlaynni ko'rsatadi."
            "/item - WoW 3.3.5 versiyasidagi xohlagan buyumlarni qidirib topish.")
    await message.answer(text="\n".join(text))
