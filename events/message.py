from discord.ext import commands
from google import genai
import os

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))




class Message(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):

        if message.author.bot:
            return
        if message.content.lower() == "hello bot":
            await message.channel.send(f"Hello {message.author.name}")
        if "gemini" in message.content.lower():
            response = client.models.generate_content(
                model="gemini-2.0-flash",
                contents=message.content,
            )
            await message.channel.send(response.text)

async def setup(bot):
    await bot.add_cog(Message(bot))