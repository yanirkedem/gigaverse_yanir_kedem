from pyrogram import Client, filters
import asyncio
from os import getenv
from dotenv import load_dotenv

load_dotenv()

async def main():
    bot = Client("gigaverse_yanir_project", api_id=getenv('api_id'), api_hash=getenv('api_hash'),bot_token=getenv('bot_token'))
    async with bot:
        asyncio.sleep(5)
        await bot.send_message("me", "Hi!")

asyncio.run(main())