from aiogram import types
from loader import dp
import requests
from bs4 import BeautifulSoup
from states.login import Login
from aiogram.dispatcher import FSMContext

@dp.message_handler(commands="login", state=None)
async def bot_echo(msg: types.Message):
    await msg.answer("Введите имя пользователя (логин):")
    
    await Login.username.set()

@dp.message_handler(state=Login.username)
async def username(msg: types.Message, state:FSMContext):
    username = msg.text
    load_username = await state.update_data({'username': username})
    await msg.answer("Введите пароль:")
    await Login.next()

@dp.message_handler(state=Login.password)
async def password(msg: types.Message, state:FSMContext):
    password = msg.text
    load_password = await state.update_data({'password': password})
    payload = await state.get_data()
    
    page = ('http://iwow.uz/ru/panel')
    url = ('http://iwow.uz/ru/login')
    try:
        with requests.session() as session:
            session.post(url, data=payload)
            r = session.get(page)
            soup = BeautifulSoup(r.text, 'html.parser')
            user_name = soup.find("td", class_="uk-table-expand").get_text()
            mail = soup.find_all("td", class_="uk-table-expand")[1].get_text()
            ip = soup.find_all("td", class_="uk-table-expand")[2].get_text()
            profiles = soup.find_all("tr")[4:]
            name_list = []
            race_list = []
            class_list = []
            lvl_list = []
            time_list = []
            coin_list = []

            for name in profiles:
                names = name.find_all("td")[0].get_text()
                race = name.select("td")[1]
                lvl = name.find_all("td")[2].get_text()
                time = name.find_all("td")[3].get_text()
                coin = name.find_all("td")[4].get_text()
                name_list.append(names)
                lvl_list.append(lvl)
                time_list.append(time)
                coin_list.append(coin)

                for img_race in race.select("img")[:1]:
                    race_title = img_race['title']
                    race_list.append(race_title)
                for img_class in race.select("img")[1:]:
                    class_title = img_class['title']
                    class_list.append(class_title)
        await msg.answer("ℹ️ ДЕТАЛЬНАЯ ИНФОРМАЦИЯ ОБ АККАУНТЕ\n"
                             f"<b>┌Логин:</b> {user_name}\n"
                             f"<b>├Email почта:</b> {mail}\n"
                             f"<b>└Последнее IP:</b> {ip}\n\n")

        for a, b, c ,d, e, f in zip(name_list, race_list, class_list, lvl_list, time_list, coin_list):
            await msg.answer(f"👥 СПИСОК ПЕРСОНАЖЕЙ\n"
                             f"ИМЯ: <b>{a} |</b> РАССА: <b>{b} |</b> КЛАСС: <b>{c} |</b> УРОВЕНЬ: <b>{d} |</b> СЫГРАННОЕ ВРЕМЯ: <b>{e} |</b> ДЕНЕГ: <b>{f}</b>")

    except:
        await msg.answer("Авторизация не удалась!")
    await state.finish()