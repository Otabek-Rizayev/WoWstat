from aiogram import Router, types
from aiogram import types
import aiohttp
import asyncio
from bs4 import BeautifulSoup
from aiogram.filters import Command
router = Router()

@router.message(Command("warmane"))
async def cmd_warmane(msg: types.Message):
    async with aiohttp.ClientSession() as session:
        async with session.get('https://www.warmane.com/') as response:
            text = await response.text(encoding="utf-8")
            soup = BeautifulSoup(text, "html.parser")
            l = soup.find_all("span")[0].get_text()
            i = soup.find_all("span")[1].get_text()
            b = soup.find_all("span")[2].get_text()
            f = soup.find_all("span")[3].get_text()
            t = soup.find_all("span")[4].get_text()
            await msg.reply(f"♻ Warmane online:\n• Lordaeron {l}\n• Icecrown {i}\n• Blackrock {b}\n• Frostwolf {f}\nJami online: {t}")


@router.message(Command("circle"))
async def cmd_circle(msg: types.Message):
    await msg.reply(f"Tez orada")

@router.message(Command("sirus"))
async def cmd_circle(msg: types.Message):
    await msg.reply("Tez orada")
