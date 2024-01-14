from pyrogram import Client, filters
import time 
from os import getenv
from dotenv import load_dotenv

load_dotenv()

bot = Client("gigaverse_yanir_project", api_id=getenv('api_id'), api_hash=getenv('api_hash'),bot_token=getenv('bot_token'))

@bot.on_message(filters.command('start'))
async def command1(bot, message):
    print(message.chat.username,message)
    await bot.send_message(message.chat.id,"Hola. You Welcome ")

@bot.on_message(filters.command('help'))
def command1(bot, message):
    time.sleep(5)
    bot.send_message(message.chat.id,"If You Need Help Call: +5511964531831 ")

bot.run()