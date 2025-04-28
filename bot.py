import discord
import os
from discord.ext import commands
from config import CONFIG
TOKEN = os.getenv("DISCORD_TOKEN")


class Bot(commands.Bot):
    def __init__(self):
        intents = discord.Intents.default()
        intents.message_content = True
        super().__init__(
            command_prefix=CONFIG["prefix"],
            intents = intents
        )
    
    
    async def setup_hook(self):
        #commands
        await self.load_extension("commands.ping")
        await self.load_extension("commands.helper")

        #Events
        await self.load_extension("events.ready")
        await self.load_extension("events.message")
        
if TOKEN:
    Bot().run(TOKEN)
else:
    print("==LOG== ERROR DISCORD TOKEN NOT FOUND")