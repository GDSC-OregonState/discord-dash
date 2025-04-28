import time
from discord.ext import commands
import discord
import os
class Ping(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    

    async def ping(self, ctx, member: discord.Member = None):
        """
        Check bot's latency or ping a member
        """
        if member:
            await ctx.send(f"{member.mention} You've been pinged!")
        else:
            start_time = time.time()
            message = await ctx.send("Pinging...")
            end_time = time.time()

            round_trip = (end_time - start_time) * 1000
            api_latency = self.bot.latency * 1000

            embed = discord.Embed(
                title="🏓 Pong!",
                description=f"**Bot Latency**: {round_trip:.2f}ms\n**API Latency**: {api_latency:.2f}ms",
                color=discord.Color.green() if round_trip < 200 else discord.Color.orange()
            )
            
            await message.edit(content=None, embed=embed)


async def setup(bot):
    await bot.add_cog(Ping(bot))