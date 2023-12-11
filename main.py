import os
import disnake
import config
import intents as intents
from disnake.ext import commands
from bs4 import BeautifulSoup
import requests


client = disnake.Client()
intents.members = True
intents.message_content = True

intents = disnake.Intents.all()
bot = commands.Bot(command_prefix='!', intents=intents)


@bot.event
async def on_ready():
    print(f'{bot.user} запустился')

    await bot.change_presence( status= disnake.Status.online, activity= disnake.Game('/help'))

for file in os.listdir("./cogs"):
    if file.endswith(".py"):
        bot.load_extension(f'cogs.{file[:-3]}')

@bot.slash_command(description='Последние новости в дискорде')
async def news(inter):
    URL = 'https://dtf.ru/tag/discord'
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, 'html.parser')
    post = soup.find('div', class_='feed__item l-island-round')
    title = post.find('div', class_='content-title content-title--short l-island-a').text.strip()
    date = post.find('time', class_='time', title=True)["title"].strip()
    url = post.find('a',
                    class_='content-header__item content-header-number', href=True)["href"].strip()
    await inter.response.send_message(f"{title}\n\nНовость от: {date}\nЧитать полную статью👇\n{url}", ephemeral=True)

@bot.slash_command(description='Информация о погоде')
async def weather(inter):
    URL = 'https://weather.rambler.ru/v-verkhney-pyshme/today/'
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, 'html.parser')
    vet = soup.find('div', class_='hjtR wind HbwD NCAm').text.strip()
    post = soup.find('span', class_='Njqa').text.strip()
    dav = soup.find('div', class_='hjtR pressure HbwD NCAm').text.strip()
    vos = soup.find('div', class_='hjtR rise HbwD NCAm').text.strip()
    zak = soup.find('div', class_='hjtR set HbwD NCAm').text.strip()
    svet = soup.find('div', class_='hjtR daylight HbwD NCAm').text.strip()
    url = 'https://st.europaplus.ru/mf/p/164922/programs/019/program-detail-m/8da14a275a26a632cf5d3559812e1421.jpg'
    await inter.response.send_message(f'🏙️ Погода на сегодня: {post}\n🌬️ {vet}\n🌄 {vos}\n🌇 {zak}\n🌍 {svet}\n{url}', ephemeral=True)
bot.run('MTA2NTExNDcyMzY3MjEzMzY0NA.GJZ72y.i_lIv8njfTeq9Cb_XPRxJUl-KEktyXROlk1f5M')

