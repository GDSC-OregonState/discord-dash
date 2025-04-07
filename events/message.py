import commands as mycommands

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
        if "add-user" in message.content.lower() and len(message.content.lower() > 1):
            username = message.content.lower().split(" ")[1]
            await message.channel.send(mycommands.add_user(username))
        else:
            await message.channel.send(mycommands.help())

async def setup(bot):
    await bot.add_cog(Message(bot))