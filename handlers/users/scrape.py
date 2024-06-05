import aiohttp
from bs4 import BeautifulSoup
import cloudscraper

async def fetch(session, url):
    async with session.get(url) as response:
        return await response.text(encoding="utf-8")

async def off_func(url):
    scraper = cloudscraper.create_scraper()
    headers = scraper.headers
    cookies = scraper.cookies

    async with aiohttp.ClientSession(headers=headers, cookies=cookies) as session:
        content = await fetch(session, "https://www.wowprogress.com/realms/rank/eu")
        soup = BeautifulSoup(content, "html.parser")
        tr = soup.find_all("tr")
        td = soup.find_all("td")
        table = soup.find_all("table", attrs={"class":"realm_list"})
        data = []
        for tb in table:
            trs = tb.find_all("tr")
            for i, tds in enumerate(trs):
                meta = tds.find_all("td")
                if i > 0 and i< 8:
                        await return f"ℹ {meta[1].text}| ♻️ {meta[5].text} | ⚔ {meta[2].text} | 🌐 {meta[3].text}"
