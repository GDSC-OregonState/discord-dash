from discord.ext import commands
import os
class Ready(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @commands.Cog.listener()
    async def on_ready(self):
        readyMsg = f"Hi {self.bot.user.display_name} is now online!"
        channelId = int(os.getenv("GENERAL_CHAT_ID"))
        await self.bot.get_channel(channelId).send(readyMsg)

        


async def setup(bot):
    await bot.add_cog(Ready(bot))