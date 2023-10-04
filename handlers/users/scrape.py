import requests
import aiohttp
import asyncio
from bs4 import BeautifulSoup


# page = ('http://iwow.uz/ru/panel')
# url = ('http://iwow.uz/ru/login')

# payload = {
#                 'username': 'virtualman',
#                 'password': '5561190OtA'
#             }

# with requests.session() as session:
#     session.post(url, data=payload)
#     r = session.get(page)
#     soup = BeautifulSoup(r.text, 'html.parser')
#     user_name = soup.find("td", class_="uk-table-expand").get_text()
#     mail = soup.find_all("td", class_="uk-table-expand")[1].get_text()
#     ip = soup.find_all("td", class_="uk-table-expand")[2].get_text()


# print(f"ℹ️ ДЕТАЛЬНАЯ ИНФОРМАЦИЯ ОБ АККАУНТЕ\n"
#           f"┌Логин: {user_name}\n"
#           f"├Email почта: {mail}\n"
#           f"└Последнее IP: {ip}\n\n"
#           f"👥 СПИСОК ПЕРСОНАЖЕЙ")
    
# #rasm = soup.find_all('img', class_="uk-border-rounded", title=True)

# profiles = soup.find_all("tr")[4:]
# rasm = soup.select("td")

# name_list = []
# race_list = []
# class_list = []
# lvl_list = []
# time_list = []
# coin_list = []

# for name in profiles:
#     names = name.find_all("td")[0].get_text()
#     race = name.select("td")[1]
#     lvl = name.find_all("td")[2].get_text()
#     time = name.find_all("td")[3].get_text()
#     coin = name.find_all("td")[4].get_text()
#     name_list.append(names)
#     lvl_list.append(lvl)
#     time_list.append(time)
#     coin_list.append(coin)

#     for img_race in race.select("img")[:1]:
#         race_title = img_race['title']
#         race_list.append(race_title)
#     for img_class in race.select("img")[1:]:
#         class_title = img_class['title']
#         class_list.append(class_title)

# for a, b, c ,d, e, f in zip(name_list, race_list, class_list, lvl_list, time_list, coin_list):
#     print(f"ИМЯ: {a} | РАССА: {b} | КЛАСС: {c} | УРОВЕНЬ: {d} | СЫГРАННОЕ ВРЕМЯ: {e} | ДЕНЕГ: {f}")


