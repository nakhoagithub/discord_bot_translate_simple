token = '' #token of discord server

# lib => googletrans, discord.py
# code language: https://py-googletrans.readthedocs.io/en/latest/

from googletrans import Translator
import discord
from discord.ext import commands

client = commands.Bot(command_prefix = '.')

code_lang = 'vi -> Tiếng Việt\
\nen -> English\
\nja -> Japanese\
\nko -> Korean\
\nru -> Russian\
\nth -> Thai\
\nhu -> Hungarian\
\nfr -> French\
\nde -> German\
\nuk -> Ukrainian\
\nzh-cn -> Chinese (simplified)\
\nzh-tw -> Chinese (traditional)\
\nlo -> Lao\
\nes -> Spanish'

def translate(data):
    content = data[0].replace('.translate', '').strip()
    code = data[-1].strip()

    # #khởi tạo là xử lý dịch từ api
    translator = Translator()
    try:
        result = translator.translate(content, dest=code)
        pass
    except ValueError as e:
        return 'Sai Mã ngôn ngữ. Vui lòng chat **.code** để được trợ giúp'
        pass

    return result.text

def get_split(content):
    return content.split('--')

@client.event
async def on_ready():
    print("Bot Online")

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    s = get_split(message.content)
    if len(s) > 1:
        if message.content.startswith('.translate'):
            await message.channel.send(translate(s))
    else:
        if message.content.startswith('.translate'):
            await message.channel.send("Tham số sai. Vui lòng chat **.help** để được trợ giúp")

    if message.content.startswith('.help'):
        await message.channel.send('Dịch một đoạn văn bản với các tham số như sau:\n<**.translate**> <**Nội dung**> <**--Mã ngôn ngữ**>\nVí dụ: **.translate Hello --vi**\nXem các mã ngôn ngữ chat lệnh **.code**')

    if message.content.startswith('.code'):
        await message.channel.send(code_lang)

client.run(token)
