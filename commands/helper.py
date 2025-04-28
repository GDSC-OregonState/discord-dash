from discord.ext import commands
import discord
import os

class Helper(commands.Cog):
    """Provide help information and lists all available commands!"""
    def __init__(self, bot):
        self.bot = bot
   
    @commands.command(help="This command lists all the things you can do with this bot!")
    async def helper(self, ctx):
        embed = discord.Embed(
            title="🤖 Available Bot Commands",
            description="Here is everything you can do with this bot!",
            color=discord.Color.blue()
        )
        
        # Create a dictionary to organize commands by cog
        cogs = {}
        no_category = []
        
        # Populate the dictionary
        for command in self.bot.commands:
            if command.cog:
                cog_name = command.cog.qualified_name
                if cog_name in cogs:
                    cogs[cog_name].append(command)
                else:
                    cogs[cog_name] = [command]
            else:
                no_category.append(command)

        for cog_name, commands_list in cogs.items():
            commands_text = ""
            for cmd in commands_list:
                desc = cmd.help if cmd.help else "No description"
                emoji = "⚙️"  # Default emoji
                if "music" in cog_name.lower():
                    emoji = "🎵"
                elif "mod" in cog_name.lower():
                    emoji = "🛡️"
                elif "fun" in cog_name.lower():
                    emoji = "🎮"
                elif "util" in cog_name.lower():
                    emoji = "🔧"
                
                commands_text += f"{emoji} **{cmd.name}** - {desc}\n"
            embed.add_field(
                name=f"📁 {cog_name}",
                value=commands_text or "No commands",
                inline=False
            )
        if no_category:
            commands_text = ""
            for cmd in no_category:
                desc = cmd.help if cmd.help else "No description"
                if len(desc) > 50:
                    desc = desc[:47] + "..."
                commands_text += f"🔹 **{cmd.name}** - {desc}\n"
            
            embed.add_field(
                name="🗃️ Uncategorized",
                value=commands_text,
                inline=False
            )    
        
        await ctx.send(embed=embed)

    @commands.command(help="Describes a given command!")
    async def describe(self, ctx, arg):
        if not arg:
            ctx.send("Oh no! Make you add what command you want to describe!")
        else:
            ctx.send(f"This is a description of {arg}")
async def setup(bot):
    await bot.add_cog(Helper(bot))