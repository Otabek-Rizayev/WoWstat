from aiogram import Router, types
from aiogram import types
import aiohttp
import asyncio
from scrape import off_func
from bs4 import BeautifulSoup
from aiogram.filters import Command
router = Router()

@router.message(Command("online"))
async def cmd_wowgame(msg: types.Message):
    async with aiohttp.ClientSession() as session:
        async with session.get('https://account.wow.game/ucp') as response:
            text = await response.text(encoding="utf-8")
            soup = BeautifulSoup(text, "html.parser")
            o = soup.find("div", {"class":"bg-[#121313] relative px-[9px] py-[5px] md:px-[26px] md:py-2 ml-auto text-xs md:text-2xl font-medium w-fit md:tracking-[3.84px] tracking-[1.92px] rounded-[7px] gap-[6px] flex items-center gradientBorderOnline"}).get_text()
            await msg.reply(f"♻ WoW.GAME online: {o.strip()}")

@router.message(Command("official"))
async def cmd_off(msg: types.Message):
    ranking = await off_func()
    await message.reply(ranking)

@router.message(Command("warmane"))
async def cmd_warmane(msg: types.Message):
    async with aiohttp.ClientSession() as session:
        async with session.get('https://www.warmane.com/') as response:
            text = await response.text(encoding="utf-8")
            soup = BeautifulSoup(text, "html.parser")
            o = soup.find_all("span")[0].get_text()
            l = soup.find_all("span")[1].get_text()
            i = soup.find_all("span")[2].get_text()
            b = soup.find_all("span")[3].get_text()
            f = soup.find_all("span")[4].get_text()
            all = soup.find_all("span")[5].get_text()
            await msg.reply(f"♻ Warmane online:\n• Onyxia {o}\n• Lordaeron {l}\n• Icecrown {i}\n• Blackrock {b}\n• Frostwolf {f}\nJami online {all}")

@router.message(Command("circle"))
async def cmd_circle(msg: types.Message):
    async with aiohttp.ClientSession() as session:
        async with session.get('https://wowcircle.net/stat.html') as response:
            text = await response.text(encoding="utf-8")
            soup = BeautifulSoup(text, "html.parser")
            price = soup.find_all("div", {"class": "online"})
            all = soup.find_all("div", {"class": "num"})
            all_p = soup.find("div", {"class": "count"})
            x1, x5, x100, fun = price[0].get_text(), price[1].get_text(), price[2].get_text(), price[3].get_text()
            await msg.reply(f"♻ Circle online:\n• X1 {x1[8:]}\n• X5 {x5[8:]}\n• X100 {x100[8:]}\n• Fun {fun[8:]}\nJami onlayn {all[1].get_text()}\nJami patchdagi onlayn {all_p.get_text()}")

@router.message(Command("sirus"))
async def cmd_sirus(msg: types.Message):
    await msg.reply("Tez orada")

    
