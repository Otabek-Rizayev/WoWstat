import aiohttp
import asyncio
from bs4 import BeautifulSoup

async def main():
	async with aiohttp.ClientSession() as session:
		async with session.get('https://wowcircle.net/stat.html') as response:
			text = await response.text(encoding="utf-8")
			soup = BeautifulSoup(text, "html.parser")
			for i in soup.find_all("div", {"class": "online"}):
				print(i)
				#price = soup.find_all(span="online")[22].get_text()
				#print(f"♻ Circle online: {price}")

asyncio.run(main())
#wm-ui-plugin-statistics