from commands.add_user import add_user
from commands.help import help

from discord.ext import commands

class Message(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author.bot:
            return
        if message.content.lower() == "hello bot":
            await message.channel.send(f"Hello {message.author.name}")
        elif "add-user" in message.content.lower():
            component_parts = message.content.lower().split(" ")
            if (len(component_parts) > 1):
                username = component_parts[1]
                await message.channel.send(add_user(username))
        else:
            await message.channel.send(help())

async def setup(bot):
    await bot.add_cog(Message(bot))