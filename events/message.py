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

async def setup(bot):
    await bot.add_cog(Message(bot))