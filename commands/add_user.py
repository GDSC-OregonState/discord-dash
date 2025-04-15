import os
import requests
from discord.ext import commands

class AddUser(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    async def add_user(self, ctx, username):
        api_token = os.getenv("GITHUB_API_TOKEN") 
        url = f"https://api.github.com/orgs/GDSC-OregonState/memberships/{username}" 
        headers = {
            "Authorization": f"Bearer {api_token}",
            "Accept": "application/vnd.github+json",
            "X-GitHub-Api-Version": "2022-11-28",
        }

        json = {"role": "member"}
        response = requests.put(url, headers=headers, json=json)

        if (response.status_code == 200):
            await ctx.send(f"User: {username} has received an invitation to the Github Org!!")
        else:
            await ctx.send(f"Failed to add user!! This was due to the following reasons: {response.json()}")

async def setup(bot):
    await bot.add_cog(AddUser(bot))