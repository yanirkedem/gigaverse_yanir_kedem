from pyrogram import Client, filters
import asyncio


api_id = 27545240
api_hash = "564982ff2fe3f0970d2403e47c3daaf9"
bot_token = "6945504868:AAGXjaQoIeVoHtuHW60S3z7cVQT2F3HOZbI"

async def main():
    bot = Client("gigaverse_yanir_project", api_id=api_id, api_hash=api_hash,bot_token=bot_token)
    async with bot:
        await bot.send_message("me", "Hi!")

asyncio.run(main())