from discord.ext import commands
import discord
import os
class Ping(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @commands.command()
    async def ping(self, ctx, member: discord.Member):
        await ctx.send(f"{member.mention} You've been pinged!")


async def setup(bot):
    await bot.add_cog(Ping(bot))