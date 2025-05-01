from discord.ext import commands
import discord
from hunt_the_wumpus import Hunt_The_Wumpus

class Fun(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.index = 1
        self.game = Hunt_The_Wumpus(8)
        self.game.init_game()

    @commands.command(name="htw", help="Play hunt the wumpus")
    async def hunt_the_wumpus(self, ctx, action: str = None):
        await ctx.send(self.game.play_game(action))

async def setup(bot):
    await bot.add_cog(Fun(bot))