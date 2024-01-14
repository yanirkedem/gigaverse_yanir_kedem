from pyrogram import Client, filters
import time 

api_id = 27545240
api_hash = "564982ff2fe3f0970d2403e47c3daaf9"
bot_token = "6945504868:AAGXjaQoIeVoHtuHW60S3z7cVQT2F3HOZbI"

bot = Client("gigaverse_yanir_project", api_id=api_id, api_hash=api_hash,bot_token=bot_token)

@bot.on_message(filters.command('start'))
async def command1(bot, message):
    print(message.chat.username,message)
    await bot.send_message(message.chat.id,"Hola. You Welcome ")

@bot.on_message(filters.command('help'))
def command1(bot, message):
    time.sleep(5)
    bot.send_message(message.chat.id,"If You Need Help Call: +5511964531831 ")

bot.run()